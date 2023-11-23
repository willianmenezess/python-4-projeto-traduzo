from src.models.history_model import HistoryModel
from src.models.user_model import UserModel
import json


def test_history_delete(app_test):
    # ja foi feita uma fixture para criar um historico de
    # traducao com dois registros e agora cria-se um usuario
    # admin para poder deletar um registro de historico

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

    app_test.delete(
        f"/admin/history/{history_id}",
        headers={
            "Authorization": "token",
            "User": "admin",
        },
    )
    assert len(json.loads(HistoryModel.list_as_json())) == 1
