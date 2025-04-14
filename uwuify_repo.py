#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path
try:
    import uwuify
except ImportError:
    os.system('pip install uwuify')
    import uwuify

def uwuify_markdown_file(file_path):
    """Uwuify the content of a markdown file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Preserve code blocks
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"CODE_BLOCK_{len(code_blocks) - 1}"
    
    # Save code blocks
    content_without_code = re.sub(r'```.*?```', save_code_block, content, flags=re.DOTALL)
    content_without_code = re.sub(r'`.*?`', save_code_block, content_without_code)
    
    # Uwuify the text
    uwuified_content = uwuify.uwuify(content_without_code)
    
    # Restore code blocks
    for i, block in enumerate(code_blocks):
        uwuified_content = uwuified_content.replace(f"CODE_BLOCK_{i}", block)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(uwuified_content)

def main():
    """Find and uwuify all markdown files in the repository."""
    # Get the repository root directory
    repo_root = os.getcwd()
    
    # Find all markdown files
    markdown_files = list(Path(repo_root).rglob('*.md'))
    
    print(f"Found {len(markdown_files)} markdown files")
    
    # Uwuify each markdown file
    for file_path in markdown_files:
        print(f"Uwuifying {file_path}")
        uwuify_markdown_file(file_path)
    
    print("All markdown files have been uwuified!")

if __name__ == "__main__":
    main()
