from src.llm_sql_generator import generate_sql_and_result
from src.hf_nusantara_llm import infer  # ganti dari Gemini

def process_question(question: str) -> str:
    try:
        result_table = generate_sql_and_result(question)
        prompt = f"""
Pertanyaan: {question}

Berikut adalah hasil pencarian dari database:
{result_table}

Buatlah jawaban dalam bahasa Indonesia yang ringkas, jelas, dan kontekstual.
"""
        return infer(prompt)

    except Exception as e:
        return f"❌ Terjadi kesalahan: {e}"





# from database.db_connection import engine
# from src.query_generator import generate_sql
# from src.answer_generator import generate_answer
# from sqlalchemy import text
# from src.gemini_llm import GeminiLLM
# from src.llm_sql_generator import generate_sql_and_result

# llm = GeminiLLM()

# def process_question(question: str) -> str:
#     try:
#         table_result = generate_sql_and_result(question)

#         prompt = f"""
# Pertanyaan: {question}

# Hasil pencarian dari database hukum:
# {table_result}

# Buatlah jawaban hukum dalam bahasa Indonesia yang rapi, jelas, dan mudah dipahami.
# """
#         jawaban = llm(prompt)
#         return jawaban

#     except Exception as e:
#         return f"❌ Terjadi kesalahan: {e}"
# # def process_question(question):
# #     # Step 1: Generate SQL dari pertanyaan
# #     sql_query = generate_sql(question)
# #     if sql_query is None:
# #         return "Maaf, pertanyaan Anda tidak bisa diproses."

# #     # Step 2: Eksekusi SQL
# #     try:
# #         with engine.connect() as conn:
# #             result = conn.execute(text(sql_query))
# #             rows = result.fetchall()
# #             columns = result.keys()
# #             # Ubah ke dict
# #             data = [dict(zip(columns, row)) for row in rows]
# #     except Exception as e:
# #         return f"Terjadi kesalahan saat eksekusi query: {e}"

# #     # Step 3: Generate jawaban dari hasil query
# #     return generate_answer(question, data)


