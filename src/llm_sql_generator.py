from src.hf_nusantara_llm import infer
from database.db_connection import engine
from sqlalchemy import text
import re

def clean_sql(sql_text: str) -> str:
    return re.sub(r"```sql|```", "", sql_text).strip()

def generate_sql_query_from_question(question: str) -> str:
    prompt = f"""
Ubah pertanyaan berikut menjadi query SQL valid untuk PostgreSQL:

Tabel `articles`: id, regulation_id, chapter_number, chapter_about, article_number (text), text  
Tabel `regulations`: id, title, number, year

Relasi:
articles.regulation_id = regulations.id

Berikan hanya SQL-nya. Pastikan nilai string dibungkus dengan tanda kutip tunggal ('...').

Pertanyaan: {question}
SQL:
"""
    raw_sql = infer(prompt)
    return clean_sql(raw_sql)

def generate_sql_and_result(question: str) -> str:
    sql = generate_sql_query_from_question(question)
    print("💡 SQL yang dihasilkan:\n", sql)

    with engine.connect() as conn:
        result = conn.execute(text(sql))
        rows = result.fetchall()
        columns = result.keys()

    table_text = "\n".join([", ".join(columns)] + [", ".join(str(c) for c in row) for row in rows])
    return table_text
