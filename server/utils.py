import os

import cv2
import numpy

classes_90 = [
    "background",
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "unknown",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "unknown",
    "backpack",
    "umbrella",
    "unknown",
    "unknown",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "unknown",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "unknown",
    "dining table",
    "unknown",
    "unknown",
    "toilet",
    "unknown",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "unknown",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]
TESTDIR = "testdata"
PBFILE = "ssd_mobilenet_v2_coco_2018_03_29.pb"
PBTXTFILE = "ssd_mobilenet_v2_coco_2018_03_29.pbtxt"
n = 0
FILEPATH = "statics/cap.mp4"


def detect_video(filepath: str, category: int = 1):
    if not os.path.exists(filepath):
        return
    global tensorflowNet
    tensorflowNet = cv2.dnn.readNetFromTensorflow(
        f"{TESTDIR}/{PBFILE}", f"{TESTDIR}/{PBTXTFILE}"
    )
    cap = cv2.VideoCapture(filepath)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    skip_count = int(frame_count / 10)
    print(f"frame count: {frame_count}")
    count = []
    for i in range(1, frame_count, skip_count):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        _, frame = cap.read()
        print(f"frame: {int(cap.get(cv2.CAP_PROP_POS_FRAMES))}")
        count.append(detect_image(frame, category))
    return count


def detect_image(frame: numpy.ndarray, category: int = 1) -> str:
    rows, cols, channels = frame.shape
    tensorflowNet.setInput(
        cv2.dnn.blobFromImage(frame, size=(640, 640), swapRB=True, crop=False)
    )
    networkOutput = tensorflowNet.forward()
    count = 0
    write_flag = []
    for detection in networkOutput[0, 0]:
        if detection[1] != category:
            continue
        count += 1
        score = float(detection[2])
        if score > 0.2:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv2.rectangle(
                frame,
                (int(left), int(top)),
                (int(right), int(bottom)),
                (0, 0, 255),
                2,
            )
            cv2.putText(
                frame,
                classes_90[int(detection[1])],
                (int(left), int(top)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 255),
                2,
                8,
            )
    global n
    cv2.imwrite(f"statics/out_{category}_{str(n).zfill(2)}.png", frame)
    n += 1
    return count


def create_gif(category: int = 1) -> bool:
    from PIL import Image
    import glob

    files = glob.glob(f"statics/out_{category}_*.png")
    if len(files) < 1:
        raise Exception("there is no png file")
    images = [Image.open(file) for file in files]
    images[0].save(f"statics/{category}.gif", save_all=True, append_images=images[1:])
    return True


if __name__ == "__main__":
    detect_video(FILEPATH)
    create_gif()
