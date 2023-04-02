from typing Dict, List, Tuple, Union

from flask import Blueprint, Response, jsonify, request
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Union[Response, Tuple[Response, int]]:

    data: Dict[str, Union[List[dict], str]] = request.json

    try:
        validated_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    first_result = build_query(
        cmd=validated_data['cmdl'],
        value=validated_data['value'],
        data=None,
        file_name=validated_data['file_name'],
    )
    result = build_query(
        cmd=validated_data['cmd2'],
        value=validated_data['value2'],
        data=first_result,
    )