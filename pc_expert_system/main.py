from services.expert_system import run_expert_system

input_ids = {
    "cpu_id": 1,
    "gpu_id": 4,
    "ram_id": 7,
    "storage_id": 10,
    "psu_id": 13
}

result = run_expert_system(input_ids)

print("Kategori:", result["kategori"])
print("Harga:", result["total_price"])
print("Analisis:", result["analysis"])