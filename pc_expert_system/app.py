from flask import Flask, render_template, request
from services.expert_system import run_expert_system
from models.component_model import get_components_by_type

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    selected_ids = None # Inisialisasi agar tidak error saat pertama buka halaman

    # =========================
    # Ambil data dropdown dari DB
    # =========================
    cpu_list = get_components_by_type("cpu")
    gpu_list = get_components_by_type("gpu")
    ram_list = get_components_by_type("ram")
    storage_list = get_components_by_type("storage")
    psu_list = get_components_by_type("psu")
    motherboard_list = get_components_by_type("motherboard")
    casing_list = get_components_by_type("casing")
    cooler_list = get_components_by_type("cooler")

    # =========================
    # Jika user submit form
    # =========================
    if request.method == "POST":
        try:
            # Ambil ID dari form dan simpan ke dictionary untuk dikirim balik ke template
            selected_ids = {
                "cpu_id": int(request.form.get("cpu")),
                "gpu_id": int(request.form.get("gpu")),
                "ram_id": int(request.form.get("ram")),
                "storage_id": int(request.form.get("storage")),
                "psu_id": int(request.form.get("psu")),
                "motherboard_id": int(request.form.get("motherboard")),
                "casing_id": int(request.form.get("casing")),
                "cooler_id": int(request.form.get("cooler"))
            }

            # Jalankan Inference Engine Forward Chaining
            result = run_expert_system(selected_ids)
            
        except (TypeError, ValueError):
            # Penanganan jika user menekan tombol analisis tapi ada pilihan yang kosong
            result = {
                "total_price": 0,
                "kategori": "-",
                "is_compatible": False,
                "analysis": ["⚠️ Mohon tentukan semua komponen terlebih dahulu untuk memulai analisis."]
            }

    return render_template(
        "index.html",
        result=result,
        selected_ids=selected_ids, # Mengirim balik pilihan user agar dropdown tidak reset
        cpu_list=cpu_list,
        gpu_list=gpu_list,
        ram_list=ram_list,
        storage_list=storage_list,
        psu_list=psu_list,
        motherboard_list=motherboard_list,
        casing_list=casing_list,
        cooler_list=cooler_list
    )

if __name__ == "__main__":
    app.run(debug=True)