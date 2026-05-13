from config.db import get_connection


# =========================
# Ambil komponen berdasarkan ID
# =========================
def get_component_by_id(component_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM components WHERE id = %s", (component_id,))
    result = cursor.fetchone()

    conn.close()
    return result


# =========================
# Ambil komponen berdasarkan tipe (untuk dropdown)
# =========================
def get_components_by_type(component_type):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT * FROM components
        WHERE type = %s
    """

    cursor.execute(query, (component_type,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result
  
def get_upgrade_options(type, min_score):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM components 
        WHERE type = %s AND score > %s
        ORDER BY score ASC
        LIMIT 3
    """, (type, min_score))

    results = cursor.fetchall()
    conn.close()
    return results