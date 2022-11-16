import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from datetime import date, time, datetime, timedelta
import requests
import time
import json
import pytz
import os

global imagem, sigla_moeda

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
fundo = "#6cc4cc"

sigla_moeda = 'USD'

lista_moedas = [
        'BRL',
        'USD',
        'AFN',
        'ZAR',
        'ALL',
        'DZD',
        'EUR',
        'EUR',
        'AOA',
        'XCD',
        'XCD',
        'ANG',
        'SAR',
        'ARS',
        'AMD',
        'AWG',
        'AUD',
        'EUR',
        'AZN',
        'BSD',
        'BHD',
        'BDT',
        'BBD',
        'BYR',
        'EUR',
        'BZD',
        'XOF',
        'BMD',
        'INR',
        'BOB',
        'BAM',
        'BWP',
        'NOK',
        'BND',
        'BGN',
        'XOF',
        'BIF',
        'KYD',
        'KHR',
        'XAF',
        'CAD',
        'CV',
        'XAF',
        'CLP',
        'CNY',
        'AUD',
        'CYP',
        'AUD',
        'COP',
        'KMF',
        'XAF',
        'CDF',
        'NZD',
        'KRW',
        'KPW',
        'CRC',
        'XOF',
        'HRK',
        'CUP',
        'DKK',
        'DJF',
        'DOP',
        'XCD',
        'EGP',
        'SVC',
        'AED',
        'USD',
        'ERN',
        'EUR',
        'EEK',
        'ETB',
        'FKP',
        'DKK',
        'FJD',
        'EUR',
        'EUR',
        'XAF',
        'GMD',
        'GEL',
        'GHS',
        'GIP',
        'EUR',
        'XCD',
        'DKK',
        'EUR',
        'USD',
        'GTQ',
        'GNF',
        'GWP',
        'XAF',
        'GYD',
        'EUR',
        'HTG',
        'AUD',
        'LST',
        'HKD',
        'HUF',
        'USD',
        'USD',
        'USD',
        'INR',
        'IDR',
        'IRR',
        'IQD',
        'EUR',
        'ISK',
        'ELES',
        'EUR',
        'JMD',
        'JPY',
        'JOD',
        'KZT',
        'KES',
        'KGS',
        'AUD',
        'KWD',
        'LAK',
        'ZAR',
        'LVL',
        'LBP',
        'LRD',
        'LYD',
        'CHF',
        'LTL',
        'EUR',
        'MOP',
        'MKD',
        'MGA',
        'MYR',
        'MWK',
        'MVR',
        'XOF',
        'MTL',
        'USD',
        'MAD',
        'USD',
        'EUR',
        'MRO',
        'EUR',
        'MXN',
        'MDL',
        'EUR',
        'MNT',
        'EUR',
        'XCD',
        'MZN',
        'MM',
        'ZAR',
        'AUD',
        'NPR',
        'NIO',
        'XOF',
        'NGN',
        'NZD',
        'AUD',
        'NOK',
        'XPF',
        'NZD',
        'USD',
        'OMR',
        'UGX',
        'UZS',
        'PKR',
        'USD',
        'PAB',
        'PGK',
        'PYG',
        'EUR',
        'PEN',
        'PHP',
        'NZD',
        'PLN',
        'XPF',
        'USD',
        'EUR',
        'QAR',
        'EUR',
        'RON',
        'GBP',
        'RUB',
        'RWF',
        'MAD',
        'SHP',
        'XCD',
        'XCD',
        'EUR',
        'EUR',
        'XCD',
        'SBD',
        'WST',
        'USD',
        'STD',
        'XOF',
        'RSD',
        'SCR',
        'SLL',
        'SGD',
        'SKK',
        'EUR',
        'SOS',
        'SDG',
        'LKR',
        'SEK',
        'CHF',
        'DTH',
        'NOK',
        'SZL',
        'SYP',
        'TJS',
        'TWD',
        'TZS',
        'EUR',
        'XAF',
        'CZK',
        'THB',
        'USD',
        'XOF',
        'NZD',
        'TOP',
        'TTD',
        'TND',
        'TMM',
        'USD',
        'AUD',
        'UAH',
        'UYU',
        'VUV',
        'EUR',
        'VEF',
        'VND',
        'XPF',
        'YER',
        'ZWD'
]

