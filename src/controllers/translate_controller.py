from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator

translate_controller = Blueprint("translate_controller", __name__)


@translate_controller.route("/", methods=["GET"])
def get_translate():
    parameter = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?"
    }
    return render_template("index.html", param=parameter)


@translate_controller.route("/", methods=["POST"])
def translate_text():
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    translated = GoogleTranslator(
        source="auto", target=translate_to).translate(text_to_translate)
    parameter = {
        "languages": LanguageModel.list_dicts(),
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
        "translated": translated
    }
    return render_template("index.html", param=parameter)
