# 1 Dalis Einaras
# Duomenų lentelės atvaizdavimas: Pagrindinėje programos dalyje turėsime lentelę
# kuri atvaizduos sportininko treniruočių duomenis. 
# Lentelė gali būti sudaryta iš stulpelių,
# kuriuose bus pateikti šie duomenys: data, atlikti pratimai, pakartojimų skaičius, 
# kilogramai arba kilogramais atlikti pratimai ir pan.
import PySimpleGUI as sg
import json

# Pradinių duomenų lentelė
data = []

# Lentelės stulpelių antraštės
header = ['Data', 'Atlikti pratimai', 'Trukmė (min)', 'Pakartojimų skaičius', 'Irankio Svoris (kg)']

# Sukuriamas lango išdėstymas
layout = [
    [sg.Table(values=data, headings=header, auto_size_columns=True, justification='right',
         display_row_numbers=False, num_rows=15, key='Table', size=(None, 400))],
    [sg.Button('Pridėti', size=(15, 1)), sg.Button('Redaguoti', size=(15, 1)),
     sg.Button('Ištrinti', size=(15, 1)), sg.Button('Saugoti į failą', size=(15, 1)),
     sg.Button('Atkurti iš failo', size=(15, 1)), sg.Button('Duomenų apdorojimas', size=(15, 1)),
     sg.Button('Išeiti', size=(15, 1))]
]


# Sukuriame langą su nurodytu dydžiu
window = sg.Window('Sportininko treniruočių duomenys', layout)

# Funkcija, kuri atnaujina lentelę
def update_table():
    window['Table'].update(values=data)

# Funkcija, kuri išvalo visus įvestus duomenis
def clear_input():
    for key in ('Data', 'Atlikti pratimai', 'Trukmė (min)', 'Pakartojimų skaičius', 'Irankio Svoris (kg)'):
        window[key].update('')

# Programos vykdomoji dalis
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Išeiti':
        break
    elif event == 'Pridėti':
        # Įvedimo langas
        input_layout = [
            [sg.Text('Data:', size=20), sg.InputText(key='Data')],
            [sg.Text('Atlikti pratimai:', size=20), sg.InputText(key='Atlikti pratimai')],
            [sg.Text('Trukmė (min):', size=20), sg.InputText(key='Trukmė (min)')],
            [sg.Text('Pakartojimų skaičius:', size=20), sg.InputText(key='Pakartojimų skaičius')],
            [sg.Text('Irankio Svoris (kg):', size=20), sg.InputText(key='Irankio Svoris (kg)')],
            [sg.Button('Pridėti'), sg.Button('Atšaukti')]
        ]

        input_window = sg.Window('Pridėti naują įrašą', input_layout, element_justification='center')


        while True:
            event, values = input_window.read()

            if event == sg.WIN_CLOSED or event == 'Atšaukti':
                input_window.close()
                break
            elif event == 'Pridėti':
                data.append([values['Data'], values['Atlikti pratimai'], values['Trukmė (min)'], values['Pakartojimų skaičius'], values['Irankio Svoris (kg)']])
                update_table()
                clear_input()
                input_window.close()

    elif event == 'Redaguoti':
        selected_row = values['Table'][0]
        if selected_row:
            # Redagavimo langas
            edit_layout = [
                [sg.Text('Data:'), sg.InputText(data[selected_row][0], key='Data')],
                [sg.Text('Atlikti pratimai:'), sg.InputText(data[selected_row][1], key='Atlikti pratimai')],
                [sg.Text('Trukmė (min):'), sg.InputText(data[selected_row][2], key='Trukmė (min)')],
                [sg.Text('Pakartojimų skaičius:'), sg.InputText(data[selected_row][3], key='Pakartojimų skaičius')],
                [sg.Text('Irankio Svoris (kg):'), sg.InputText(data[selected_row][4], key='Irankio Svoris (kg)')],
                [sg.Button('Išsaugoti'), sg.Button('Atšaukti')]
            ]

            edit_window = sg.Window('Redaguoti įrašą', [[sg.VerticalBox(edit_layout, element_justification='center')]])

            while True:
                event, values = edit_window.read()

                if event == sg.WIN_CLOSED or event == 'Atšaukti':
                    edit_window.close()
                    break
                elif event == 'Išsaugoti':
                    data[selected_row] = [values['Data'], values['Atlikti pratimai'], values['Trukmė (min)'], values['Pakartojimų skaičius'], values['Irankio Svoris (kg)']]
                    update_table()
                    edit_window.close()

    elif event == 'Ištrinti':
        selected_row = values['Table'][0]
        if selected_row:
            del data[selected_row]
            update_table()

    elif event == 'Saugoti į failą':
        with open('treniruotes.json', 'w') as file:
            json.dump(data, file)

    elif event == 'Atkurti iš failo':
        try:
            with open('treniruotes.json', 'r') as file:
                data = json.load(file)
                update_table()
        except FileNotFoundError:
            sg.popup_error('Failas nerastas.')

    elif event == 'Duomenų apdorojimas':
        # Čia galite pridėti savo duomenų apdorojimo kodą
        pass

window.close()


# 2 Dalis Lukas
#Įvedimo, redagavimo ir trynimo funkcionalumas (CRUD):
#Leiskite naudotojui įvesti naujas treniruotes į lentelę,
#redaguoti esamas, trinti nepageidaujamus įrašus ir peržiūrėti turimus įrašus. 
#Tai įgyvendins CRUD funkcionalumą (Create, Read, Update, Delete).


# 3 Dalis Eimantas
#Duomenų saugojimas į failą ir atkūrimas (JSON/Pickle):
#Sukurkite funkcijas, kurios leis naudotojui išsaugoti treniruočių duomenis į failą, 
#naudojant JSON arba Pickle formatą. 
#Be to, reikės funkcijų, kurios atkuria duomenis iš šio failo į programos lentelę.


# 4 Dalis Dainius 
#Duomenų apdorojimo funkcija:
#Sukurkite funkciją, kuri apdoros sportininko treniruočių duomenis. 
#Pavyzdžiui, galite šią funkciją panaudoti, kad apskaičiuotumėte, 
#kokia buvo vidutinė treniruočių trukmė, sumažinote svorius arba kilogramus per tam tikrą laikotarpį ir panašiai. 



import PySimpleGUI as sg
import json


### 3 Dalis Eimantas

# Funkcijos, kurios leis išsaugoti ir atkurti treniruočių duomenis į JSON failą

def save_to_json(data):
    with open('treniruotes.json', 'w') as file:
        json.dump(data, file, indent=4)

def load_from_json():
    try:
        with open('treniruotes.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

# PySimpleGUI

sg.theme('DarkBlue3')

layout = [
    [sg.Button('Pridėti'), sg.Button('Išsaugoti'), sg.Button('Atkurti')],
    [sg.Table(values=[], headings=['Data', 'Pratimai', 'Pakartojimai', 'Svoris'], auto_size_columns=False, justification='right', num_rows=10, key='table')],
]

window = sg.Window('Treniruočių Duomenys', layout, resizable=True)

data = load_from_json()

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Pridėti':
        data.append({
            'Data': values['data'],
            'Pratimai': values['pratimai'],
            'Pakartojimai': values['pakartojimai'],
            'Svoris': values['svoris']
        })
        window['table'].update(values=data)

    if event == 'Išsaugoti':
        save_to_json(data)
        sg.popup('Duomenys išsaugoti')

    if event == 'Atkurti':
        data = load_from_json()
        window['table'].update(values=data)

window.close()