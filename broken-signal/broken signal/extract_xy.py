from PIL import Image
import csv


IMAGE_PATH = "reconstructed_image.png"
OUTPUT_CSV = "xy_values.csv"
PIXEL_LIMIT = 172352


img = Image.open(IMAGE_PATH).convert("RGB")
pixels = list(img.getdata())[:PIXEL_LIMIT]


with open(OUTPUT_CSV, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x", "y"])
    for r, g, b in pixels:
        x = r * 100 + g
        y = b
        writer.writerow([x, y])

print(f"Wrote {len(pixels)} rows to {OUTPUT_CSV}")