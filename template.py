import os

# Folder & file structure to create INSIDE the current folder
structure = {
    "docker-compose.yml": "",
    "requirements.txt": "",
    "README.md": "",
    "app": {
        "main.py": "",
        "config.py": "",
        "db.py": "",
        "models.py": "",
        "schemas.py": "",
        "routers": {
            "sensors.py": "",
            "telemetry.py": "",
            "incidents.py": "",
            "rca.py": "",
        },
        "ml": {
            "train_forecast.py": "",
            "anomaly_detection.py": "",
            "rca_rag.py": "",
            "embeddings_store.py": "",
        },
        "ingest": {
            "ingest_open_meteo.py": "",
        }
    }
}

def create_structure(base_path, items):
    """Recursively create folders and files inside current directory."""
    for name, content in items.items():
        path = os.path.join(base_path, name)

        # If content is dict → create folder
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            # Create empty file
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


if __name__ == "__main__":
    current_dir = os.getcwd()   # ← yahi energy-guard-backend folder hai
    create_structure(current_dir, structure)
    print("📁 Project structure created successfully inside this folder!")
