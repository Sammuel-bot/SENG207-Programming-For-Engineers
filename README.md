# SENG 207: Programming for Engineers
**University of Ghana, Legon | Biomedical Engineering (BMEN) | 2023**

Coursework projects completed as part of the SENG 207 Programming 
for Engineers course. All projects built with Python.

---

## Project 1 — Red Wine Quality Analysis (`10988638.ipynb`)
Exploratory data analysis on a dataset of 1,601 red wine samples.
Investigates how chemical properties (acidity, pH, alcohol content, 
sulphates, etc.) relate to wine quality scores.

- Loaded and cleaned raw CSV data, handling missing values
- Explored data distributions and summary statistics
- Generated a correlation heatmap to identify key quality indicators

**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

---

## Project 2 — Desktop GUI Applications

### p1.py — QR Code Generator
A desktop app that takes any URL or text and instantly generates 
a QR code displayed within the app.

**Tools:** Python, qrcode, FreeSimpleGUI

### p2.py — Text-to-Speech App
A desktop app that converts typed text to spoken audio, with options 
to switch between male and female voices.

**Tools:** Python, pyttsx3, FreeSimpleGUI, threading

---

## Notes
> p1.py and p2.py were originally built with PySimpleGUI. Since that 
> library moved to a paid model after v4.x, the code has been updated 
> to use FreeSimpleGUI, a free open-source fork with identical syntax.

## Requirements
```bash
pip install qrcode[pil] FreeSimpleGUI pyttsx3 pandas numpy matplotlib seaborn
```

## What I Learned
- Data cleaning and handling missing values with Pandas
- Exploratory data analysis and visualizing patterns in real datasets
- Building desktop GUI applications with Python
- Working with external libraries (qrcode, pyttsx3)
- Using threading to prevent UI freezing during audio playback
- Structuring Python projects across multiple files
