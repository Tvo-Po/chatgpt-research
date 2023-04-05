import argparse
from pathlib import Path
import re
import sys


def format_markdown_for_github(md_path: Path):
    with open(md_path, 'r') as md_file:
        md = md_file.read()
        md = md.replace('<li><p>', '<li>') \
               .replace('</p></li>', '</li>') \
               .replace('**User:**', '**Me:**') \
               .replace('</li>\n```', '</li><br/>\n\n```')
        md = re.sub(r'```(.+)\n.+\nCopy code\n', r'```\g<1>\n', md)
    with open(md_path, 'w') as md_file:
        md_file.write(md)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='github formatter for AIRPM ChatGPT exported markdown'
    )
    parser.add_argument(
        '-p',
        dest='path',
        required=True,
        type=Path,
        help='path to markdown'
    )
    args = parser.parse_args()
    if not args.path.exists():
        print('[!] File not exist.')
        sys.exit(1)
    if not args.path.is_file():
        print('[!] Given path must lead to file. ')
        sys.exit(1)
    format_markdown_for_github(args.path)
    print('[+] Markdown has been successfully formatted.')
