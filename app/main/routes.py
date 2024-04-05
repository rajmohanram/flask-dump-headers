from flask import send_from_directory, request, render_template, jsonify, Response
from app.main import bp
import os
import json
import logging


@bp.route('/')
def index():
    logging.info(request.headers)
    if request.headers['Accept'] == "application/json":
        return Response(response=json.dumps(dict(request.headers)), status=200,
                        mimetype="application/json")
    return render_template("index.html", request_headers = request.headers)


@bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(bp.root_path, '../static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


