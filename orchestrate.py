import subprocess
import time
import sys
from datetime import datetime

# CONFIGURATION
# List your scripts in order
PIPELINE = ["extract.py", "transform.py", "load.py"]
MAX_RETRIES = 3
RETRY_DELAY = 10  # seconds to wait between retries

def run_script(script_path):
    """Runs a single script with retry logic."""
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"[{datetime.now()}] 🚀 Running {script_path} (Attempt {attempt}/{MAX_RETRIES})")
        
        try:
            # subprocess.run waits for the script to finish
            # we use sys.executable to ensure we use the same python/venv
            result = subprocess.run([sys.executable, script_path], check=True)
            print(f"[{datetime.now()}] ✅ {script_path} succeeded.")
            return True  # Move to next script
            
        except subprocess.CalledProcessError:
            print(f"[{datetime.now()}] ⚠️  {script_path} failed.")
            if attempt < MAX_RETRIES:
                print(f"[{datetime.now()}] 😴 Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"[{datetime.now()}] ❌ {script_path} failed after {MAX_RETRIES} attempts.")
                return False

def main():
    start_time = time.time()
    print(f"\n--- Pipeline Started at {datetime.now()} ---")
    
    for script in PIPELINE:
        success = run_script(script)
        if not success:
            print(f"--- Pipeline ABORTED at {script} ---\n")
            sys.exit(1) # Tell PM2 the run failed
            
    total_time = (time.time() - start_time) / 60
    print(f"--- Pipeline COMPLETED Successfully in {total_time:.2f} mins ---\n")

if __name__ == "__main__":
    main()