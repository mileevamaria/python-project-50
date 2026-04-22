import json


def jsonify(diff):
    return json.dumps(diff, indent=2)
