def generate_sql(question):
    q = question.lower()

    # Contoh 1: Pasal 26 dari UU ITE
    if "pasal 26" in q and "uu ite" in q:
        return """
        SELECT a.article_number, a.text, r.title
        FROM articles a
        JOIN regulations r ON a.regulation_id = r.id
        WHERE a.article_number = '26' AND r.title ILIKE '%informasi dan transaksi elektronik%';
        """

    # Contoh 2: Semua pasal dari UU tertentu (misal UU Perlindungan Data Pribadi)
    if "pasal dalam uu perlindungan data pribadi" in q:
        return """
        SELECT a.article_number, a.text
        FROM articles a
        JOIN regulations r ON a.regulation_id = r.id
        WHERE r.title ILIKE '%perlindungan data pribadi%';
        """

    # Contoh 3: Nama semua peraturan tentang keamanan siber
    if "peraturan tentang keamanan siber" in q:
        return """
        SELECT title, year
        FROM regulations
        WHERE title ILIKE '%keamanan siber%';
        """

    return None
