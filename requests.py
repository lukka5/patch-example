def make_request(success=True):
    if not success:
        return 400, "Bad request"
    return 200, "Success"
