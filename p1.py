# AGYAPONG SAMUEL BAFFOUR
# 10988638
# BMEN
import qrcode
import FreeSimpleGUI as sg
import io

def make_qr_bytes(url):
    image = qrcode.make(url)
    buf = io.BytesIO()
    image.save(buf, format='PNG')
    return buf.getvalue()

qrc_image = [sg.Image(data=b'', key='-QRCODE-', size=(350,350), background_color='gray')]

layout=[
    [sg.Input('', key='-URL-', justification='center')],
    [sg.Button('Create', key='-submit-', expand_x=True, button_color='blue')],
    [sg.Column([qrc_image], justification='center')],
]

wind = sg.Window('QRCode Generator APP', layout,  resizable=True)

while True:
    event, values = wind.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == '-submit-':
        url = values['-URL-']
        if url:
            qr_bytes = make_qr_bytes(url)
            wind['-QRCODE-'].update(data=qr_bytes)
            wind.refresh()

wind.close()