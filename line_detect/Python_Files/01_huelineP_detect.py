# file: line detect/Python file/01_huelineP_detect.py
import os
import cv2
import numpy as np

# ---- paths ----
img_path = "images/depth_gray.png"
out_dir  = "images/line_detect/houghp"
os.makedirs(out_dir, exist_ok=True)

# ---- load ----
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if img_gray is None:
    raise FileNotFoundError(f"Not found: {os.path.abspath(img_path)}")

# (optional) choose ONE blur by uncommenting and setting 'xx' from your PDF
# img_gray = cv2.blur(img_gray, (xx, xx))                     # Average blur
# img_gray = cv2.GaussianBlur(img_gray, (xx, xx), xx)         # Gaussian blur
img_gray = cv2.medianBlur(img_gray, 41)                     # Median blur (odd >1)
# img_gray = cv2.bilateralFilter(img_gray, xx, xx, xx)        # Bilateral (d, sigmaColor, sigmaSpace)

# ---- edge image ----
edge = img_gray.copy()
edge = cv2.Canny(img_gray, 210, 630, apertureSize=3, L2gradient=False)  # uncomment and set thresholds

# ---- HoughLinesP params ----
rho   = 1
theta = np.pi / 180
minLineLength = 0   # "none" → use 0
maxLineGap    = 10   # "none" → use 0

# thresholds: 30..630 step 30 → 21 images
for thr in range(0, 21, 1):
    # detect lines on the edge image
    lines = cv2.HoughLinesP(edge, rho, theta, threshold=thr,
                            minLineLength=minLineLength, maxLineGap=maxLineGap)

    # draw lines on a BGR version for visibility
    vis = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    if lines is not None:
        for x1, y1, x2, y2 in lines.reshape(-1, 4):
            cv2.line(vis, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # save
    out_path = os.path.join(out_dir, f"huelinep_{thr}.png")
    cv2.imwrite(out_path, vis)

print(f"Done. Saved {len(list(range(30,631,30)))} images to: {out_dir}")
