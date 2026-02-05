import pytest
import os

from flask import Flask, request
from main import main

@pytest.fixture
def client() -> Flask.test_client:
    """
    Cria um cliente HTTP de teste que executa exatamente a Cloud Function real, em memória, de forma rápida e isolada.

    Retorna: Flask.test_client: Cliente HTTP de teste para a aplicação Flask.
    """
    app = Flask(__name__)
    def flask_entrypoint(**_):
        return main(request)
    app.add_url_rule("/api/<string:resource>", view_func=flask_entrypoint, methods=["GET"])
    return app.test_client()