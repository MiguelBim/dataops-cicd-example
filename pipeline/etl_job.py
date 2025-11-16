import argparse
import os
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    # Minimal example transform: drop null rows and add total column if exists
    df = df.dropna().copy()
    if {"quantity", "price"}.issubset(df.columns):
        df["total"] = df["quantity"] * df["price"]
    return df

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--env", default=os.getenv("ENV", "dev"))
    args = parser.parse_args()

    print(f"[ETL] Running in env={args.env}")
    df = pd.read_csv(args.input)
    out = transform(df)
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"[ETL] Wrote {len(out)} rows to {args.output}")

if __name__ == "__main__":
    main()
