#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Prints exactly one line, a hilariously useless superpower, and writes
the same line to /output/entry.txt (the artifact the judge reads).

The line is fixed and printed verbatim: one run, one line, no variation.
"""
import os

LINE = "I can stop time, but only while I'm asleep, so I wake up exactly as late as ever."

def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass

if __name__ == "__main__":
    main()
