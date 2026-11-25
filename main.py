"""One-line entry for the make.fun bounty
"The Funniest Office Joke, Judged Head to Head".

The entry is a single joke line about office life. Running this
program prints the line and writes it (with no trailing newline)
to /output/entry.txt, which is the entry the judge reads.
"""

import os

ENTRY = "My manager says we are a family here, so I asked HR if that means I can ignore his emails the way I ignore my relatives."


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
