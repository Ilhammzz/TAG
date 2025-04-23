from hf_evoreign_llm import infer
from database.db_connection import engine
from sqlalchemy import text
import re

def clean_sql(sql_text: str) -> str:
    """Hilangkan markdown dan whitespace berlebih"""
    return re.sub(r"```sql|```", "", sql_text).strip()

def generate_sql_query_from_question(question: str) -> str:
    """Buat prompt dan kirim ke LLM untuk mengubah pertanyaan menjadi query SQL"""
    prompt = f"""
Ubah pertanyaan berikut menjadi query SQL valid untuk PostgreSQL.

Struktur tabel:
Tabel `articles`: id, regulation_id, chapter_number, chapter_about, article_number (TEXT), text (TEXT)  
Tabel `regulations`: id, title (TEXT), number, year

Relasi:
articles.regulation_id = regulations.id

Pastikan nilai string dibungkus dengan tanda kutip tunggal ('...').
Berikan HANYA query-nya tanpa penjelasan apapun.

Pertanyaan: {question}
SQL:
"""
    raw_sql = infer(prompt)
    return clean_sql(raw_sql)

def generate_sql_and_result(question: str) -> str:
    """Ubah pertanyaan jadi SQL → Eksekusi ke PostgreSQL → Kembalikan hasil query sebagai teks tabel"""
    sql = generate_sql_query_from_question(question)
    print("🔎 SQL Generated:\n", sql)

    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql))
            rows = result.fetchall()
            columns = result.keys()

        if not rows:
            return "⚠️ Tidak ditemukan hasil dari query."

        # Format hasil ke string tabel
        table_text = "\n".join(
            [", ".join(columns)] + [", ".join(str(c) for c in row) for row in rows]
        )
        return table_text

    except Exception as e:
        return f"❌ Error saat eksekusi SQL:\n{e}"
