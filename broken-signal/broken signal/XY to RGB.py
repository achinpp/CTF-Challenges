import pandas as pd

INPUT_FILE = "redcypher_broken_signal_recovered_holes.csv"
OUTPUT_FILE = "outputtt.csv"

# Read the X,Y CSV file
df = pd.read_csv(INPUT_FILE)

# Check that required columns exist
if "X" not in df.columns or "Y" not in df.columns:
    raise ValueError("The input CSV must contain X and Y columns.")

# Convert X and Y to numeric values
df["X"] = pd.to_numeric(df["X"], errors="coerce")
df["Y"] = pd.to_numeric(df["Y"], errors="coerce")

# Detect missing or non-numeric values
if df[["X", "Y"]].isnull().any().any():
    bad_rows = df[df[["X", "Y"]].isnull().any(axis=1)]
    print("Invalid rows:")
    print(bad_rows.head(10))
    raise ValueError("The CSV contains missing or non-numeric X/Y values.")

# Convert to integers
x = df["X"].astype(int)
y = df["Y"].astype(int)

# Treat X as a five-digit value:
# Example: 8224 becomes 08224
# R = first three digits: 082 = 82
# G = final two digits: 24
r = x // 100
g = x % 100
b = y

final_df = pd.DataFrame({
    "R": r,
    "G": g,
    "B": b
})

# Ensure all generated RGB values are possible
invalid = final_df[
    (final_df["R"] < 0) | (final_df["R"] > 255) |
    (final_df["G"] < 0) | (final_df["G"] > 255) |
    (final_df["B"] < 0) | (final_df["B"] > 255)
]

if not invalid.empty:
    print("\nInvalid RGB rows:")
    print(invalid.head(20))
    raise ValueError(
        "Some generated RGB values are outside the valid range 0–255. "
        "For the 3-digit + 2-digit encoding, X cannot be greater than 25599."
    )

# Save without row numbers
final_df.to_csv(OUTPUT_FILE, index=False)

print(f"Success! {len(final_df)} RGB rows saved to {OUTPUT_FILE}")
print("\nFirst five converted rows:")
print(final_df.head())