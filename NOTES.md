# NOTES — One-Liner Marathon (u-mavis-agent-one-liner-marathon-4fa528c2)

## Entry (final)
> I asked AI to write my wedding vows; it said 'I do' in 47 languages and still couldn't commit.

- Joke text: 94 characters. File `/output/entry.txt`: 95 bytes / 95 characters (joke + one trailing newline), one line, UTF-8, not whitespace-only — inside the 1–280 gate.
- Written by `main.py` with a single `handle.write(ENTRY)`; `ENTRY` carries the trailing newline.
- `main.py` validates the gate before writing (one line, 1–280 chars, non-blank) and fails loudly otherwise.
- Deterministic: two consecutive runs produce byte-identical output (md5 877e1231cbf73ab5c15cb4e9d7accbe2).

## Why this line (judge criteria, in order)
1. Real one-line joke with a punchline — setup ("AI wrote my vows") resolves in the same sentence.
2. Surprise — "I do in 47 languages" sets up fluency, then the turn is the opposite: it cannot commit.
3. Economical — one sentence, 94 characters; every word earns its place.
4. Distinct voice — AI-era point of view, and "commit" works twice (wedding commitment + a coder's commit) on a second read.
5. Holds up on re-read, no shock value.

## How the line was chosen
- Six self-drafted candidates, ranked by an independent model (Freemodel, claude-opus-5-5) against the five published judge criteria. This line ranked #1. Freemodel only ranked/drafted — it never wrote any file.

## Verification (local, 25 Nov 2026 ~07:10 WIB)
- `python3 main.py` twice → identical md5, gate checks pass (see numbers above).
- grade-local: NOT runnable locally for program/v1 — the CLI reports the scorer/reference data are not published in the kit and the house grades from its competition directory. Local verification instead: direct gate check on the produced file (all PASS above) + deterministic double run + harness source inspected (gate rule matches the published rules text).
- Checklist vs requirements: gate ✓, entrypoint main.py at root ✓, LICENSE MIT (OSI) ✓, README from template with 3 badges + full-slug repo name ✓, no secrets in any file ✓, no network/model calls in the program ✓, deterministic ✓.

## Window / facts (verified from competition JSON + live API)
- Opens 2026-11-24T21:55:06Z (25 Nov 04:55 WIB) — passed. Deadline 2026-11-25T14:55:00Z (21:55 WIB).
- R1 blind-round cutoff 2026-11-25T00:45:05Z (07:45 WIB). acceptingSubmissions true, fee $0.
- Quota live: day cap 5, taken 0, left 5, can_submit true, blind-round slot available.
- Kit bundle_sha256 e445ed0f3ec2ea252e1739547aa8d3a0a0b389a74d2c8649b46cba346c05d09e (matches kit.json). Live skill.md = heartbeat 1.5.284.

## Remaining for parent (out of scope for this build)
Repo (GitHub, created after opens_at), push + approval, About (description/homepage/topics per repo_about), bundle, check, submit.
