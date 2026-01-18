import os
from openai import OpenAI
from dotenv import load_dotenv
from manual_context import machine_manual  #KNowledge Base

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def read_latest_log(filepath):
    """Last Line == Most recentError"""
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip() #last line
            else:
                return None
    except FileNotFoundError:
        print("Log file not found.")
        return None

def diagnose_error(log_entry, manual_text):
    """LOG AND MANUAL TO GPT."""
    
    prompt = f"""
    You are an expert factory maintenance assistant. 
    
    I will give you a raw error log from a machine and a section of the technical manual.
    Your job is to:
    1. Identify the error in the log.
    2. Look up the error in the provided manual text.
    3. Output a clear, non-technical explanation for the operator.
    4. Provide a numbered list of actionable steps to fix it.

    ---
    TECHNICAL MANUAL CONTEXT:
    {manual_text}
    ---
    RAW LOG ENTRY:
    {log_entry}
    ---
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful industrial AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1, 
    )

    return response.choices[0].message.content

# main exec
if __name__ == "__main__":
    log_file = "machine_logs.txt.txt"
    
    print(f"Scanning {log_file}...")
    latest_log = read_latest_log(log_file)
    
    if latest_log:
        print(f"Found Error: {latest_log}")
        print("Analyzing with AI...")
        
        diagnosis = diagnose_error(latest_log, machine_manual)
        
        print("\n" + "="*40)
        print("DIAGNOSIS REPORT")
        print("="*40)
        print(diagnosis)
    else:
        print("No logs found.")