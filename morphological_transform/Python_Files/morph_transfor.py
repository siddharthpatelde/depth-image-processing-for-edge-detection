import cv2
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path

# -------- paths (repo-root aware) --------
ROOT = Path(__file__).resolve().parents[2]          # .../repo/
IMG_PATH = ROOT / "images" / "test-2.jpeg"          # input image
OUT_DIR  = ROOT / "images" / "morph_transform"      # output dir
OUT_DIR.mkdir(parents=True, exist_ok=True)

# -------- load --------
img = cv2.imread(str(IMG_PATH), cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError(f"Could not load image: {IMG_PATH}")

# -------- thresholding --------
# fixed/global threshold (your original)
_, mask = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)

# adaptive thresholds (tweak blockSize & C as needed; blockSize must be odd >= 3)
blockSize = 3
C = 35


mask_mean = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C
)

mask_gauss = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize, C
)

# -------- morphology on the (fixed) mask (unchanged) --------
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=1)
erosion  = cv2.erode(mask, kernel, iterations=3)
opening  = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
closing  = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mg       = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
th       = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

# -------- save outputs --------
to_save = {
    "adaptive_mean.png":   mask_mean,
    "adaptive_gaussian.png": mask_gauss,
    "dilation.png": dilation,
    "erosion.png":  erosion,
    "opening.png":  opening,
    "closing.png":  closing,
    "gradient.png": mg,
    "tophat.png":   th,
}
for name, arr in to_save.items():
    cv2.imwrite(str(OUT_DIR / name), arr)

# -------- show (2 x 5 grid) --------
titles = [
    'image', 'global mask', 'adaptive mean', 'adaptive gaussian',
    'dilation', 'erosion', 'opening', 'closing', 'gradient', 'tophat'
]
images = [img, mask, mask_mean, mask_gauss, dilation, erosion, opening, closing, mg, th]

plt.figure(figsize=(12, 6))
for i in range(len(images)):
    plt.subplot(2, 5, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=9)
    plt.xticks([]); plt.yticks([])

plt.tight_layout()
plt.show()
