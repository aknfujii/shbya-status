import os
import logging
from datetime import datetime

import numpy
from flask import jsonify
import firebase_admin
from firebase_admin import firestore

from app import app
from utils import detect_video, FILEPATH, DIR, create_gif

logger = logging.getLogger(__name__)

if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app()


# TODO: authentication作成
@app.route("/api/create_status", methods=["GET"])
def create_status():
    if not os.path.exists(FILEPATH):
        os.system("./DL.sh")
    client = firestore.Client()
    if client.collection(u'status').where(
            u'updated_at', u'==',
            datetime.fromtimestamp(os.stat(FILEPATH).st_ctime)).get():
        response_status = {"status": False}
        app.logger.info(response_status)
        return response_status
    person_counts = detect_video(FILEPATH, 1)
    umbrella_counts = detect_video(FILEPATH, 28)
    app.logger.info(f"person_counts: {person_counts}")
    app.logger.info(f"umbrella_counts: {umbrella_counts}")
    person_average = int(numpy.average(person_counts)) if person_counts else 0
    umbrella_average = int(
        numpy.average(umbrella_counts)) if umbrella_counts else 0
    updated_at = datetime.fromtimestamp(os.stat(FILEPATH).st_ctime)

    ref = client.collection(u'status').document()
    ref.set(
        {
            "person": person_average,
            "umbrella": umbrella_average,
            "updated_at": updated_at,
        },
        merge=False)
    if not glob.glob('{DIR}/*.png'):
        create_gif(1)
        create_gif(28)
    os.remove(f"{DIR}/cap.mp4")
    response_status = {"status": True}
    app.logger.info(response_status)
    return response_status


@app.route("/api/get_status", methods=["GET"])
def get_status():
    """

    Returns:
        Status data
    """
    client = firestore.Client()
    ref = client.collection(u'status')
    return jsonify([doc.to_dict() for doc in ref.get()])