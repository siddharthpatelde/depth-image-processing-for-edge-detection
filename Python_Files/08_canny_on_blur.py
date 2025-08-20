import cv2, os

# inputs (gray grids you already saved)
base = "images"
inputs = [
    ("04_average_gray_grid.png",  "avg"),
    ("05_gaussian_gray_grid.png", "gauss"),
    ("06_median_gray_grid.png",   "median"),
    ("07_bilateral_gray_grid.png","bilateral"),
]

# output folder
out_dir = os.path.join(base, "canny_on_gray")
os.makedirs(out_dir, exist_ok=True)

# 21 Canny settings: (low, high) = (t, 3t) for t = 10..210
thresholds = list(range(10, 211, 10))  # 10,20,...,210  → 21 combos

for fname, tag in inputs:
    img = cv2.imread(os.path.join(base, fname), cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Skipped (not found): {fname}")
        continue
    for idx, t in enumerate(thresholds, 1):
        edges = cv2.Canny(img, t, 3*t, apertureSize=3, L2gradient=False)
        out = os.path.join(out_dir, f"{tag}_{idx:02d}_canny_{t}_{3*t}.png")
        cv2.imwrite(out, edges)

