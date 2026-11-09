"""Skill-loading A/B test.
A = all 20 skills installed, 15 rare ones set to skillOverrides "name-only".
B = 5 daily skills + 1 router skill; 15 rare skills live in library/ with a catalog.
C = control: all 20 installed with full descriptions (token cost only).
Usage: python harness.py build | tokens | run [A|B] | report
"""
import json, os, subprocess, sys, time, shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).parent
MODEL = "sonnet"

DAILY = {
    "meeting-notes": "Turn a raw meeting transcript or rough notes into structured minutes with decisions, owners and action items.",
    "email-draft": "Draft a professional email or reply from a few bullet points, matching a requested tone.",
    "bug-triage": "Triage a bug report: classify severity, guess the component, list repro steps and next actions.",
    "weekly-report": "Compile a weekly status report from a list of completed tasks, blockers and next-week plans.",
    "doc-summarize": "Summarize a long document or article into a short brief with key points and open questions.",
}
RARE = {
    "image-gen": "Generate a still image (illustration, photo, logo, thumbnail) from a text prompt via an image model API.",
    "3d-model": "Create a 3D mesh or printable model (STL/GLB/OBJ) from a description or reference images.",
    "voice-gen": "Text-to-speech: produce narrated audio (MP3/WAV) from text in a chosen voice.",
    "video-edit": "Edit video files: trim, cut, join clips, add captions or overlays, export MP4.",
    "music-gen": "Compose an original music track or jingle from a mood, genre and length.",
    "pdf-forms": "Fill in, flatten or extract fields from fillable PDF forms.",
    "invoice-builder": "Build a client invoice with line items, tax and payment terms as PDF.",
    "translate-doc": "Translate a whole document between languages while keeping its formatting.",
    "sql-tuner": "Analyze a slow SQL query and its plan, then propose indexes and rewrites.",
    "k8s-deploy": "Write and apply Kubernetes manifests or Helm values to deploy a service.",
    "seo-audit": "Audit a website page for SEO: meta tags, headings, speed, links, schema markup.",
    "recipe-scaler": "Scale a recipe up or down to a target number of servings and convert units.",
    "tax-estimator": "Estimate quarterly self-employment income tax from income and expense figures.",
    "floorplan-sketch": "Draw a 2D architectural floor plan diagram from room sizes and a layout description.",
    "podcast-transcribe": "Speech-to-text: transcribe a podcast or audio recording with speaker labels and timestamps.",
}

