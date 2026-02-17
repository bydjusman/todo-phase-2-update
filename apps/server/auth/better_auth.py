from better_auth import BetterAuth
from better_auth.plugins import EmailPassword
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Better Auth
auth = BetterAuth(
    secret=os.getenv("BETTER_AUTH_SECRET", "super-secret-jwt-key-for-local-development-min-32-chars"),
    plugins=[
        EmailPassword(),
    ],
    database_url=os.getenv("DATABASE_URL", "sqlite:///./todo_app.db"),
)
