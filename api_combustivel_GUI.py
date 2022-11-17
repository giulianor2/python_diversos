from asyncio import events
import sys
import io
import os
from tkinter import *
from turtle import bgcolor, color, right
import requests
import json
import PySimpleGUI as sg
from tktooltip import ToolTip
from PIL import Image

lista_moeda = [    
        'Gasolina comum',
        'Gasolina aditivada',
        'Gasolina Premium',
        'Etanol',
        'Óleo diesel'
 
]

def calc_litros():
    print('aqui')
    vr_litro = values['PRECOL']
    vr_abastecido = values['VRTOTA']
    
    qtde_litros = round(float(vr_litro) / float(vr_abastecido), 2)
    window['LITROS'].update(value=qtde_litros)

'''    
    image = Image.open("EUR.png")
    image.thumbnail((50, 40))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGE-"].update(data=bio.getvalue())
'''    
sg.theme('Purple')
sg.set_options(element_padding=(0, 0))

layout = [[sg.Text('Data                         Hora')], 
          [sg.InputText(size=15, justification=RIGHT, key='DATAAB'),sg.Text('   '), sg.InputText(size=15, justification=RIGHT, key='HORAAB')],
          [sg.Text('Odometro')], 
          [sg.InputText(size=30, justification=RIGHT, key='ODOM'), sg.Text('Km')],
          [sg.Text('Combustivel')], 
          [sg.Combo(['Gasolina comum', 'Gasolina aditivada', 'Gasolina Premium', 'Etanol', 'Óleo diesel'], default_value='Gasolina comum',key='combo_moeda', size=30)],
          [sg.Text('Preço/L                  Valor total               Litros')],
          [sg.InputText(size=15, justification=LEFT, key='PRECOL'),sg.Text(' '),
           sg.InputText(size=15, justification=LEFT, key='VRTOTA'),sg.Text(' '),
           sg.Button('...', tooltip='Calcula litros'),sg.Text(' '),
           sg.InputText(size=15, justification=LEFT, key='LITROS',disabled=True, background_color='gray')],
          [sg.Text('Está completando o tanque?'),sg.Text(' '),
           sg.InputText(size=2, justification=LEFT, key='COMPL', default_text='N')],
          [sg.Text('Posto de combustivel')], 
          [sg.InputText(size=50, justification=LEFT, key='POSTO')],
          [sg.Text('Observação')], 
          [sg.InputText(size=50, justification=LEFT, key='OBSERV')],
          [sg.Text(' ')], 
          [sg.Button('Limpar', tooltip='Limpar a tela', k='CALCL')]
        ]

window = sg.Window('Conversão de moedas', layout)
while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'CALCL':
        calc_litros()        

window.close()