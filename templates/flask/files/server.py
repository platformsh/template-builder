import traceback
import uuid
import sys

import flask
import flask.json
import gevent.pywsgi
import pymysql
import redis

from platformshconfig import Config

app = flask.Flask(__name__)
config = Config()


@app.route('/')
def root():
    tests = {
        "database": wrap_test(test_mysql, config.credentials("database")),
        "redis": wrap_test(test_redis, config.credentials("rediscache"))
    }
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
        port=instance["port"],
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
    http_server = gevent.pywsgi.WSGIServer(('127.0.0.1', int(config.port)), app)
    http_server.serve_forever()
