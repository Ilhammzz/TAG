from sqlalchemy import create_engine

# Ganti dengan info dari ngrok
DB_URI = "postgresql+psycopg2://postgres:admin@0.tcp.ap.ngrok.io:11245/db_regulation"

engine = create_engine(DB_URI)
