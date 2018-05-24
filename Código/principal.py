import tkinter as tk
from criptoarquivo import *
from interface import *

Venda = historicoVenda()
Compra = historicoCompra()
Usuarios = bancoDeUsuarios()
Estoque = estoqueTotal() 
   
#---------------------------------FUNÇAO JANELA DE TRANSAÇOES-----------------------------------


#---------------------------LAYOUT JANELA DE LOGIN--------------------------------
window = tk.Tk()
window.title("Controle de Estoque - LPtech")
window.geometry("350x200+525+270")

titulo = tk.Label(text="Usuário:")
titulo.place(x=50, y=50)

entrada1 = tk.Entry()
entrada1.place(x=105, y=50)

senha = tk.Label(text="Senha:")
senha.place(x=50,y=75)

entrada2 = tk.Entry()
entrada2.place(x=105, y=75)

aviso = tk.Label(text="")
aviso.place(x=0,y=0)


botao1 = tk.Button(text = "Entrar", command = lambda: acesso(entrada1,entrada2,aviso,window))
botao1.place(x = 150, y=105)

window.mainloop()

