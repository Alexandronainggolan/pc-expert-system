from config.db import get_connection

def save_build(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO builds (cpu_id, gpu_id, ram_id, storage_id, psu_id, total_price, kategori)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """

    cursor.execute(query, (
        data["cpu_id"],
        data["gpu_id"],
        data["ram_id"],
        data["storage_id"],
        data["psu_id"],
        data["total_price"],
        data["kategori"]
    ))

    conn.commit()
    build_id = cursor.lastrowid
    conn.close()

    return build_id


def save_analysis(build_id, facts):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO build_analysis (build_id, bottleneck, performa_awal, performa_akhir)
    VALUES (%s,%s,%s,%s)
    """, (
        build_id,
        facts.get("bottleneck"),
        facts.get("performa_awal"),
        facts.get("performa_akhir")
    ))

    for log in facts["log"]:
        cursor.execute("""
        INSERT INTO rule_logs (build_id, rule_applied)
        VALUES (%s,%s)
        """, (build_id, log))

    conn.commit()
    conn.close()