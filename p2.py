# AGYAPONG SAMUEL BAFFOUR
# 10988638
# BMEN
import FreeSimpleGUI as sg
import pyttsx3
import threading

def speak(text, use_male):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if use_male:
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

layout = [
    [sg.Text("Enter your text here:")],
    [sg.InputText(key="input_text")],
    [sg.Text("Select a voice:")],
    [sg.Radio("Male", group_id="voice", key="male_voice"), sg.Radio("Female", group_id="voice", key="female_voice")],
    [sg.Button("Speak"), sg.Button("Stop")]
]

window = sg.Window("Text-to-Speech App", layout, resizable=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Stop":
        break

    if event == "Speak":
        text = values["input_text"]
        use_male = values["male_voice"]
        if text:
            t = threading.Thread(target=speak, args=(text, use_male))
            t.start()

window.close()