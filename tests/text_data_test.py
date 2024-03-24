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


@pytest.fixture
def text_data_instance():
    # Create an instance of TextData for testing
    text = "This is a test text."
    return TextData(text)


def test_get_word_list_with_simple_text(text_data_instance):
    # Test with a simple sentence
    expected_words = ["This", "is", "a", "test", "text"]
    assert text_data_instance.get_word_list() == expected_words


def test_get_word_list_with_complex_text(text_data_instance):
    # Test with a sentence containing punctuation and numbers
    text_data_instance.raw_data = (
        "Hello, world! This is a sample text with 123 numbers."
    )
    expected_words = [
        "Hello",
        "world",
        "This",
        "is",
        "a",
        "sample",
        "text",
        "with",
        "123",
        "numbers",
    ]
    assert text_data_instance.get_word_list() == expected_words


def test_get_word_list_with_empty_text():
    # Test with empty text
    text_data_instance = TextData("")
    assert text_data_instance.get_word_list() == []


def test_get_word_list_with_special_characters(text_data_instance):
    # Test with text containing special characters
    text_data_instance.raw_data = "Hello, world! How are you today? #@$"
    expected_words = ["Hello", "world", "How", "are", "you", "today"]
    assert text_data_instance.get_word_list() == expected_words


def test_get_word_list_with_multiline_text(text_data_instance):
    # Test with text containing newline characters
    text_data_instance.raw_data = "This is a\nmultiline\nsentence."
    expected_words = ["This", "is", "a", "multiline", "sentence"]
    assert text_data_instance.get_word_list() == expected_words


def test_get_unique_words_with_complex_text(text_data_instance):
    # Test with a sentence containing punctuation and numbers
    text_data_instance.raw_data = (
        "Hello, world! This is a sample text with 123 numbers."
    )
    expected_unique_words = [
        "Hello",
        "world",
        "This",
        "is",
        "a",
        "sample",
        "text",
        "with",
        "123",
        "numbers",
    ]
    assert set(text_data_instance.get_unique_words()) == set(expected_unique_words)


def test_get_unique_words_with_empty_text():
    # Test with empty text
    text_data_instance = TextData("")
    assert set(text_data_instance.get_unique_words()) == set()


def test_get_unique_words_with_special_characters(text_data_instance):
    # Test with text containing special characters
    text_data_instance.raw_data = "Hello, world! How are you today? #@$"
    expected_unique_words = ["Hello", "world", "How", "are", "you", "today"]
    assert set(text_data_instance.get_unique_words()) == set(expected_unique_words)


def test_get_unique_words_with_multiline_text(text_data_instance):
    # Test with text containing newline characters
    text_data_instance.raw_data = "This is a\nmultiline\nsentence."
    expected_unique_words = ["This", "is", "a", "multiline", "sentence"]
    assert set(text_data_instance.get_unique_words()) == set(expected_unique_words)