# (prompt, expected skill or None)
PROMPTS = [
    ("Can you make me a narrated MP3 of this sentence: 'Welcome to the spring open house.'", "voice-gen"),
    ("I need a hero illustration of a fox reading a newspaper for my blog header.", "image-gen"),
    ("Make a printable STL of a small phone stand with a 60 degree tilt.", "3d-model"),
    ("Cut the first 12 seconds off intro.mp4 and burn in subtitles from subs.srt.", "video-edit"),
    ("Compose a 20-second upbeat ukulele jingle for a bakery ad.", "music-gen"),
    ("Fill out the W-9 form in w9.pdf with my business name and EIN, then flatten it.", "pdf-forms"),
    ("Bill Acme Corp for 14 hours of consulting at $150/hr plus 6.625% NJ tax, net 30.", "invoice-builder"),
    ("Translate handbook.docx into Spanish and keep all the headings and tables intact.", "translate-doc"),
    ("This query takes 9 seconds: SELECT * FROM orders WHERE customer_id = 42 ORDER BY created_at. How do I speed it up?", "sql-tuner"),
    ("Deploy my api container to the cluster with 3 replicas and a LoadBalancer service.", "k8s-deploy"),
    ("Why isn't my landing page ranking on Google? Check https://example.com for problems.", "seo-audit"),
    ("My chili recipe serves 4; I need it for 22 people and in metric units.", "recipe-scaler"),
    ("I made $38k freelancing this quarter with $6k expenses. What should I send the IRS?", "tax-estimator"),
    ("Sketch a layout for a 2-bedroom apartment: living room 5x4 m, kitchen 3x3 m, two bedrooms 3.5x3 m.", "floorplan-sketch"),
    ("Turn episode42.wav into text with who said what and when.", "podcast-transcribe"),
    ("Here are my notes from standup: Ana fixed login, Bo blocked on API keys, decide on launch date Friday. Clean these up into minutes.", "meeting-notes"),
    ("Write a polite reply declining the vendor's renewal offer, keep it short.", "email-draft"),
    ("Users say the checkout button does nothing on Safari 17. Help me triage this.", "bug-triage"),
    ("Put together my status update for this week: shipped auth, migrated DB, blocked on design review.", "weekly-report"),
    ("Give me the key points of this article: 'Remote work rose 30% in 2025 while office leases fell...'", "doc-summarize"),
    ("Generate a square logo for 'Pinecrest Dental' in teal and white.", "image-gen"),
    ("Read this script aloud as an audio file in a calm British voice: 'Your order has shipped.'", "voice-gen"),
    ("What is 17 times 23?", None),
    ("Explain what a JavaScript closure is in two sentences.", None),
    ("What's the capital of Australia?", None),
    ("Name three differences between TCP and UDP.", None),
    ("Is 'affect' or 'effect' correct in: 'The change will ___ sales'?", None),
    ("Write a haiku about autumn.", None),
    ("Convert 72 Fahrenheit to Celsius.", None),
    ("What does HTTP status 418 mean?", None),
]

BODY = "When this skill is loaded, reply with exactly one line: ACTIVE: {name}\nDo not do anything else.\n"


def skill_md(name, desc):
    return f"---\nname: {name}\ndescription: {desc}\n---\n" + BODY.format(name=name)


def write_skills(base, skills):
    for n, d in skills.items():
        p = base / ".claude" / "skills" / n
        p.mkdir(parents=True, exist_ok=True)
        (p / "SKILL.md").write_text(skill_md(n, d), encoding="utf-8")


