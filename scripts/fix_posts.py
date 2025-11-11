import json
from pathlib import Path
p = Path('blog/fixtures/posts.json')
if not p.exists():
    print('ERROR: file not found', p)
    raise SystemExit(1)
raw = p.read_bytes()
encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1']
text = None
for e in encodings:
    try:
        text = raw.decode(e)
        # basic sanity: must start with '[' or '{'
        if text.lstrip().startswith('[') or text.lstrip().startswith('{'):
            encoding_used = e
            break
    except Exception:
        continue
if text is None:
    print('ERROR: could not decode file with common encodings')
    raise SystemExit(2)
try:
    data = json.loads(text)
except Exception as exc:
    print('ERROR: JSON parse failed:', exc)
    raise
# rewrite as UTF-8 pretty JSON
p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
print('OK: parsed and rewrote', p, 'items=', len(data), 'decoded_with=', encoding_used)
