#!/usr/bin/env python3
"""Build a contact sheet (one static HTML page) from local images.

Use it two ways:
  * taste checkpoint: one row per direction, for the owner's eyes
  * comparison: direction / reference / our build in one row, at the same
    scale, then screenshot the page so the model judges ONE combined image

Standard library only. Write outputs to the session scratchpad, never the repo.

Spec (JSON):
{
  "title": "What we're deciding: ...",
  "note": "Look at: ...",              # optional
  "width": 220,                         # optional, px per image (same scale for all)
  "rows": [
    {"label": "A: Four places", "caption": "Fuller, more familiar.",
     "items": [{"img": "a1.webp", "name": "Apple Store", "url": "https://mobbin.com/screens/..."}]}
  ],
  "question": "Which feels most like us: A, B, C, or none?"   # optional
}

Usage: python3 sheet.py spec.json out.html
       python3 sheet.py --from-dir DIR out.html
Image paths are relative to the spec file. Raster images are embedded so the
HTML can be opened locally or served without file:// access.

--from-dir builds the spec from simulator captures named step-NN_<cfg>.png
(the sim-matrix.sh / flow-step.sh contract): one row per <cfg>, ordered by NN,
with the filename as the caption.
"""
import argparse
import base64
import html
import mimetypes
import re
from urllib.parse import urlparse
import json
from pathlib import Path

CAPTURE = re.compile(r'^step-(\d+)_(.+)\.png$')

CSS = """
:root{--bg:#f7f7f5;--ink:#141414;--ink2:#5f5f5f;--line:#e3e3df}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);
font:15px/1.45 -apple-system,system-ui,sans-serif}
main{max-width:1280px;margin:0 auto;padding:24px 16px 48px}
h1{font-size:20px;margin:0 0 6px}.note{color:var(--ink2);margin:0 0 16px}
section{border-top:1px solid var(--line);padding:18px 0}
h2{font-size:17px;margin:0}.cap{color:var(--ink2);margin:2px 0 12px}
.row{display:flex;gap:12px;overflow-x:auto;padding-bottom:6px}
figure{margin:0;flex:0 0 auto}figure img{display:block;border-radius:12px}
figcaption{font-size:12px;color:var(--ink2);margin-top:4px;max-width:var(--w)}
.q{margin-top:16px;font-weight:600}
"""


def build(spec: dict, base: Path) -> str:
    w = int(spec.get("width", 220))
    if w <= 0:
        raise ValueError("width must be positive")
    e = html.escape
    out = [f"<!doctype html><html lang=en><head><meta charset=utf-8>"
           f"<meta name=viewport content='width=device-width,initial-scale=1'>"
           f"<title>{e(spec.get('title', 'Contact sheet'))}</title><style>{CSS}</style></head>"
           f"<body><main style='--w:{w}px'><h1>{e(spec.get('title', ''))}</h1>"]
    if spec.get("note"):
        out.append(f"<p class=note>{e(spec['note'])}</p>")
    for row in spec["rows"]:
        out.append(f"<section><h2>{e(row.get('label', ''))}</h2>")
        if row.get("caption"):
            out.append(f"<p class=cap>{e(row['caption'])}</p>")
        out.append("<div class=row>")
        for it in row["items"]:
            img = (base / it["img"]).resolve(strict=True)
            mime = mimetypes.guess_type(img.name)[0]
            if mime not in {"image/png", "image/jpeg", "image/webp", "image/gif"}:
                raise ValueError(f"unsupported comparison image: {img.name}")
            src = f"data:{mime};base64," + base64.b64encode(img.read_bytes()).decode("ascii")
            if it.get("url") and urlparse(it["url"]).scheme not in {"https", "http"}:
                raise ValueError("reference URLs must use http or https")
            name = e(it.get("name", ""))
            cap = f"<a href='{e(it['url'])}'>{name}</a>" if it.get("url") else name
            if it.get("note"):
                cap += f": {e(it['note'])}"
            out.append(f"<figure><img src='{src}' width={w} alt='{name}'><figcaption>{cap}</figcaption></figure>")
        out.append("</div></section>")
    if spec.get("question"):
        out.append(f"<p class=q>{e(spec['question'])}</p>")
    out.append("</main></body></html>")
    return "".join(out)


def spec_from_dir(directory: Path) -> dict:
    """One row per capture configuration, from files named step-NN_<cfg>.png."""
    rows = {}
    for path in sorted(directory.iterdir()):
        match = CAPTURE.match(path.name)
        if match:
            rows.setdefault(match.group(2), []).append((int(match.group(1)), path.name))
    if not rows:
        raise ValueError(f"no step-NN_<cfg>.png captures in {directory}")
    return {
        "title": f"Captures: {directory.name}",
        "rows": [{"label": cfg,
                  "items": [{"img": name, "name": name} for _, name in sorted(steps)]}
                 for cfg, steps in sorted(rows.items())],
    }


def main(argv=None) -> None:
    parser = argparse.ArgumentParser(description="Build a contact sheet from a JSON spec or a capture dir.")
    parser.add_argument("spec", nargs="?", type=Path, help="spec JSON (omit with --from-dir)")
    parser.add_argument("out", type=Path, help="output HTML path")
    parser.add_argument("--from-dir", type=Path, help="directory of step-NN_<cfg>.png captures")
    args = parser.parse_args(argv)
    if bool(args.spec) == bool(args.from_dir):
        parser.error("give either spec.json or --from-dir DIR")
    if args.from_dir:
        base = args.from_dir
        spec = spec_from_dir(base)
    else:
        base = args.spec.parent
        spec = json.loads(args.spec.read_text())
    args.out.write_text(build(spec, base))
    print(args.out)


if __name__ == "__main__":
    main()
