import os
import re
import time
import argparse
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    raise ValueError("Please set DEEPSEEK_API_KEY in your .env file.")

# Initialize DeepSeek Client
client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")

def separate_frontmatter(content):
    """
    Safely extracts Docusaurus YAML frontmatter.
    Returns: (frontmatter_string, body_string)
    """
    match = re.match(r'^(---\s*\n.*?\n---\s*\n)(.*)', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content

def clean_llm_output(text):
    """
    Removes the ```markdown ... ``` wrapper that LLMs sometimes add to their responses.
    """
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[11:] # Remove starting backticks and language identifier
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def rewrite_with_deepseek(text):
    """
    Sends the markdown text to DeepSeek with a highly specialized educational prompt.
    """
    system_prompt = """
    You are a highly empathetic Senior Software Engineer and Expert Technical Mentor. 
    Your goal is to rewrite the provided curriculum lesson to make it deeply engaging, elaborate, and human. 
    The original text sounds "robotic" and passive. You must transform it into an encouraging, mentor-like conversation.

    TONE & STYLE GUIDELINES:
    1. Be deeply empathetic. Acknowledge that learning these concepts is hard (e.g., "you are not alone", "this is tricky").
    2. Use real-world analogies to explain abstract or dense technical concepts.
    3. Speak directly to the reader using "you" and "we".
    4. Eliminate cliché AI filler phrases like "In conclusion", "Let's dive right in", "Delve into", or "Welcome to this lesson".

    STRUCTURAL RULES:
    1. PRESERVE ALL CODE BLOCKS exactly as they are written.
    2. PRESERVE ALL HTML / JSX tags. Do NOT alter or remove <iframe>, <div>, or style tags (these are for Docusaurus video rendering).
    3. PRESERVE the core structural headers (e.g., "Learning Objectives", "Next Steps", "Video").
    4. Do NOT output any conversational filler before or after the markdown (Do NOT say "Here is the rewritten lesson:").
    5. ONLY output raw, valid Markdown. 
    """

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Rewrite this lesson following the system guidelines:\n\n{text}"}
            ],
            temperature=0.65, # 0.65 balances technical accuracy with creative, empathetic analogies
        )
        return clean_llm_output(response.choices[0].message.content)
    except Exception as e:
        print(f"\n[ERROR] DeepSeek API failed: {e}")
        return None

def process_file(filepath, make_backup=True):
    """Reads, backs up, and rewrites a single markdown file."""
    print(f"⏳ Processing: {filepath}...", end="", flush=True)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    frontmatter, body = separate_frontmatter(original_content)
    
    if not body.strip():
        print(" [SKIPPED - Empty Body]")
        return

    improved_body = rewrite_with_deepseek(body)
    
    if improved_body:
        # Create a backup of the original file just in case
        if make_backup:
            backup_path = filepath + ".bak"
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)

        # Overwrite the original file with the new content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(frontmatter + improved_body + "\n")
        print(" [SUCCESS]")
    else:
        print(" [FAILED]")

def process_path(target_path, no_backup=False):
    """Routes a file or directory path to the processor."""
    if not os.path.exists(target_path):
        print(f"❌ Error: Path '{target_path}' does not exist.")
        return

    make_backup = not no_backup

    if os.path.isfile(target_path):
        if target_path.endswith('.md'):
            process_file(target_path, make_backup)
        else:
            print(f"⏭️ Skipped non-markdown file: {target_path}")
            
    elif os.path.isdir(target_path):
        print(f"📂 Scanning directory: {target_path}")
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith('.md'):
                    filepath = os.path.join(root, file)
                    process_file(filepath, make_backup)
                    time.sleep(2) # Respect API rate limits

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rewrite Docusaurus curriculum using DeepSeek API.")
    parser.add_argument(
        "path", 
        type=str, 
        help="Path to a specific .md file or a folder (e.g., 'curriculum/01-Foundations')"
    )
    parser.add_argument(
        "--no-backup", 
        action="store_true", 
        help="Disable automatic creation of .bak files for originals."
    )
    
    args = parser.parse_args()
    
    print("🤖 Initializing DeepSeek Curriculum Rewriter...")
    if not args.no_backup:
        print("🛡️ Backup mode is ON. Original files will be saved as .bak")
        
    confirm = input(f"Are you sure you want to process '{args.path}'? (y/n): ")
    
    if confirm.lower() == 'y':
        process_path(args.path, args.no_backup)
        print("\n✅ All done! Review your files, then run Docusaurus to see the changes.")
    else:
        print("Aborted.")