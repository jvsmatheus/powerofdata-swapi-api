from app.exceptions.api_exceptions import InvalidFilterException, InvalidSortException


ALLOWED_FILTERS = {
    "people": {"name", "gender", "eye_color"},
    "films": {"title", "director", "producer"},
    "planets": {"name", "climate", "terrain"},
    "starships": {"name", "model", "manufacturer"}
}

EXACT_MATCH_FIELDS = {
    "gender"
}

def apply_filters(results: list, params: dict, resource: str) -> list:
    allowed_fields = ALLOWED_FILTERS.get(resource, set())
    
    invalid_filters = [
        key for key in params.keys()
        if key not in allowed_fields and key != "sort"
    ]

    if invalid_filters:
        raise InvalidFilterException(f"Invalid filters: {invalid_filters}. Allowed filters: {allowed_fields}")

    filters = {
        k: v for k, v in params.items()
        if k in allowed_fields
    }

    for key, value in filters.items():
        if key in EXACT_MATCH_FIELDS:
            results = [
                item for item in results
                if str(item.get(key, "")).lower() == value.lower()
            ]
        else:
            results = [
                item for item in results
                if value.lower() in str(item.get(key, "")).lower()
            ]

    return results


def apply_sort(results: list, params: dict, resource: str) -> list:
    sort = params.get("sort")
    if not sort:
        return results

    reverse = sort.startswith("-")
    field = sort.replace("-", "")

    allowed_fields = ALLOWED_FILTERS.get(resource, set())

    if field not in allowed_fields:
        raise InvalidSortException(f"Invalid sort field: {field}. Allowed sort fields: {allowed_fields}")

    return sorted(results, key=lambda x: x.get(field, ""), reverse=reverse)