ALLOWED_FILTERS = {
    "people": {"name", "gender", "eye_color"},
    "films": {"title", "director", "producer"},
    "planets": {"name", "climate", "terrain"},
    "starships": {"name", "model", "manufacturer"}
}

EXACT_MATCH_FIELDS = {
    "gender",
    "eye_color",
    "climate",
    "terrain"
}

def apply_filters(results: list, params: dict, resource: str) -> list:
    allowed_fields = ALLOWED_FILTERS.get(resource, set())

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


def apply_sort(results: list, params: dict) -> list:
    sort = params.get("sort")
    if not sort:
        return results

    reverse = sort.startswith("-")
    field = sort.replace("-", "")

    return sorted(results, key=lambda x: x.get(field, ""), reverse=reverse)