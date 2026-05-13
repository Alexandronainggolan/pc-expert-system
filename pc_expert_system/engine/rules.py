def apply_rules(facts):

    # =========================
    # DEFAULT
    # =========================
    facts["compatible"] = True

    # =========================
    # BOTTLENECK CHECK
    # =========================
    if facts["cpu_score"] < facts["gpu_score"]:
        facts["bottleneck"] = "cpu"
        facts["log"].append("CPU bottleneck")

    elif facts["gpu_score"] < facts["cpu_score"]:
        facts["bottleneck"] = "gpu"
        facts["log"].append("GPU bottleneck")

    else:
        facts["bottleneck"] = "balanced"

    # =========================
    # RAM CHECK
    # =========================
    if facts["ram_score"] <= 3:
        facts["performa_awal"] = "rendah"
        facts["log"].append("RAM rendah")

    # =========================
    # CPU vs MOTHERBOARD
    # =========================
    if (
        facts["cpu_socket"] and
        facts["motherboard_socket"] and
        facts["cpu_socket"] != facts["motherboard_socket"]
    ):
        facts["compatible"] = False
        facts["log"].append(
            "CPU tidak kompatibel dengan motherboard"
        )

    # =========================
    # RAM vs MOTHERBOARD
    # =========================
    if (
        facts["ram_type"] and
        facts["motherboard_ram_type"] and
        facts["ram_type"] != facts["motherboard_ram_type"]
    ):
        facts["compatible"] = False
        facts["log"].append(
            "RAM tidak kompatibel dengan motherboard"
        )

    # =========================
    # PSU CHECK
    # =========================
    total_power = (
        facts["cpu_power"] +
        facts["gpu_power"]
    )

    if facts["psu_power"] < total_power:
        facts["compatible"] = False
        facts["log"].append(
            "PSU tidak cukup"
        )

    return facts