import os
from datetime import datetime

import numpy
from flask import jsonify

from app import db, app
from models import Status, status_schema
from utils import detect_video, FILEPATH, create_gif


def create_status():
    if Status.query.filter(
        Status.updated == datetime.fromtimestamp(os.stat("statics/cap.mp4").st_ctime)
    ).all():
        return False
    person_counts = detect_video(FILEPATH, 1)
    umbrella_counts = detect_video(FILEPATH, 28)
    print(f"person_counts: {person_counts}")
    print(f"umbrella_counts: {umbrella_counts}")
    person_average = int(numpy.average(person_counts)) if person_counts else 0
    umbrella_average = int(numpy.average(umbrella_counts)) if umbrella_counts else 0
    updated = datetime.fromtimestamp(os.stat("statics/cap.mp4").st_ctime)
    new_status = Status(person=person_average, umbrella=umbrella_average, updated=updated)
    db.session.add(new_status)
    db.session.commit()
    create_gif(1)
    create_gif(28)
    return True


@app.route("/api/get_status", methods=["GET"])
def get_status():
    """

    Returns:
        Status data
    """
    create_status()
    query = Status.query.all()
    return jsonify(status_schema.dump(query))
