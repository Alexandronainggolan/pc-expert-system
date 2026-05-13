from models.component_model import get_component_by_id

def build_facts(input_ids):
    cpu = get_component_by_id(input_ids["cpu_id"])
    gpu = get_component_by_id(input_ids["gpu_id"])
    ram = get_component_by_id(input_ids["ram_id"])
    storage = get_component_by_id(input_ids["storage_id"])
    psu = get_component_by_id(input_ids["psu_id"])
    motherboard = get_component_by_id(input_ids["motherboard_id"])

    facts = {
        # level
        "cpu_level": cpu["level"],
        "gpu_level": gpu["level"],
        "ram_level": ram["level"],
        "storage_level": storage["level"],
        "psu_level": psu["level"],

        # score
        "cpu_score": cpu["score"],
        "gpu_score": gpu["score"],
        "ram_score": ram["score"],
        "storage_score": storage["score"],

        # 🔥 compatibility attributes
        "cpu_socket": cpu.get("socket"),
        "motherboard_socket": motherboard.get("socket"),

        "ram_type": ram.get("ram_type"),
        "motherboard_ram_type": motherboard.get("ram_type"),

        "cpu_power": cpu.get("power_watt", 0),
        "gpu_power": gpu.get("power_watt", 150),
        "psu_power": psu.get("power_watt", 0),

        # status
        "compatible": True,

        # log
        "log": []
    }

    return facts