import sys, re, datetime, pathlib, textwrap

USAGE = """
Usage:
  python tools/new_problem.py <platform> "<title>" <url>

Examples:
  python tools/new_problem.py leetcode "Two Sum" https://leetcode.com/problems/two-sum/
  python tools/new_problem.py codewars "Reverse String" https://www.codewars.com/kata/5168bb5dfe9a00b126000018
"""

PLATFORMS = {"leetcode", "codewars", "hackerrank"}

def slugify(title: str) -> str:
    s = title.lower().strip()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s

def header(platform: str, title: str, url: str) -> str:
    today = datetime.date.today().isoformat()
    return textwrap.dedent(f"""\
    # {today}
    # Platform: {platform.capitalize()}
    # Problem: {title}
    # Link: {url}
    # Approach: (write 1–2 lines here)
    """)

def main():
    if len(sys.argv) < 4:
        print(USAGE); sys.exit(1)

    platform = sys.argv[1].lower()
    title = sys.argv[2]
    url = sys.argv[3]

    if platform not in PLATFORMS:
        print(f"Platform must be one of: {', '.join(sorted(PLATFORMS))}")
        sys.exit(1)

    date = datetime.date.today().isoformat()
    fname = f"{date}_{slugify(title)}.py"
    outdir = pathlib.Path(platform)
    outdir.mkdir(exist_ok=True)
    outpath = outdir / fname

    if outpath.exists():
        print(f"File already exists: {outpath}"); sys.exit(1)

    content = header(platform, title, url) + "\n\nclass Solution:\n    pass\n"
    outpath.write_text(content, encoding="utf-8")
    print(f"Created: {outpath}")

if __name__ == "__main__":
    main()
