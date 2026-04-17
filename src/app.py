import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructure import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(jackson_family.get_all_members()), 200


@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"msg": "Member not found"}), 404
    return jsonify(member), 200


@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()

    if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
        return jsonify({"msg": "Invalid data"}), 400

    new_member = jackson_family.add_member({
        "first_name": data["first_name"],
        "age": data["age"],
        "lucky_numbers": data["lucky_numbers"]
    })

    return jsonify(new_member), 200


@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    deleted = jackson_family.delete_member(member_id)

    if not deleted:
        return jsonify({"msg": "Member not found"}), 404

    return jsonify({"done": True}), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