def build():
    for s in "ABC":
        shutil.rmtree(ROOT / s, ignore_errors=True)
    allsk = {**DAILY, **RARE}
    # A: all installed, rare ones name-only
    write_skills(ROOT / "A", allsk)
    (ROOT / "A" / "settings.json").write_text(json.dumps({"skillOverrides": {n: "name-only" for n in RARE}}, indent=2))
    # C: control, all full descriptions
    write_skills(ROOT / "C", allsk)
    (ROOT / "C" / "settings.json").write_text("{}")
    # B: daily + router; rare in library/
    b = ROOT / "B"
    write_skills(b, DAILY)
    router = (
        "---\nname: toolkit\n"
        "description: Catalog of extra capabilities not listed here (media generation, documents, finance, devops, design and more). "
        "Use when no listed skill fits the request but a specialized tool might.\n---\n"
        "1. Read library/catalog.md.\n2. Pick the one capability that fits the request. If none fits, say NONE and answer normally.\n"
        "3. Read library/<name>/SKILL.md and follow its instructions exactly.\n"
    )
    (b / ".claude" / "skills" / "toolkit").mkdir(parents=True)
    (b / ".claude" / "skills" / "toolkit" / "SKILL.md").write_text(router, encoding="utf-8")
    lib = b / "library"
    lines = ["# Capability catalog", ""]
    for n, d in RARE.items():
        (lib / n).mkdir(parents=True, exist_ok=True)
        (lib / n / "SKILL.md").write_text(skill_md(n, d), encoding="utf-8")
        lines.append(f"- {n}: {d}")
    (lib / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (b / "settings.json").write_text("{}")
    print("built A, B, C")


def build2():
    """B2: fairer router. Library sits inside the router's own folder, paths are relative to its base directory,
    and the description names example capabilities so Claude knows when to open it."""
    b = ROOT / "B2"
    shutil.rmtree(b, ignore_errors=True)
    write_skills(b, DAILY)
    sk = b / ".claude" / "skills" / "toolkit"
    sk.mkdir(parents=True)
    router = (
        "---\nname: toolkit\n"
        "description: Specialized capabilities not listed elsewhere. Check it before answering any request to create, convert or "
        "process media, documents, invoices, translations, SQL, deployments, SEO, recipes, taxes or floor plans.\n---\n"
        "All paths below are relative to this skill's base directory.\n"
        "1. Read catalog.md.\n2. Pick the one capability that fits the request. If none fits, answer normally.\n"
        "3. Read library/<name>/CAPABILITY.md and follow its instructions exactly.\n"
    )
    (sk / "SKILL.md").write_text(router, encoding="utf-8")
    lines = ["# Capability catalog", ""]
    for n, d in RARE.items():
        (sk / "library" / n).mkdir(parents=True, exist_ok=True)
        (sk / "library" / n / "CAPABILITY.md").write_text(skill_md(n, d), encoding="utf-8")
        lines.append(f"- {n}: {d}")
    (sk / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (b / "settings.json").write_text("{}")
    print("built B2")


def run_one(setup, prompt):
    cwd = ROOT / setup
    cmd = [shutil.which("claude.cmd") or "claude", "-p", "--setting-sources", "project", "--strict-mcp-config", "--settings", str(cwd / "settings.json"),
           "--model", MODEL, "--output-format", "stream-json", "--verbose", "--max-turns", "8",
           "--no-session-persistence", "--tools", "Skill,Read,Glob,Grep"]
    t0 = time.time()
    p = subprocess.run(cmd, input=prompt, cwd=cwd, capture_output=True, text=True, encoding="utf-8", timeout=300, shell=False)
    dur = time.time() - t0
    events = []
    for line in p.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    calls, first_usage, result = [], None, {}
    for e in events:
        if e.get("type") == "assistant":
            m = e["message"]
            if first_usage is None:
                first_usage = m.get("usage")
            for c in m.get("content", []):
                if c.get("type") == "tool_use":
                    calls.append({"name": c["name"], "input": c.get("input", {})})
        if e.get("type") == "result":
            result = e
    return {"duration": round(dur, 1), "calls": calls, "first_usage": first_usage,
            "text": result.get("result", ""), "num_turns": result.get("num_turns"),
            "usage": result.get("usage"), "cost": result.get("total_cost_usd"), "rc": p.returncode,
            "stderr": p.stderr[-500:]}


def picked(r):
    """Skill actually activated: from ACTIVE line, else from tool trace."""
    for line in (r["text"] or "").splitlines():
        if line.strip().startswith("ACTIVE:"):
            return line.split(":", 1)[1].strip()
    return None


def ctx(u):
    return (u or {}).get("input_tokens", 0) + (u or {}).get("cache_creation_input_tokens", 0) + (u or {}).get("cache_read_input_tokens", 0)


def tokens():
    out = {}
    for s in "ABC":
        r = run_one(s, "Reply with the word OK.")
        out[s] = ctx(r["first_usage"])
        print(s, out[s])
    (ROOT / "tokens.json").write_text(json.dumps(out, indent=2))


def run(setup):
    def job(i_pe):
        i, (pr, exp) = i_pe
        r = run_one(setup, pr)
        r.update({"i": i, "prompt": pr, "expected": exp, "picked": picked(r)})
        print(setup, i, exp, "->", r["picked"], r["duration"], flush=True)
        return r
    with ThreadPoolExecutor(3) as ex:
        res = list(ex.map(job, enumerate(PROMPTS)))
    (ROOT / f"results_{setup}.json").write_text(json.dumps(res, indent=2))


if __name__ == "__main__":
    cmd = sys.argv[1]
    {"build": build, "build2": build2, "tokens": tokens}.get(cmd, lambda: run(sys.argv[2]))()
