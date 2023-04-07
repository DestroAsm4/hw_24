from typing import Dict, List, Tuple, Union, List, Optional, Any, Iterable

from flask import Blueprint, Response, jsonify, request
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:



    data = request.json


    try:
        RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400


    first_result = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        data=None,
        file_name=data['file_name'],
    )
    result = build_query(
        cmd=data['cmd2'],
        value=data['value2'],
        data=first_result,
        file_name=data['file_name'],
    )
    return jsonify(list(result))