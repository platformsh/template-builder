import base64
import json
import os
import traceback
import uuid
import sys

import flask
import gevent.pywsgi
import pymysql
import redis


app = flask.Flask(__name__)

relationships = json.loads(
    base64.b64decode(os.environ["PLATFORM_RELATIONSHIPS"]))


@app.route('/')
def root():
    tests = {}
    tests["mysql"] = wrap_test(test_mysql, relationships["mysql"][0])
    tests["redis"] = wrap_test(test_redis, relationships["redis"][0])
    return flask.json.jsonify(tests)


def wrap_test(callback, *args, **kwargs):
    try:
        result = callback(*args, **kwargs)
        return {
            "status": "OK",
            "return": result,
        }
    except Exception:
        return {
            "status": "ERROR",
            "error": traceback.format_exception(*sys.exc_info())
        }


def test_mysql(instance):
    connection = pymysql.connect(
        host=instance["host"],
        user=instance["username"],
        password=instance["password"],
        db=instance["path"],
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

    finally:
        connection.close()


def test_redis(instance):
    r = redis.StrictRedis(
        host=instance["host"],
        port=instance["port"],
        db=0,
    )
    key_name = "foo-%s" + str(uuid.uuid4())
    value = b"bar"

    r.set(key_name, "bar")
    assert value == r.get(key_name)


if __name__ == "__main__":
    http_server = gevent.pywsgi.WSGIServer(
        ('127.0.0.1', int(os.environ["PORT"])), app)
    http_server.serve_forever()
