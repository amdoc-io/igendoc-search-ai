from flask import jsonify, Blueprint, request

generate_ai_response_api_blueprint = Blueprint(
    "generate_ai_response_api_blueprint", __name__
)


@generate_ai_response_api_blueprint.route("/generate-ai-response", methods=["POST"])
def generate_ai_response():
    body = request.get_json()
    doc_bot_id = body["doc_bot_id"]
    # session_id is for entity relationship which we target in the future
    # session_id = body["session_id"]
    prompt = body["prompt"]
    # Use doc_bot_id to query for the LLM model
    # Your code here
    data = {"doc_bot_id": doc_bot_id, "prompt": prompt, "session_id": session_id}
    return jsonify(data), 200
