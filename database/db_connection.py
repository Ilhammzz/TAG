from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Ambil URI dari .env
DB_URI = os.getenv("DB_URI")

# Cek kalau belum diset
if DB_URI is None:
    raise ValueError("DB_URI tidak ditemukan di file .env")

# Buat SQLAlchemy engine
engine = create_engine(DB_URI)

# (Opsional) Buat session factory untuk ORM/eksekusi manual
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Coba test koneksi
def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'"))
            tables = result.fetchall()
            print("[✔] Database connected. Tables found:")
            for table in tables:
                print(" -", table[0])
    except Exception as e:
        print("[✘] Database connection failed:", e)
