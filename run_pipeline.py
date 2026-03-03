import subprocess
import time
import sys
from datetime import datetime
#import win32com.Client as win32
# CONFIGURATION
PIPELINE = ["test-pmt.py", "test-pmt2.py", "test-pmt3.py"]
MAX_RETRIES = 3
RETRY_DELAY = 10 


TO = ["samuel.nakupenda@gmail.com"]
'''
def send_email_oulook(to, subject, body, attachments=None):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = to
    mail.Subject = subject
    mail.HTMLBody = body

    if attachments:
        for file in attachments:
            mail.Attachments.Add(file)

    mail.Send()
    print("Email Sent Via Outlook")


'''
def run_script(script_path):
    """Runs a single script with retry logic."""
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"[{datetime.now()}] 🚀 Running {script_path} (Attempt {attempt}/{MAX_RETRIES})")
        
        try:
            # sys.executable ensures it uses the same python/venv as the orchestrator
            subprocess.run([sys.executable, script_path], check=True)
            print(f"[{datetime.now()}] ✅ {script_path} succeeded.")
            #send email
            #send_email_oulook(to=TO, subject=f"[{datetime.now()}] ✅ {script_path} succeeded.", body=f"[{datetime.now()}] ✅ {script_path} succeeded.")
            return True 
            
        except subprocess.CalledProcessError:
            print(f"[{datetime.now()}] ⚠️  {script_path} failed.")
            if attempt < MAX_RETRIES:
                print(f"[{datetime.now()}] 😴 Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"[{datetime.now()}] ❌ {script_path} failed after {MAX_RETRIES} attempts.")
                #send_email_oulook(to=TO, subject=f"❌ {script_path} FAILED.", body=f"[{datetime.now()}] ❌ {script_path} FAILED.")
                return False

def main():
    start_time = time.time()
    results = [] # To keep track of what happened
    
    print(f"\n--- Pipeline Started at {datetime.now()} ---")
    
    for script in PIPELINE:
        success = run_script(script)
        
        if success:
            results.append((script, "SUCCESS"))
        else:
            # We DON'T sys.exit(1) here anymore. 
            # We just record the failure and move to the next script.
            print(f"[{datetime.now()}] ⏭️  Moving to next script despite failure...")
            results.append((script, "FAILED"))
            
    # FINAL SUMMARY
    duration = (time.time() - start_time) / 60
    print(f"\n--- Pipeline Finished in {duration:.2f} mins ---")
    print("SUMMARY:")
    
    any_failures = False
    for script, status in results:
        icon = "✅" if status == "SUCCESS" else "❌"
        print(f" {icon} {script}: {status}")
        if status == "FAILED":
            any_failures = True

    # If ANY script failed, we exit with code 1 so PM2 shows "Errored" status.
    # This helps you see that something went wrong by looking at 'pm2 list'
    if any_failures:
        print("\nFinal Status: Completed with errors.\n")
        sys.exit(1)
    else:
        print("\nFinal Status: All scripts successful.\n")
        sys.exit(0)

if __name__ == "__main__":
    main()