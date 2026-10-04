"""_site/index.html を生成する。CI上では GITHUB_SHA が入る。"""
import os
from datetime import datetime, timezone
from pathlib import Path

from app.calc import fizzbuzz

sha = os.environ.get("GITHUB_SHA", "local")[:7]
built_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
items = "".join(f"<li>{fizzbuzz(i)}</li>" for i in range(1, 16))

out = Path("_site")
out.mkdir(exist_ok=True)
(out / "index.html").write_text(
    f"""<!doctype html>
<meta charset="utf-8">
<title>cicd-lab</title>
<h1>cicd-lab</h1>
<p>commit: <code>{sha}</code> / built: {built_at}</p>
<ol>{items}</ol>
""",
    encoding="utf-8",
)
print(f"built _site/index.html (commit {sha})")
