import time
import uuid

from flask import jsonify


def to_json(status, data):
    return jsonify({"status": status, "data": data}), status


def get_uuid():
    """
    Method generates universally unique identifier
    :return: unique alpha numeric string.
    """
    return str(uuid.uuid4()).replace("-", "").upper()


def get_current_ts():
    return time.strftime('%Y-%m-%d %H:%M:%S')
