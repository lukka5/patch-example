from unittest.mock import patch

from patch_example.app import main


class TestApp:
    @patch("patch_example.app.make_request")
    def test_app_success(self, make_request_mock):
        make_request_mock.return_value = 200, "everythin ok"
        assert main() == "OK"

    @patch("patch_example.app.make_request")
    def test_app_failure(self, make_request_mock):
        make_request_mock.return_value = 400, "some error"
        assert main() == "FAIL"
