from app.services.swapi_service import SwapiService
from app.exceptions.api_exceptions import BadRequestException, UnauthorizedException
from flask import jsonify

import os

API_KEY = os.getenv("API_KEY")

def handle_request(request):
    _validate_api_key(request)

    path_parts = request.path.strip("/").split("/")
    if len(path_parts) != 2 or path_parts[0] != "api":
        raise BadRequestException("Invalid endpoint. Use /api/<resource>")

    resource = path_parts[-1]
    query_params = request.args.to_dict()

    service = SwapiService()
    response = service.list(resource, query_params)

    return jsonify(response.to_dict()), 200


def _validate_api_key(request):
    api_key = request.headers.get("x-api-key")
    if not api_key or api_key != API_KEY:
        raise UnauthorizedException("Invalid API Key")