from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from wordavl.text_data import TextData


@pytest.fixture
def mocked_requests_get():
    mocked_response = MagicMock()
    mocked_response.text = "Mocked response text"
    mocked_response.raise_for_status.return_value = None
    with patch("requests.get") as mocked_get:
        mocked_get.return_value = mocked_response
        yield mocked_get


def test_read_from_link(mocked_requests_get):
    url = "https://example.com"
    text_data = TextData(url)
    assert text_data.raw_data == "Mocked response text"
    mocked_requests_get.assert_called_once_with(url)


def test_read_local_file(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("Test file content")
    text_data = TextData(str(file_path))
    assert text_data.raw_data == "Test file content"


def test_init_with_invalid_source():
    with pytest.raises(FileNotFoundError):
        TextData("invalid_source")
