import logging
import json
import service.person_service as service

from flask import Flask, Response, request

logging.basicConfig(level=logging.INFO, force=True)


def create_app():
    app = Flask(__name__)

    @app.route('/people', methods=['GET'])
    def get_all_people() -> Response:
        people = service.get_all_person()

        return Response(response=json.dumps(people), status=200, mimetype='application/json')

    @app.route('/friend_list', methods=['GET'])
    def get_friends_of_person() -> Response:
        query_parameters = request.args
        name = query_parameters.get('name')
        friend_list = service.get_friend_list(name)

        return Response(response=json.dumps(friend_list), status=200, mimetype='application/json')

    return app
