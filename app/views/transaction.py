"""Module with transaction endpoints."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app import schemas
from app.utils.constants import PING_RESPONSE
from app.utils.decorators import error_decorator

transaction_view = Blueprint("transaction", __name__)


@transaction_view.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""

    return jsonify(PING_RESPONSE), HTTPStatus.OK


@transaction_view.route("/", methods=["GET"])
@error_decorator
def get_transaction_by_params():
    """Get transaction by query params."""

    params = schemas.SearchTransaction().load(request.args)
    res = app.transaction_controller.search_transactions(params)

    return jsonify(res), HTTPStatus.OK


@transaction_view.route("/user", methods=["GET"])
@error_decorator
def get_transactions_by_user():
    """Get transactions by user."""

    params = schemas.SearchUser().load(request.args)
    res = app.transaction_controller.search_transactions_by_user(params)

    return jsonify(res), HTTPStatus.OK


@transaction_view.route("/", methods=["POST"])
@error_decorator
def create_transaction():
    """Create transaction."""

    transaction = schemas.CreateTransaction().load(request.json)
    res = app.transaction_controller.create_transaction(transaction)

    return jsonify(res), HTTPStatus.CREATED
