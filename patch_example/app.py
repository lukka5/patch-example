from patch_example.requests import make_request


def main():
    status_code, response = make_request()
    if status_code == 200:
        return "OK"
    return "FAIL"


if __name__ == "__main__":
    main()
