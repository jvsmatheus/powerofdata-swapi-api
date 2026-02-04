from app.clients.swapi_client import SwapiClient
from app.models.response import ApiResponse
from app.utils.filter_utils import apply_filters, apply_sort
from app.exceptions.api_exceptions import NotFoundException

class SwapiService:

    def __init__(self):
        self.client = SwapiClient()

    def list(self, resource: str, params: dict):
        data = self.client.get(resource)

        results = data.get("results", [])
        if not results:
            raise NotFoundException("No results found")

        results = apply_filters(results, params, resource)
        results = apply_sort(results, params)

        response = ApiResponse(
            success=True,
            data=results
        )

        return response