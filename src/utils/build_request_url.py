def build_request_url(base_url: str, params: dict):
    query_string = "&".join(f"filter[{key}]={value}" for key, value in params.items() if value is not None)
    return f"{base_url}?{query_string}"
