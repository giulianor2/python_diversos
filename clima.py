import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.tix import *
from PIL import ImageTk, Image
import pytz
import requests
import datetime
import pycountry_convert as pc
import json
import time
from datetime import datetime

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul

fundo_dia="#6cc4cc"
fundo_noite="#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

def info():
    weather_key = '74db8d03761c1e007553ccbc6d73fe92'
    cidade = e_local.get()
    api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + cidade + "&appid=" + weather_key + "&lang=pt"

    #HTTP request
    requisicao=requests.get(api_link)

    data=requisicao.json()
    
    # zona , pais, horas 
    pais_codigo = data['sys']['country']
    
    zona_fuso=pytz.country_timezones[pais_codigo]
    pais = pytz.country_names[pais_codigo]
    
    # data
    zona = pytz.timezone(zona_fuso[0]) 
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")
    
    tempo= data["main"]["temp"]
    pressao = data["main"]["pressure"]
    umidade = data["main"]["humidity"]
    velocidade = data["wind"]["speed"]
    descrcao = data["weather"][0]["description"]
    
    # Mudando informaçoes
    def country_to_continent(country_name):
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    
    continente= country_to_continent(pais)
    
    l_cidade['text'] = cidade + " - " + pais +" / "+ continente
    l_data['text'] = zona_horas
    l_pressao['text'] = "Pressão : "+ str(pressao)
    l_umidade['text'] = umidade
    l_umidade_simbol['text'] = "%"
    l_umidade_nome['text'] = "Humidade"
    l_velocidade['text'] = "velocidade do vento : "+ str(velocidade)
    l_descricao['text'] = descrcao
    
    zona_regiao = datetime.now(zona)
    zona_regiao = zona_regiao.strftime("%H")
    
    global imagem
    
    zona_regiao = int(zona_regiao)
    if zona_regiao <= 5:
        imagem = Image.open('imagens/lua.png')
        fundo = fundo_noite
    elif zona_regiao <= 11:
        imagem = Image.open('imagens/sol_dia.png')
        fundo = fundo_dia
    elif zona_regiao <= 17:
        imagem = Image.open('imagens/sol_tarde.png')
        fundo = fundo_tarde
    elif zona_regiao <= 23:
        imagem = Image.open('imagens/lua.png')
        fundo= fundo_noite
    else: 
        pass  
     
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_icon1 = Label(frame_quadros,image=imagem, compound=LEFT,  bg=fundo, fg="white",font=('Ivy 10 bold'), anchor="nw", relief=FLAT)
    l_icon1.place(x=160, y=50)
    
    janela.configure(bg=fundo)
    frame_quadros.configure(bg=fundo)
    frame_principal.configure(bg=fundo)
    
    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_pressao['bg'] = fundo
    l_umidade['bg'] = fundo
    l_umidade_simbol['bg'] =fundo
    l_umidade_nome['bg'] = fundo
    l_velocidade['bg'] = fundo
    l_descricao['bg'] = fundo
        
janela = Tk()
janela.title('Clima')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

tip = Balloon(janela)

frame_principal = Frame(janela, width=320, height=50,bg=co1, pady=0, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)

frame_quadros = Frame(janela, width=320, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frame_principal)
style.theme_use("clam")

e_local= Entry(frame_principal,width=20, justify='left',font=("",14),highlightthickness=1,relief="solid")
e_local.place(x=15, y=10)
tip.bind_widget(e_local, balloonmsg="Digite o nome da cidade")

b_ver = Button(frame_principal,command=info, text="Ver clima", height=1, bg=co1, fg=co2,font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_ver.place(x=250, y=10)

l_cidade = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 14 '), bg=fundo, fg=co1)
l_cidade.place(x=10, y=4)

l_data = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_data.place(x=10, y=54)

l_umidade = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 45 '), bg=fundo, fg=co1)
l_umidade.place(x=10, y=100)

l_umidade_simbol = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 bold '), bg=fundo, fg=co1)
l_umidade_simbol.place(x=85, y=110)

l_umidade_nome = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 8 '), bg=fundo, fg=co1)
l_umidade_nome.place(x=85, y=140)

l_pressao = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 10 '), bg=fundo, fg=co1)
l_descricao.place(x=170, y=190)

janela.mainloop()