#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("/Users/admin/satellite-ngono")
HEAD = (ROOT / "partials/head.html").read_text(encoding="utf-8")

for path in ROOT.glob("*.html"):
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"<html\s+lang=\"[^\"]*\"", '<html lang="fr"', text, count=1)
    # Replace entire head content between <head> and </head> keeping title and gtag
    title_m = re.search(r"<title>.*?</title>", text, re.DOTALL)
    gtag_m = re.search(r"<!-- Google tag.*?gtag.*?</script>\s*", text, re.DOTALL)
    title = title_m.group(0) if title_m else ""
    gtag = gtag_m.group(0) if gtag_m else ""
    meta_desc = ""
    m = re.search(r'<meta content="" name="description">', text)
    if m:
        meta_desc = m.group(0)
    new_head = "<head>\n"
    if gtag:
        new_head += "    " + gtag.strip() + "\n"
    new_head += "    " + title + "\n"
    new_head += HEAD
    if meta_desc and "keywords" not in HEAD:
        new_head += '    <meta content="" name="keywords">\n    <meta content="" name="description">\n'
    new_head += "</head>"
    text = re.sub(r"<head>.*?</head>", new_head, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")
    print("cleaned", path.name)
