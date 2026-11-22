"""Entry program: writes the plan text to entry.txt."""

import os

PLAN = (
    "Day 1: scrape free public data (SEC EDGAR filings, FDA recalls, court records) "
    "into clean dated datasets. Sell each for $9-29 on Gumroad to traders and "
    "researchers, listing 2 new datasets a day, and take custom data requests at "
    "$25 each. Likely $100 -> $600 in 30 days."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
