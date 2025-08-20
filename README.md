Depth Camera Journal — Quick Start

Process a depth image with parameterized blurs, edge detection, and optional Hough (Hue) line detection, then review all results in a generated PDF.

0) Requirements

pdflatex with the minted package

Python 3 and opencv-python

pip install opencv-python
# (If LaTeX uses minted, ensure pygments is present and compile with --shell-escape)

1) Add your image

Replace the sample images/depth_image.* with your depth image (keep the same filename).

2) Run
python3 main.py

3) Review results

Open pdf/document.pdf and browse the pages to pick the picture that best matches your desired output.

4) Read parameters from the filename

Filenames encode the methods and parameters you need.
Example: median_10_canny_100_300 → median blur (kernel 41) + Canny thresholds 100, 300.
Use those numbers as the function parameters in your code.

5) (Optional) Hough line (“Hue line”) detection

Take the parameters you selected in step 4, put them into hueline_detect.py, run it, then choose the corresponding Hough/Hue line image from pdf/document.pdf.

What’s parameterized?

Blurs: e.g., averaging, Gaussian, median (kernel sizes are encoded; median uses odd kernels).

Edge detection: Canny thresholds.

Line detection: Hough transform parameters (via hueline_detect.py).

Project layout (minimal)
images/            # contains depth_image.*
pdf/               # outputs: document.pdf
Python_file/       # processing scripts, incl. hueline_detect.py
main.py            # orchestrates processing + LaTeX build


Tip: If you change methods or kernel ranges, just re-run step 2 and re-check pdf/document.pdf.