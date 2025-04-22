def generate_answer(question, data):
    if not data:
        return "Tidak ditemukan data yang relevan."

    output = ""
    for row in data:
        pasal = row.get("article_number", "")
        isi = row.get("text", "")
        judul = row.get("title", "")
        output += f"\n📜 {judul} - Pasal {pasal}\n{isi}\n"
    
    return output.strip()
