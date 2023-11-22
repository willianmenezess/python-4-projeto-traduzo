from models.abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    # transforma o data em dicionário, pois vem da requisição em formato json
    def to_dict(self):
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"]
        }

    # usa o find do AbstractModel para retornar uma lista de dicionários
    # usa o to_dict para cada um dos itens da lista, para nao vir o _id
    @classmethod
    def list_dicts(cls):
        return [language.to_dict() for language in LanguageModel.find()]
