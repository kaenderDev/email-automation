import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import Config

logger = logging.getLogger(__name__)


def _build_message(name: str, recipient: str) -> MIMEMultipart:
    """Builds the MIME e-mail message (plain-text + HTML)."""
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "✅ Submission Confirmed!"
    msg["From"] = Config.EMAIL_ADDRESS
    msg["To"] = recipient

    plain_body = (
        f"Hello, {name}!\n\n"
        "Thank you for reaching out. We have received your submission "
        "and will get back to you shortly.\n\n"
        "Best regards,\n"
        "The Support Team"
    )

    html_body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <style>
        body      {{ font-family: Arial, sans-serif; background: #f4f4f4; margin: 0; padding: 0; }}
        .card     {{ max-width: 520px; margin: 40px auto; background: #ffffff;
                     border-radius: 8px; overflow: hidden;
                     box-shadow: 0 2px 8px rgba(0,0,0,.12); }}
        .header   {{ background: #4f46e5; padding: 32px 40px; }}
        .header h1{{ color: #ffffff; margin: 0; font-size: 22px; }}
        .body     {{ padding: 32px 40px; color: #374151; line-height: 1.6; }}
        .body p   {{ margin: 0 0 16px; }}
        .badge    {{ display: inline-block; background: #ede9fe; color: #4f46e5;
                     border-radius: 4px; padding: 4px 12px; font-weight: bold;
                     font-size: 14px; margin-bottom: 20px; }}
        .footer   {{ background: #f9fafb; padding: 16px 40px;
                     font-size: 12px; color: #9ca3af; text-align: center; }}
      </style>
    </head>
    <body>
      <div class="card">
        <div class="header">
          <h1>Submission Confirmed ✅</h1>
        </div>
        <div class="body">
          <p>Hello, <strong>{name}</strong>!</p>
          <span class="badge">Received</span>
          <p>
            Thank you for reaching out. We have successfully received your
            submission and our team will get back to you shortly.
          </p>
          <p>If you have any questions in the meantime, just reply to this e-mail.</p>
          <p>Best regards,<br /><strong>The Support Team</strong></p>
        </div>
        <div class="footer">
          This is an automated message — please do not reply directly to this address.
        </div>
      </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(plain_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))
    return msg


def send_confirmation_email(name: str, recipient: str) -> None:
    """
    Connects to the configured SMTP server and sends a confirmation
    e-mail to *recipient*.

    Raises:
        smtplib.SMTPException: on any SMTP-level error.
        EnvironmentError: if EMAIL_ADDRESS or EMAIL_PASSWORD are unset.
    """
    Config.validate()

    msg = _build_message(name, recipient)

    logger.info(
        "Connecting to SMTP %s:%s as %s",
        Config.SMTP_HOST, Config.SMTP_PORT, Config.EMAIL_ADDRESS
    )

    with smtplib.SMTP(Config.SMTP_HOST, Config.SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.login(Config.EMAIL_ADDRESS, Config.EMAIL_PASSWORD)
        server.sendmail(Config.EMAIL_ADDRESS, recipient, msg.as_string())

    logger.info("E-mail delivered to %s", recipient)