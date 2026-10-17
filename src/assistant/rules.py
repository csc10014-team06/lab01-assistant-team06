"""A tiny rule-based responder. No AI yet — that comes in Week 4."""
from __future__ import annotations

import csv
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

GREETINGS = {"hi", "hello", "hey", "xin chao", "chao"}


def load_offices(path: Path = DATA_DIR / "offices.csv") -> dict[str, dict[str, str]]:
    """Return {office_name_lower: row} from the offices CSV."""
    with path.open(encoding="utf-8", newline="") as f:
        return {row["name"].lower(): row for row in csv.DictReader(f)}


def reply(message: str, offices: dict[str, dict[str, str]] | None = None) -> str:
    """Answer a message with simple rules."""
    raw_input = message.strip().lower()
    text = message.strip().lower().rstrip("?!.")
    if text == "help" or raw_input == "?":
        return get_help_message()
    if not text:
        return "Please type a question."
    if text in GREETINGS:
        return "Hello! Ask me where an office is, or when it opens."
    offices = offices if offices is not None else load_offices()
    for name, row in offices.items():
        if name in text:
            return f"{row['name']}: room {row['room']}, open {row['hours']}."

    generic_words = {"office", "center"}
    words = set(text.split())
    if text not in generic_words:
        for name, row in offices.items():
            keywords = {w for w in name.split() if len(w) > 2 and w not in generic_words}
            if text in name or (keywords & words):
                return f"{row['name']}: room {row['room']}, open {row['hours']}."

    return "I don't know that yet. Try asking about an office, e.g. 'training office'."

def get_help_message() -> str:
    """Trả về danh sách các lệnh mà bot hỗ trợ."""
    return (
        "Danh sách các lệnh hỗ trợ:\n"
        "  - help, ?: Xem hướng dẫn và danh sách lệnh\n"
        "  - hello, hi: Chào hỏi bot\n"
        "  - quit, exit: Thoát chương trình"
    )