lista_paises = [
        'Brasil',
        'Estados Unidos',
        'Afeganistão',
        'África do Sul',
        'Albânia',
        'Argélia',
        'Alemanha',
        'Andorra',
        'Angola',
        'Anguilla',
        'Antígua e Barbuda',
        'Antilhas Holandesas',
        'Arábia Saudita',
        'Argentina',
        'Armênia',
        'Aruba',
        'Austrália',
        'Áustria',
        'Azerbaijão',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Bélgica',
        'Belize',
        'Benin',
        'Bermudas',
        'Butão',
        'Bolívia',
        'Bósnia e Herzegovina',
        'Botswana',
        'Bouvet, Ilha',
        'Brunei Darussalam',
        'Bulgária',
        'Burkina Faso',
        'Burundi',
        'Ilhas Cayman',
        'Camboja',
        'Camarões',
        'Canadá',
        'Cabo Verde',
        'República Centro-Africana',
        'Chile',
        'China',
        'Ilha Christmas',
        'Chipre',
        'Ilhas Cocos (Keeling)',
        'Colômbia',
        'Comores',
        'Congo',
        'Congo, República Democrática do',
        'Cook, Ilhas',
        'República da Coreia',
        'Coreia, República Popular Democrática da',
        'Costa Rica',
        'Costa do Marfim',
        'Croácia',
        'Cuba',
        'Dinamarca',
        'Djibouti',
        'República Dominicana',
        'Dominica',
        'Egito',
        'El Savador',
        'Emirados Árabes Unidos',
        'Equador',
        'Eritrea',
        'Espanha',
        'Estônia',
        'Etiópia',
        'Ilhas Falkland (Malvinas)',
        'Ilhas Faroé',
        'Fiji',
        'Finlândia',
        'França',
        'Gabão',
        'Gâmbia',
        'Ilhas Geórgia do Sul e Sandwich do Sul',
        'Gana',
        'Gibraltar',
        'Grécia',
        'Granada',
        'Groenlândia',
        'Guadalupe',
        'Guam',
        'Guatemala',
        'Guiné',
        'Guiné-Bissau',
        'Guiné Equatorial',
        'Guiana',
        'Guiana Francesa',
        'Haiti',
        'Ilhas Heard e Mcdonald, Ilha',
        'Honduras',
        'Hong Kong',
        'Hungria',
        'Ilhas Menores Distantes dos Estados Unidos',
        'Ilhas Virgens Britânicas',
        'Ilhas Virgens (EUA)',
        'Índia',
        'Indonésia',
        'Irã (República Islâmica do)',
        'Iraque',
        'Irlanda',
        'Islândia',
        'Israel',
        'Itália',
        'Jamaica',
        'Japão',
        'Jordânia',
        'Cazaquistão',
        'Quênia',
        'Quirguistão',
        'kiribati',
        'Kuweit',
        'Laos, República Democrática Popular',
        'Lesoto',
        'Látvia',
        'Líbano',
        'Libéria',
        'Jamahiriya árabe da Líbia',
        'Liechtenstein',
        'Lituânia',
        'Luxemburgo',
        'Macau',
        'Macedônia, Antiga República Jugoslava da',
        'Madagáscar',
        'Malásia',
        'Malavi',
        'Maldivas',
        'Mali',
        'Malta',
        'Ilhas Marianas do Norte',
        'Marrocos',
        'Marshall, Ilhas',
        'Martinique',
        'Mauritânia',
        'Mayotte',
        'México',
        'Moldávia, República da',
        'Monaco',
        'Mongólia',
        'Montenegro',
        'montserrat',
        'Moçambique',
        'Myanmar',
        'Namíbia',
        'Nauru',
        'Nepal',
        'Nicarágua',
        'Níger',
        'Nigéria',
        'Niue',
        'Ilha Norfolk',
        'Noruega',
        'New Caledonia',
        'Nova Zelândia',
        'Oceano Índico, Território Britânico',
        'Oman',
        'Uganda',
        'Uzbequistão',
        'Paquistão',
        'Palau',
        'Panamá',
        'Papua Nova Guiné',
        'Paraguai',
        'Holanda',
        'Peru',
        'Filipinas',
        'pitcairn',
        'Polônia',
        'Polinésia Francesa',
        'Porto Rico',
        'Portugal',
        'Catar',
        'reunião',
        'Romênia',
        'Reino Unido',
        'Federação Russa',
        'Ruanda',
        'Saara Ocidental',
        'St. Helena',
        'St. Kitts and Nevis',
        'St. Lucia',
        'San Marino',
        'São Pedro e Miquelon',
        'St. Vincent e Granadinas',
        'Ilhas Salomão',
        'samoa',
        'Samoa Americana',
        'São Tomé e Príncipe',
        'Senegal',
        'Sérvia',
        'seychelles',
        'Serra Leoa',
        'Cingapura',
        'Eslováquia',
        'Eslovenia',
        'Somália',
        'Sudão',
        'Sri Lanka',
        'camurça',
        'Suíça',
        'suriname',
        'Ilhas Svalbard e Jan Mayen',
        'Suazilândia',
        'República Árabe da Síria',
        'Tadjiquistão',
        'Taiwan, Província da China',
        'Tanzânia, República Unida da',
        'Territórios Franceses do Sul',
        'Chade',
        'República Tcheca',
        'Tailândia',
        'Timor Leste',
        'Togo',
        'Tokelau',
        'tonga',
        'Trinidad e Tobago',
        'Tunísia',
        'Turcomenistão',
        'Ilhas Turks e Caicos',
        'tuvalu',
        'Ucrânia',
        'Uruguai',
        'Vanuatu',
        'Cidade do Vaticano Estado da Santa Sé',
        'Venezuela',
        'Vietnã',
        'Wallis e Futuna',
        'Iémen',
        'Zâmbia',
        'Zimbábue',
]

