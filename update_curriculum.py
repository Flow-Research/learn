import argparse
import os
import re
import time

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not API_KEY:
    raise ValueError("Please set DEEPSEEK_API_KEY in your .env file.")

client = OpenAI(api_key=API_KEY, base_url="https://api.deepseek.com")


def separate_frontmatter(content):
    """
    Safely extracts Docusaurus YAML frontmatter.
    Returns: (frontmatter_string, body_string)
    """
    match = re.match(r"^(---\s*\n.*?\n---\s*\n)(.*)", content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return "", content


def clean_llm_output(text):
    """
    Removes Markdown fences that LLMs sometimes add around the whole response.
    """
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[11:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()


def promote_video_section(body):
    """
    Keep any lesson video high on the page.

    If a lesson contains a "## Video" section, move it immediately after
    "## Learning Objectives". This is deterministic so the final layout does
    not depend entirely on the LLM following instructions.
    """
    video_match = re.search(
        r"(?ms)^## Video\s*\n.*?(?=^##\s+|\Z)",
        body,
    )
    if not video_match:
        return body

    video_section = video_match.group(0).strip()
    body_without_video = (
        body[: video_match.start()] + body[video_match.end() :]
    ).strip()

    if re.search(r"(?m)^## Watch First\s*$", body_without_video):
        return body_without_video

    video_section = re.sub(r"(?m)^## Video\s*$", "## Watch First", video_section)

    objectives_match = re.search(
        r"(?ms)^## Learning Objectives\s*\n.*?(?=^##\s+|\Z)",
        body_without_video,
    )
    if objectives_match:
        insert_at = objectives_match.end()
        return (
            body_without_video[:insert_at].rstrip()
            + "\n\n"
            + video_section
            + "\n\n"
            + body_without_video[insert_at:].lstrip()
        ).strip()

    return video_section + "\n\n" + body_without_video


def rewrite_with_deepseek(text):
    """
    Sends the Markdown text to DeepSeek with a launch-readiness prompt.
    """
    system_prompt = """
    You are a senior software engineer, ML educator, and technical curriculum editor for
    Flow Education Initiative. Rewrite the provided lesson so it is ready for launch.

    Audience:
    - Mid-level African software engineers growing into AI/ML, blockchain, and protocol engineering.

    Tone:
    - Engineering-first, clear, practical, warm, and concise.
    - Avoid hype, generic motivational filler, and robotic transitions.

    Content requirements:
    1. Preserve YAML frontmatter if present in the input body.
    2. Preserve all existing iframes, HTML, JSX, and code blocks unless a code block is broken.
    3. If a lesson has a video iframe or "## Video" section, place that video near the top,
       immediately after "## Learning Objectives", and rename the section to "## Watch First".
    4. Add a useful visual explanation where it helps. Prefer Docusaurus-friendly Mermaid code
       fences such as ```mermaid for flowcharts, concept maps, sequences, or lifecycle diagrams.
    5. Use math where it genuinely clarifies a concept. Prefer Docusaurus-friendly fenced
       math blocks such as ```math for display equations and inline $...$ sparingly.
    6. Include runnable, valid code snippets when the lesson teaches implementation.
    7. Keep lesson sections scannable: Learning Objectives, visual/video if available,
       concept explanation, worked example, exercises, self-assessment, further reading, next steps.
    8. Use official documentation links in Further Reading when relevant.
    9. Do not invent citations, paper titles, or video URLs.
    10. Output only raw, valid Markdown/MDX. Do not wrap the whole answer in fences.
    """.strip()

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": f"Rewrite this lesson following the system guidelines:\n\n{text}",
                },
            ],
            temperature=0.6,
        )
        rewritten = clean_llm_output(response.choices[0].message.content)
        return promote_video_section(rewritten)
    except Exception as e:
        print(f"\n[ERROR] DeepSeek API failed: {e}")
        return None


def process_file(filepath, make_backup=True):
    """Reads, backs up, and rewrites a single markdown file."""
    print(f"Processing: {filepath}...", end="", flush=True)

    with open(filepath, "r", encoding="utf-8") as f:
        original_content = f.read()

    frontmatter, body = separate_frontmatter(original_content)

    if not body.strip():
        print(" [SKIPPED - Empty Body]")
        return

    improved_body = rewrite_with_deepseek(body)

    if improved_body:
        if make_backup:
            backup_path = filepath + ".bak"
            with open(backup_path, "w", encoding="utf-8") as f:
                f.write(original_content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + improved_body + "\n")
        print(" [SUCCESS]")
    else:
        print(" [FAILED]")


def process_path(target_path, no_backup=False):
    """Routes a file or directory path to the processor."""
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        return

    make_backup = not no_backup

    if os.path.isfile(target_path):
        if target_path.endswith(".md"):
            process_file(target_path, make_backup)
        else:
            print(f"Skipped non-markdown file: {target_path}")

    elif os.path.isdir(target_path):
        print(f"Scanning directory: {target_path}")
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    process_file(filepath, make_backup)
                    time.sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rewrite Docusaurus curriculum lessons using DeepSeek."
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to a specific .md file or folder, e.g. curriculum/01-Foundations",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Disable automatic creation of .bak files for originals.",
    )

    args = parser.parse_args()

    print("Initializing DeepSeek curriculum rewriter...")
    if not args.no_backup:
        print("Backup mode is ON. Original files will be saved as .bak")

    confirm = input(f"Are you sure you want to process '{args.path}'? (y/n): ")

    if confirm.lower() == "y":
        process_path(args.path, args.no_backup)
        print("\nDone. Review the files, then run Docusaurus to verify rendering.")
    else:
        print("Aborted.")
