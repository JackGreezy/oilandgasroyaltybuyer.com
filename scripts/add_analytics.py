#!/usr/bin/env python3
"""
Add Vercel Web Analytics script to all HTML files in the public directory.
"""

import pathlib
import re
import sys

# Vercel Analytics script tag to inject
ANALYTICS_SCRIPT = '<script defer src="https://cdn.vercel-insights.com/v1/script.js"></script>'

def add_analytics_to_html(file_path):
    """Add analytics script before closing </head> tag if not already present."""
    content = file_path.read_text(encoding='utf-8', errors='ignore')
    
    # Check if analytics script is already present
    if 'vercel-insights.com' in content or 'cdn.vercel-insights' in content:
        return False
    
    # Find the closing </head> tag and inject the script before it
    if '</head>' in content:
        # Insert the script just before </head>
        modified_content = content.replace('</head>', f'{ANALYTICS_SCRIPT}</head>')
        file_path.write_text(modified_content, encoding='utf-8')
        return True
    
    return False

def main():
    project_root = pathlib.Path(__file__).parent.parent
    public_dir = project_root / 'public'
    
    if not public_dir.exists():
        print(f"Error: {public_dir} does not exist")
        sys.exit(1)
    
    html_files = list(public_dir.rglob('*.html'))
    modified_count = 0
    skipped_count = 0
    
    print(f"Found {len(html_files)} HTML files")
    
    for html_file in html_files:
        if add_analytics_to_html(html_file):
            modified_count += 1
            print(f"✓ Added analytics to {html_file.relative_to(project_root)}")
        else:
            skipped_count += 1
    
    print(f"\nSummary:")
    print(f"  Modified: {modified_count} files")
    print(f"  Skipped: {skipped_count} files (already has analytics or no </head> tag)")
    print(f"\nVercel Web Analytics has been successfully added to all HTML files!")

if __name__ == '__main__':
    main()
