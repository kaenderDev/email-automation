import os
from dotenv import load_dotenv
 
load_dotenv()
 
 
class Config:
    # Flask
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-in-production")
 
    # SMTP
    EMAIL_ADDRESS: str = os.getenv("EMAIL_ADDRESS", "")
    EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD", "")
    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
 
    @classmethod
    def validate(cls) -> None:
        """Raises an error on startup if critical env vars are missing."""
        missing = [
            var for var, val in {
                "EMAIL_ADDRESS": cls.EMAIL_ADDRESS,
                "EMAIL_PASSWORD": cls.EMAIL_PASSWORD,
            }.items() if not val
        ]
        if missing:
            raise EnvironmentError(
                f"Missing required environment variable(s): {', '.join(missing)}"
            )
 