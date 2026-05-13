from models.component_model import get_upgrade_options

def calculate_kategori(facts):
    score = (
        facts["cpu_score"] +
        facts["gpu_score"] +
        facts["ram_score"] +
        facts["storage_score"]
    ) / 4

    if facts.get("bottleneck"):
        score -= 1

    if facts["ram_score"] <= 3:
        score -= 1

    if not facts["compatible"]:
        score -= 2  # 🔥 penalti besar kalau tidak kompatibel

    if score <= 4:
        return "low"
    elif score <= 7:
        return "medium"
    else:
        return "high"


def generate_kesimpulan(facts):
    if not facts["compatible"]:
        return "Build tidak kompatibel"

    if facts.get("bottleneck") == "cpu":
        return "Performa dibatasi CPU"
    elif facts.get("bottleneck") == "gpu":
        return "Performa dibatasi GPU"
    else:
        return "Performa seimbang"


# 🔥 rekomendasi spesifik
def generate_recommendation(facts):
    rekomendasi = []

    if facts.get("bottleneck") == "cpu":
        options = get_upgrade_options("cpu", facts["cpu_score"])
        for o in options:
            rekomendasi.append(f"Upgrade CPU ke {o['name']}")

    if facts.get("bottleneck") == "gpu":
        options = get_upgrade_options("gpu", facts["gpu_score"])
        for o in options:
            rekomendasi.append(f"Upgrade GPU ke {o['name']}")

    if facts["ram_score"] <= 3:
        options = get_upgrade_options("ram", facts["ram_score"])
        for o in options:
            rekomendasi.append(f"Upgrade RAM ke {o['name']}")

    if not facts["compatible"]:
        rekomendasi.append("Perbaiki kompatibilitas komponen terlebih dahulu")

    if not rekomendasi:
        rekomendasi.append("Spesifikasi sudah optimal")

    return rekomendasi