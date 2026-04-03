import FreeSimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

sg.theme('Material1')  # Set the theme of the GUI

layout = [[sg.Text('Enter the text you want to be spoken:')],
          [sg.Input(key='input_text')],
          [sg.Text('Select the voice type:')],
          [sg.Radio('Male', 'voice_type', key='male_voice', default=True),
           sg.Radio('Female', 'voice_type', key='female_voice')],
          [sg.Text('Select the speech rate:')],
          [sg.Slider(range=(0, 200), default_value=100, size=(20, 10), orientation='h', key='speech_rate')],
          [sg.Text('Select the speech volume:')],
          [sg.Slider(range=(0, 100), default_value=50, size=(20, 10), orientation='h', key='speech_volume')],
          [sg.Button('Speak'), sg.Button('Exit')]]

window = sg.Window('Text-to-Speech App', layout, size=(400, 300))  # Create a window with the layout and size

while True:
    event, values = window.read()  # Read the window events and values
    if event == sg.WINDOW_CLOSED or event == 'Exit':  # If the window is closed or the Exit button is clicked
        break
    if event == 'Speak':  # If the Speak button is clicked
        engine.setProperty('rate', values['speech_rate'])  # Set the speech rate
        engine.setProperty('volume', values['speech_volume'] / 100)  # Set the speech volume
        if values['male_voice']:  # If the Male radio button is selected
            engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel')  # Set the male voice
        else:  # If the Female radio button is selected
            # Try different voice identifiers for the female voice
            if 'com.apple.speech.synthesis.voice.karen' in [voice.id for voice in engine.getProperty('voices')]:
                engine.setProperty('voice', 'com.apple.speech.synthesis.voice.karen')  # Set the female voice
            elif 'com.apple.speech.synthesis.voice.samantha' in [voice.id for voice in engine.getProperty('voices')]:
                engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')  # Set the female voice
            elif 'com.apple.speech.synthesis.voice.Victoria' in [voice.id for voice in engine.getProperty('voices')]:
                engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Victoria')  # Set the female voice
            else:
                sg.popup_error('Female voice not found')  # Display an error message if the female voice is not found