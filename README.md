# SENG 207: Programming for Engineers
**University of Ghana, Legon | Biomedical Engineering (BMEN) | 2023**

- ####  SENG 207 – Programming for Engineers is intended to introduce the fundamental concepts in computer programming to undergraduate engineering students. 

- ####  Students will be introduced to Python Programming with specific focus in deepening their problem-solving skills using both structured and object-oriented programming approaches. 

- ####  The labs and exercises are designed to enhance the students’ skills in creating complete programs to solve engineering, and other real-world problems. 

# The objectives:
- #### To deepen students understanding in structured programming whiles introducing them to the fundamentals of computer programming.

- #### To give hands on training to students in order to develop their skill in using programming to solve engineering and other real world problems.

# Course Projects

<p>The course projects for SENG207 Programming for Engineers are shown in the table below:</p>

|Project|Title|Comment|
|----|----|----|
|1 |Console Applications |Implementation of Python collections, arithmetic operations, and functions|
|2|Unit Convertor Desktop Application|Implementation of logical controls and use of modules and libraries|
|3|Desktop Text Editor Application|Implementation of logical controls and use of modules and libraries|
|4|Simple Web Application|Implementation of OOP and programming logic for CRUD|
|5|Data Analytics Project|Data analysis, data visualization, data inferences using data analytic libraries|

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

---

## Project 3 — Tic-Tac-Toe GUI (`p11.py`)
A fully playable two-player Tic-Tac-Toe game with a graphical interface.
Handles win detection across all rows, columns, and diagonals.

**Tools:** Python, FreeSimpleGUI

### p9.py — Terminal Version
A command-line version of the same game built before the GUI version.

---

## Project 4 — Enhanced Text-to-Speech App (`p8.py`)
An improved version of the TTS app with additional controls for 
speech rate and volume via sliders, and automatic voice fallback 
if a selected voice is unavailable on the system.


**Tools:** Python, pyttsx3, FreeSimpleGUI
```

---


## What I Learned
- Data cleaning and handling missing values with Pandas
- Exploratory data analysis and visualizing patterns in real datasets
- Building desktop GUI applications with Python
- Working with external libraries (qrcode, pyttsx3)
- Using threading to prevent UI freezing during audio playback
- Structuring Python projects across multiple files
- Iterative development — improving the same app across multiple versions
- Game logic implementation (win detection, turn switching)
- Building interactive GUIs with buttons, sliders, and radio controls
- Handling edge cases (unavailable voices, occupied board positions)
