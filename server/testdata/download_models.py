#!/usr/bin/env python
# code from https://github.com/opencv/opencv_extra.git

from __future__ import print_function
import hashlib
import os
import sys
import tarfile
import requests

if sys.version_info[0] < 3:
    from urllib2 import urlopen
else:
    from urllib.request import urlopen


class Model:
    MB = 1024 * 1024
    BUFSIZE = 10 * MB

    def __init__(self, **kwargs):
        self.name = kwargs.pop("name")
        self.url = kwargs.pop("url", None)
        self.downloader = kwargs.pop("downloader", None)
        self.filename = kwargs.pop("filename")
        self.sha = kwargs.pop("sha", None)
        self.archive = kwargs.pop("archive", None)
        self.member = kwargs.pop("member", None)

    def __str__(self):
        return "Model <{}>".format(self.name)

    def printRequest(self, r):
        def getMB(r):
            d = dict(r.info())
            for c in ["content-length", "Content-Length"]:
                if c in d:
                    return int(d[c]) / self.MB
            return "<unknown>"

        print("  {} {} [{} Mb]".format(r.getcode(), r.msg, getMB(r)))

    def verify(self):
        if not self.sha:
            return False
        print("  expect {}".format(self.sha))
        sha = hashlib.sha1()
        try:
            with open(self.filename, "rb") as f:
                while True:
                    buf = f.read(self.BUFSIZE)
                    if not buf:
                        break
                    sha.update(buf)
            print("  actual {}".format(sha.hexdigest()))
            return self.sha == sha.hexdigest()
        except Exception as e:
            print("  catch {}".format(e))

    def get(self):
        if self.verify():
            print("  hash match - skipping")
            return True

        basedir = os.path.dirname(self.filename)
        if basedir and not os.path.exists(basedir):
            print("  creating directory: " + basedir)
            os.makedirs(basedir, exist_ok=True)

        if self.archive or self.member:
            assert self.archive and self.member
            print("  hash check failed - extracting")
            print("  get {}".format(self.member))
            self.extract()
        elif self.url:
            print("  hash check failed - downloading")
            print("  get {}".format(self.url))
            self.download()
        else:
            assert self.downloader
            print("  hash check failed - downloading")
            sz = self.downloader(self.filename)
            print("  size = %.2f Mb" % (sz / (1024.0 * 1024)))

        print(" done")
        print(" file {}".format(self.filename))
        return self.verify()

    def download(self):
        try:
            r = urlopen(self.url, timeout=60)
            self.printRequest(r)
            self.save(r)
        except Exception as e:
            print("  catch {}".format(e))

    def extract(self):
        try:
            with tarfile.open(self.archive) as f:
                assert self.member in f.getnames()
                self.save(f.extractfile(self.member))
        except Exception as e:
            print("  catch {}".format(e))

    def save(self, r):
        with open(self.filename, "wb") as f:
            print("  progress ", end="")
            sys.stdout.flush()
            while True:
                buf = r.read(self.BUFSIZE)
                if not buf:
                    break
                f.write(buf)
                print(">", end="")
                sys.stdout.flush()


def GDrive(gid):
    def download_gdrive(dst):
        session = requests.Session()  # re-use cookies

        URL = "https://docs.google.com/uc?export=download"
        response = session.get(URL, params={"id": gid}, stream=True)

        def get_confirm_token(response):  # in case of large files
            for key, value in response.cookies.items():
                if key.startswith("download_warning"):
                    return value
            return None

        token = get_confirm_token(response)

        if token:
            params = {"id": gid, "confirm": token}
            response = session.get(URL, params=params, stream=True)

        BUFSIZE = 1024 * 1024
        PROGRESS_SIZE = 10 * 1024 * 1024

        sz = 0
        progress_sz = PROGRESS_SIZE
        with open(dst, "wb") as f:
            for chunk in response.iter_content(BUFSIZE):
                if not chunk:
                    continue  # keep-alive

                f.write(chunk)
                sz += len(chunk)
                if sz >= progress_sz:
                    progress_sz += PROGRESS_SIZE
                    print(">", end="")
                    sys.stdout.flush()
        print("")
        return sz

    return download_gdrive


models = [
    Model(
        name="MobileNet-SSD v2 (TensorFlow)",
        url="http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz",
        sha="69c93d29e292bc9682396a5c78355b1dfe481b61",
        filename="ssd_mobilenet_v2_coco_2018_03_29.tar.gz",
    ),
    Model(
        name="MobileNet-SSD v2 (TensorFlow)",
        archive="ssd_mobilenet_v2_coco_2018_03_29.tar.gz",
        member="ssd_mobilenet_v2_coco_2018_03_29/frozen_inference_graph.pb",
        sha="35d571ac314f1d32ae678a857f87cc0ef6b220e8",
        filename="ssd_mobilenet_v2_coco_2018_03_29.pb",
    ),
]

# Note: models will be downloaded to current working directory
#       expected working directory is <testdata>/dnn
if __name__ == "__main__":

    selected_model_name = None
    if len(sys.argv) > 1:
        selected_model_name = sys.argv[1]
        print("Model: " + selected_model_name)

    failedModels = []
    for m in models:
        print(m)
        if selected_model_name is not None and not m.name.startswith(
            selected_model_name
        ):
            continue
        if not m.get():
            failedModels.append(m.filename)

    if failedModels:
        print("Following models have not been downloaded:")
        for f in failedModels:
            print("* {}".format(f))
        exit(15)
