import os
import logging
import sys
from datetime import datetime, timezone, timedelta

import numpy
from flask import jsonify
import firebase_admin
from firebase_admin import firestore

from .app import app
from .utils import detect_video, create_gif
from .config import FILEPATH, DIR

logger = logging.getLogger(__name__)
logger.propagate = False

JST=timezone(timedelta(hours=+9), "JST")

if not firebase_admin._apps:
    default_app = firebase_admin.initialize_app()


@app.route('/')
def root():
    return ""

# TODO: authentication作成
@app.route("/api/create_status", methods=["GET"])
def create_status():
    # TODO: cronでしか許可しない
    client = firestore.Client()
    if (
        client.collection("status")
        .where("updated_at", "<=", datetime.now(tz=JST) - timedelta(hour=1))
        .get()
    ):
        response_status = {"status": False}
        app.logger.info(response_status)
        return response_status
    person_counts = detect_video(1)
    umbrella_counts = detect_video(28)
    app.logger.info(f"person_counts: {person_counts}")
    app.logger.info(f"umbrella_counts: {umbrella_counts}")
    person_average = int(numpy.average(person_counts)) if person_counts else 0
    umbrella_average = int(numpy.average(umbrella_counts)) if umbrella_counts else 0
    updated_at = datetime.now(tz=JST)

    ref = client.collection("status").document(updated_at.isoformat())
    ref.set(
        {
            "person": person_average,
            "umbrella": umbrella_average,
            "updated_at": updated_at,
        },
        merge=False,
    )
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
    ref = client.collection("status").order_by(
        "updated_at", direction=firestore.Query.DESCENDING
    )
    results=[doc.to_dict() for doc in ref.get()]
    for result in results:
        for k,v in result.items():
            if k == "updated_at":
                result.update({k:datetime.fromtimestamp(v.timestamp()).astimezone(JST).isoformat()})
    return jsonify(results)
