import logging
import json
import service.person_service as service

from flask import Flask, Response, request

from src.mapper.person_mapper import map_person_to_dict

logging.basicConfig(level=logging.INFO, force=True)


def create_app():
    app = Flask(__name__)

    @app.route('/people', methods=['GET'])
    def get_all_people() -> Response:
        people = service.get_all_person()

        people_dict = list(map(lambda x: map_person_to_dict(x), people))

        return Response(response=json.dumps(people_dict), status=200, mimetype='application/json')

    @app.route('/friend_list', methods=['GET'])
    def get_friends_of_person() -> Response:
        query_parameters = request.args
        name = query_parameters.get('name')
        friend_list = service.get_friend_list(name)

        friend_list_dict = list(map(lambda x: map_person_to_dict(x), friend_list))

        return Response(response=json.dumps(friend_list_dict), status=200, mimetype='application/json')

    @app.route('/non_friend_list', methods=['GET'])
    def get_non_friend_list() -> Response:
        query_parameters = request.args
        name = query_parameters.get('name')
        non_friend_list = service.get_non_friend_list(name)

        non_friend_list_dict = list(map(lambda x: map_person_to_dict(x), non_friend_list))

        return Response(response=json.dumps(non_friend_list_dict), status=200, mimetype='application/json')


    return app
