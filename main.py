#!/usr/bin/env python3
import sys, subprocess, time, shutil
from pathlib import Path

# scripts to run, in order
SCRIPTS = [
    "Python_Files/04_average_blur.py",
    "Python_Files/05_gauss_blur.py",
    "Python_Files/06_median_blur.py",
    "Python_Files/07_bilateral_blur.py",
    "Python_Files/08_canny_on_blur.py",
    "morphological_transform/Python_Files/morph_transfor.py"
]

# name of your LaTeX file
LATEX_FILE = "document.tex"   # change to your actual .tex filename
OUTPUT_DIR = "pdf"            # folder where PDF will be saved

def main():
    base = Path(__file__).parent

    # Run Python scripts in sequence
    for name in SCRIPTS:
        script = base / name
        print(f"\n▶ Running {script.name} ...")
        try:
            subprocess.run([sys.executable, str(script)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"✖ {script.name} exited with error code {e.returncode}")
            break
        time.sleep(0.5)

    # Prepare LaTeX paths
    tex_path = base / LATEX_FILE
    output_dir = base / OUTPUT_DIR
    output_dir.mkdir(exist_ok=True)

    print("\n▶ Building LaTeX document...")
    try:
        subprocess.run([
            "pdflatex",
            "-synctex=1",
            "-interaction=nonstopmode",
            "--shell-escape",
            str(tex_path)
        ], check=True)

        # Move the PDF into output folder
        pdf_path = tex_path.with_suffix(".pdf")
        target_path = output_dir / pdf_path.name
        shutil.move(str(pdf_path), str(target_path))

        # Remove auxiliary files (.aux, .log, .out, .synctex.gz, etc.)
        for ext in [".aux", ".log", ".out", ".synctex.gz", ".toc"]:
            aux_file = tex_path.with_suffix(ext)
            if aux_file.exists():
                aux_file.unlink()

        # Open the PDF
        # subprocess.run(["xdg-open", str(target_path)])  # Linux
        # On macOS use: 
        subprocess.run(["open", str(target_path)])
        # On Windows use: subprocess.run(["start", str(target_path)], shell=True)

    except subprocess.CalledProcessError as e:
        print(f"✖ LaTeX build failed with error code {e.returncode}")

    print("\n✅ Done.")

if __name__ == "__main__":
    main()
