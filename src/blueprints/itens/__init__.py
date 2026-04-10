from flask import Blueprint

bp = Blueprint("itens", __name__)

from . import routes 