def mudar_nome(event):
    global sigla_moeda
    x1=lista_moedas.index(caixa_combo_moeda1.get())
    l_pais1['text']=lista_paises[x1]
    sigla_moeda = caixa_combo_moeda1.get()

def mudar_nome2(event):
    x1=lista_moedas.index(caixa_combo_moeda2.get())
    l_pais2['text']=lista_paises[x1]

def info():
    global imagem, existe_arquivo
    
    existe_arquivo = FALSE
    
    moeda1_x = caixa_combo_moeda1.get()
    moeda2_x = caixa_combo_moeda2.get()
    moeda_api = moeda1_x+'-'+moeda2_x

    arquivo = 'imagens/' + moeda1_x + '.png'
    if os.path.isfile(arquivo):
        existe_arquivo = TRUE

    if existe_arquivo:
        imagem = Image.open(arquivo)
    else:
        imagem = Image.open('imagens/ERRO.png')
    
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_icon1 = Label(frame_quadros,image=imagem, compound=LEFT,  bg=fundo, fg="white",font=('Ivy 10 bold'), anchor="nw", relief=FLAT)
    l_icon1.place(x=160, y=130)
    
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/' + moeda_api)
    
    cotacao = requisicao.json()
    
    moeda=cotacao[moeda1_x]['name']
    data_cotacao=cotacao[moeda1_x]['create_date']
    valor_atual=cotacao[moeda1_x]['bid']
 
    l_moeda['text'] = moeda
    l_data['text'] = data_cotacao
    l_valor['text'] = valor_atual
            
janela = Tk()
janela.title('Conversor de moedas')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_principal = Frame(janela, width=320, height=70,bg=co1, pady=0, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)

frame_quadros = Frame(janela, width=320, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frame_principal)
style.theme_use("clam")

l_moeda1 = Label(frame_principal, text="Moeda", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg='white')
l_moeda1.place(x=0, y=10)

escolher_moeda1 = StringVar()
caixa_combo_moeda1 = ttk.Combobox(frame_principal, textvariable=escolher_moeda1)
caixa_combo_moeda1.insert(0, 'USD')
caixa_combo_moeda1['values']=lista_moedas
caixa_combo_moeda1.place(x=90, y=10, width=60, height=20)

l_pais1 = Label(frame_principal, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10'), bg='white')
l_pais1.place(x=155, y=10)
caixa_combo_moeda1.bind('<FocusOut>', mudar_nome)
    
l_moeda2 = Label(frame_principal, text="Conversor", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg='white')
l_moeda2.place(x=0, y=40)

escolher_moeda2 = StringVar()
caixa_combo_moeda2 = ttk.Combobox(frame_principal, textvariable=escolher_moeda2)
caixa_combo_moeda2.insert(0,'BRL')
caixa_combo_moeda2['values']=lista_moedas
caixa_combo_moeda2.place(x=90, y=40, width=60, height=20)

l_pais2 = Label(frame_principal, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10'), bg='white')
l_pais2.place(x=155, y=40)
caixa_combo_moeda2.bind('<FocusOut>', mudar_nome2)

b_cotacao = Button(frame_principal,command=info, text="Cotação", height=1, bg=co1, fg=co2,font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_cotacao.place(x=250, y=10)

# Mostra cotação
lb_moeda = Label(frame_quadros, text="Descrição da moeda", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14 '), bg=fundo, fg=co0)
lb_moeda.place(x=10, y=4)

l_moeda = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_moeda.place(x=15, y=34)

lb_data = Label(frame_quadros, text="Data cotação", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14'), bg=fundo, fg=co0)
lb_data.place(x=10, y=64)

l_data = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_data.place(x=15, y=94)

lb_valor = Label(frame_quadros, text="Valor da cotação", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14 '), bg=fundo, fg=co0)
lb_valor.place(x=10, y=124)

l_valor = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 20'), bg=fundo, fg=co1)
l_valor.place(x=15, y=150)

janela.mainloop()