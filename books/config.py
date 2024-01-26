import os
from dotenv import load_dotenv

# Load envs for connecting to Postgres DB
load_dotenv("./database.env")
# DB_USER = os.getenv("DB_USER")
# PASSWORD = os.getenv("PASSWORD")
# HOST = os.getenv("HOST")
# DATABASE = os.getenv("DATABASE")
# PORT = os.getenv("PORT")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "this-is-very-secure"
    # SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
