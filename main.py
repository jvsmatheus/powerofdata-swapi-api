from flask import jsonify
from app.controllers.swapi_controller import handle_request
from app.exceptions.api_exceptions import ApiException, InvalidFilterException, InvalidSortException
from app.models.response import ApiResponse

def main(request):
    try:
        return handle_request(request)

    except ApiException as ex:
        response = ApiResponse(
            success=False,
            message=ex.message
        )
        return jsonify(response.to_dict()), ex.status_code
    
    except InvalidFilterException as ex:
        response = ApiResponse(
            success=False,
            message=ex.message
        )
        return jsonify(response.to_dict()), ex.status_code
    
    except InvalidSortException as ex:
        response = ApiResponse(
            success=False,
            message=ex.message
        )
        return jsonify(response.to_dict()), ex.status_code

    except Exception:
        response = ApiResponse(
            success=False,
            message="Internal server error"
        )
        return jsonify(response.to_dict()), 500