CREATE DATABASE IF NOT EXISTS pc_expert_system;
USE pc_expert_system;

-- Tabel Komponen Utama
CREATE TABLE IF NOT EXISTS components (
    id INT AUTO_INCREMENT PRIMARY KEY,
    type VARCHAR(50) NOT NULL, -- cpu, gpu, motherboard, ram, storage, psu, casing, cooler
    name VARCHAR(255) NOT NULL,
    price DECIMAL(15, 2) NOT NULL,
    socket VARCHAR(50),        -- Untuk CPU & Motherboard (LGA1700, AM5, dll)
    ram_type VARCHAR(50),     -- Untuk Motherboard & RAM (DDR4, DDR5)
    power_watt INT,           -- Untuk PSU (Total Watt) atau CPU/GPU (Consumption)
    vram VARCHAR(50),         -- Untuk GPU (8GB, 12GB, dll)
    spec VARCHAR(255),        -- Keterangan tambahan (DDR speed, Storage Gen, dll)
    score INT DEFAULT 0,      -- Untuk kalkulasi kategori (1-10)
    level VARCHAR(50)         -- low, medium, high
);

-- Tabel untuk menyimpan hasil build user
CREATE TABLE IF NOT EXISTS builds (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpu_id INT,
    gpu_id INT,
    ram_id INT,
    storage_id INT,
    psu_id INT,
    motherboard_id INT,
    casing_id INT,
    cooler_id INT,
    total_price DECIMAL(15, 2),
    kategori VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabel untuk log analisis sistem pakar
CREATE TABLE IF NOT EXISTS build_analysis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    build_id INT,
    bottleneck VARCHAR(100),
    performa_awal VARCHAR(100),
    performa_akhir VARCHAR(100),
    FOREIGN KEY (build_id) REFERENCES builds(id) ON DELETE CASCADE
);

-- Tabel untuk menyimpan log rule yang terpicu
CREATE TABLE IF NOT EXISTS rule_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    build_id INT,
    log_message TEXT,
    FOREIGN KEY (build_id) REFERENCES builds(id) ON DELETE CASCADE
);