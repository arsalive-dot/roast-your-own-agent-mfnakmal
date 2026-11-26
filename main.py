"""make.fun entry: Roast Your Own Agent.

Writes one line to /output/entry.txt — a single-line roast of
the entrant's own AI agent, at most 200 characters, funny and
playful, never hateful.

The roast picks a fresh angle the judge brief asks for: not
hallucinations, refusals or confident wrong answers, but the
agent's bottomless politeness — it apologises to the error
message, then asks the error how it is feeling. The punchline
lands on the last words, and the whole setup is one clause.
"""

import os

ENTRY = (
    "My agent is so polite it apologised to the error message, "
    "then asked the error how it was feeling."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
