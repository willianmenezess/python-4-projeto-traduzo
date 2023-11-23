from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
import json


def test_history_delete(app_test):
    # ja foi feita uma fixture para criar um usuario admin
    # e outra para criar um historico de traducao, mas
    # estão sendo sobrescritas por outra fixture
    # de um nivel acima que dropa o banco, então é necessário recriar
    HistoryModel({
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }).save()

    HistoryModel({
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        }).save()

    UserModel({
            "name": "admin",
            "password": "admin",
            "token": "token",
        }).save()

    assert len(json.loads(HistoryModel.list_as_json())) == 2

    # captura o id do primeiro historico de traducao
    history = HistoryModel.list_as_json()
    history_json = json.loads(history)
    history_id = history_json[0]["_id"]
    print(f"\n {history_json}")
    print(history_id)

    app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": "token",
            "User": "admin",
        },
    )
    assert len(json.loads(HistoryModel.list_as_json())) == 1
