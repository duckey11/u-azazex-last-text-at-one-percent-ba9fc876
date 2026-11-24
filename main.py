#!/usr/bin/env python3
"""Last Text at One Percent - a dying phone's final text message."""

import os

TEXT = (
    "before i die, confession: i was never on silent, i just didn't like you. "
    "your ex texted twice. tell mom i love her and delete my search history, "
    "starting with 'can a phone feel pain'"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
