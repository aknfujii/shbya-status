import os
from datetime import datetime

import numpy
from flask import jsonify
import firebase_admin
from firebase_admin import firestore

from app import db, app
from models import Status, status_schema
from utils import detect_video, FILEPATH, create_gif

# TODO: authentication作成
@app.route("/api/create_status", methods=["GET"])
def create_status():
    if not os.path.exists(FILEPATH):
        import subprocess
        subprocess.run("./DL.sh")
    if Status.query.filter(Status.updated == datetime.fromtimestamp(
            os.stat(FILEPATH).st_ctime)).all():
        return False
    person_counts = detect_video(FILEPATH, 1)
    umbrella_counts = detect_video(FILEPATH, 28)
    print(f"person_counts: {person_counts}")
    print(f"umbrella_counts: {umbrella_counts}")
    person_average = int(numpy.average(person_counts)) if person_counts else 0
    umbrella_average = int(
        numpy.average(umbrella_counts)) if umbrella_counts else 0
    updated_at = datetime.fromtimestamp(os.stat(FILEPATH).st_ctime)

    client = firestore.Client()
    ref = client.collection(u'status').document()
    ref.set(
        {
            "person": person_average,
            "umbrella": umbrella_average,
            "updated_at": updated_at,
        },
        merge=False)
    return True


@app.route("/api/get_status", methods=["GET"])
def get_status():
    """

    Returns:
        Status data
    """
    firebase_admin.initialize_app()
    client = firestore.Client()
    ref = client.collection(u'status')
    return jsonify([doc.to_dict() for doc in ref.get()])