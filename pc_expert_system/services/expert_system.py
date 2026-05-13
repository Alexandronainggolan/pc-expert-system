# services/expert_system.py
from models.component_model import get_component_by_id

def run_expert_system(input_ids):
    # --- STAGE 1: GATHER FACTS (Mengumpulkan Fakta) ---
    facts = {}
    total_price = 0
    total_score = 0
    
    for key, c_id in input_ids.items():
        comp = get_component_by_id(c_id)
        facts[key.replace("_id", "")] = comp
        total_price += float(comp['price'])
        total_score += comp['score']

    # --- STAGE 2: INFERENCE ENGINE (Aturan Forward Chaining) ---
    conclusions = []
    is_compatible = True

    # Rule 1: Validasi Konektivitas Fisik (Soket)
    if facts['cpu']['socket'] != facts['motherboard']['socket']:
        is_compatible = False
        conclusions.append(f"❌ Soket Tidak Cocok: {facts['cpu']['name']} butuh {facts['cpu']['socket']}.")

    # Rule 2: Validasi Teknologi Memori
    if facts['motherboard']['ram_type'] != facts['ram']['form_factor']:
        is_compatible = False
        conclusions.append(f"❌ Tipe RAM Tidak Sesuai: Motherboard mendukung {facts['motherboard']['ram_type']}.")

    # Rule 3: Analisis Kapasitas Daya
    # Mengasumsikan TDP CPU + GPU sebagai beban utama
    watt_demand = facts['cpu']['power_watt'] + facts['gpu']['power_watt']
    if facts['psu']['power_watt'] < (watt_demand * 1.2):
        is_compatible = False
        conclusions.append("⚠️ Kapasitas PSU terlalu mepet untuk beban CPU & GPU.")

    # Rule 4: Penentuan Kategori (Berdasarkan Fakta Harga & Skor)
    if total_price >= 15000000:
        kategori = "High-Tier Performance"
    elif total_price >= 8000000:
        kategori = "Mid-Tier Balance"
    else:
        kategori = "Entry-Tier Value"

    # --- STAGE 3: FINAL CONCLUSION ---
    if is_compatible and not conclusions:
        conclusions.append("✅ Konfigurasi Optimal: Semua komponen bekerja secara harmonis.")

    return {
        "total_price": total_price,
        "kategori": kategori,
        "is_compatible": is_compatible,
        "analysis": conclusions,
        "facts": facts
    }