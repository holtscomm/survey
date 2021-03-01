"""
API endpoints
"""
def return_json_response(data, additional_info={}, status_code=200):
    return {
        'data': data,
        'status': status_code,
    }
