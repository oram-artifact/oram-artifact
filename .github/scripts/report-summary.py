import os, sys

path = "report.log"
if not os.path.exists(path):
    print("## Proof check report\n")
    print("> :warning: `report.log` was not produced — the run did not reach "
          "completion. See the step logs above for the failure.")
    sys.exit(0)

raw = open(path).read()
try:
    import yaml
    data = yaml.safe_load(raw) or []
except Exception:
    data = None

print("## Proof check report\n")

if data is None:
    print("Could not parse `report.log`; raw contents below.\n")
else:
    tests = sum(int(e.get("tests", 0)) for e in data)
    failures = sum(int(e.get("failures", 0)) for e in data)
    if failures == 0:
        print(f"**:white_check_mark: All {tests} proof file(s) check.**\n")
    else:
        print(f"**:x: {failures} of {tests} proof file(s) failed.**\n")
    rows = []
    for e in data:
        for d in e.get("details", []):
            ok = ":white_check_mark:" if d.get("success") else ":x:"
            rows.append((ok, d.get("name", ""), d.get("time", "")))
    if rows:
        print("| Result | File | Time (s) |")
        print("|:------:|------|---------:|")
        for ok, name, t in rows:
            print(f"| {ok} | `{name}` | {t} |")
        print()

print("<details><summary>Raw <code>report.log</code></summary>\n")
print("```yaml")
print(raw.rstrip())
print("```")
print("</details>")
