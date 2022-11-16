import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from tkinter import messagebox
import requests
import json

co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
fundo = "#6cc4cc"

def info():
    cep_p = e_local.get()
      
    if cep_p.isdigit and len(cep_p) == 8:
        #HTTP request
        requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_p))
        
        data = requisicao.json()
        
        cep_x = data['cep']
        logradouro_x = data['logradouro'] 
        complemento_x = data['complemento']
        bairro_x = data['bairro']
        cidade_x = data['localidade']
        uf_x = data['uf']
                
        l_logradouro['text'] = cep_p + " - " + logradouro_x 
        l_complemento['text'] = complemento_x
        l_bairro['text'] = bairro_x
        l_cidade['text'] = cidade_x
        l_uf['text'] = uf_x
        
        janela.configure(bg=fundo)
        frame_quadros.configure(bg=fundo)
        frame_principal.configure(bg=fundo)
        
        l_logradouro['bg'] = fundo
        l_complemento['bg'] = fundo
        l_bairro['bg'] = fundo
        l_cidade['bg'] = fundo
        l_uf['bg'] = fundo
        l_local['bg'] = fundo
    else:
        messagebox.showwarning(title='AVISO', message='Digite um CEP Válido')

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_principal = Frame(janela, width=320, height=50,bg=co1, pady=0, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)

frame_quadros = Frame(janela, width=320, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)

style = ttk.Style(frame_principal)
style.theme_use("clam")

l_local = Label(frame_principal, text="CEP", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=co1, fg=co0)
l_local.place(x=0, y=10)
   
e_local= Entry(frame_principal,width=20, justify='left',font=("",14),highlightthickness=1,relief="solid")
e_local.place(x=45, y=10, width=100)

b_ver = Button(frame_principal,command=info, text="Busca CEP", height=1, bg=co1, fg=co2,font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_ver.place(x=200, y=10)

l_logradouro = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_logradouro.place(x=10, y=4)

l_complemento = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_complemento.place(x=10, y=34)

l_bairro = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_bairro.place(x=10, y=64)

l_cidade = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_cidade.place(x=10, y=94)

l_uf = Label(frame_quadros, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12'), bg=fundo, fg=co1)
l_uf.place(x=10, y=124)

janela.mainloop()