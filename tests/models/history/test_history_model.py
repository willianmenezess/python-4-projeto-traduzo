import json
from src.models.history_model import HistoryModel


# Req. 8
def test_request_history():
    list_history_json = HistoryModel.list_as_json()
    assert isinstance(list_history_json, str)
    assert len(json.loads(list_history_json)) == 2
    assert json.loads(
        list_history_json)[0]["text_to_translate"] == "Hello, I like videogame"
