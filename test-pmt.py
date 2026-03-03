import os
import time
import json
from datetime import datetime

# Configuration
LOG_FILE = "etl_history.json"

def run_etl():
    print(f"[{datetime.now()}] 🚀 ETL Process Started.")
    
    # 1. SIMULATE EXTRACT
    print(f"[{datetime.now()}] 📥 Extracting data from source...")
    time.sleep(2) # Simulate network delay
    raw_data = [
        {"item": "laptop", "price": 1200, "currency": "USD"},
        {"item": "mouse", "price": 25, "currency": "USD"},
        {"item": "monitor", "price": 300, "currency": "USD"}
    ]

    # 2. SIMULATE TRANSFORM
    print(f"[{datetime.now()}] ⚙️  Transforming data (applying tax)...")
    time.sleep(3) # Simulate processing time
    for record in raw_data:
        record["price_with_tax"] = record["price"] * 1.15  # 15% tax
        record["processed_at"] = str(datetime.now())

    # 3. SIMULATE LOAD
    print(f"[{datetime.now()}] 💾 Loading data into destination...")
    time.sleep(2)
    
    # Append results to a local file
    history = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            try:
                history = json.load(f)
            except:
                history = []

    history.append({
        "timestamp": str(datetime.now()),
        "status": "Success",
        "records_processed": len(raw_data)
    })

    with open(LOG_FILE, "w") as f:
        json.dump(history, f, indent=4)

    print(f"[{datetime.now()}] ✅ ETL Process Completed Successfully.\n")

if __name__ == "__main__":
    try:
        run_etl()
    except Exception as e:
        print(f"[{datetime.now()}] ❌ ETL Failed: {e}")
        exit(1) # Tell PM2 something went wrong