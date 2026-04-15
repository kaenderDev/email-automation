import logging
from flask import Flask, request, jsonify
from email_service import send_confirmation_email
from config import Config

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)


def validate_payload(data: dict) -> tuple[bool, str]:
    """Validates the incoming JSON payload."""
    if not data:
        return False, "Request body must be valid JSON."

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()

    if not name:
        return False, "Field 'name' is required and cannot be empty."
    if not email:
        return False, "Field 'email' is required and cannot be empty."
    if "@" not in email or "." not in email.split("@")[-1]:
        return False, "Field 'email' must be a valid e-mail address."

    return True, ""


@app.route("/health", methods=["GET"])
def health_check():
    """Simple health-check endpoint."""
    return jsonify({"status": "ok"}), 200


@app.route("/submit", methods=["POST"])
def submit():
    """
    Receives a JSON payload with 'name' and 'email',
    validates it and sends a confirmation e-mail.
    """
    data = request.get_json(silent=True)
    logger.info("POST /submit — payload received: %s", data)

    is_valid, error_msg = validate_payload(data)
    if not is_valid:
        logger.warning("Validation error: %s", error_msg)
        return jsonify({"success": False, "error": error_msg}), 400

    name = data["name"].strip()
    email = data["email"].strip()

    try:
        send_confirmation_email(name, email)
        logger.info("Confirmation e-mail sent to %s <%s>", name, email)
        return jsonify({
            "success": True,
            "message": f"Confirmation e-mail successfully sent to {email}."
        }), 200

    except Exception as exc:
        logger.error("Failed to send e-mail to %s: %s", email, exc)
        return jsonify({
            "success": False,
            "error": "Could not send the confirmation e-mail. Please try again later."
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=Config.DEBUG)