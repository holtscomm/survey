"""
API endpoints
"""
def return_json_response(data, additional_info={}, status_code=200):
    d = {
        'data': data,
        'status': status_code,
    }

    d.update(additional_info)

    return d
