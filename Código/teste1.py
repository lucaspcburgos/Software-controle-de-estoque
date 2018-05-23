import tkinter as tk
from criptoarquivo import *

dicVenda = {}
dicCompra = {}
dicUsuario = {}
listaVenda = []
listaCompra = []
dicEstoque = {}   
   
#---------------------------------FUNÇAO JANELA DE TRANSAÇOES-----------------------------------
def criaJanelaTransacao():
    
    #----------------------FUNCIONAMENTO DA JANELA TRANSAÇAO-----------------------------
    #VENDAS
    def registraTransacaoVenda():
        chaveVenda = produtoEntrada.get()
        quantidadeVenda = quantidadeEntrada.get()
        precoVenda = precoEntrada.get()
        tuplaVenda = (quantidadeVenda, precoVenda)
        if chaveVenda in dicVenda and chaveVenda in dicEstoque:
            listaVenda = dicVenda[chaveVenda]
            listaVenda.append(tuplaVenda)
            dicVenda[chaveVenda] = listaVenda#---------------------->>> ESCREVER NO ARQUIVO
        else:
            if chaveVenda in dicEstoque:
                listaVenda = []
                listaVenda.append(tuplaVenda)
                dicVenda[chaveVenda] = listaVenda
        if chaveVenda in dicEstoque:
            dicEstoque[chaveVenda] += -int(tuplaVenda[0])
            if dicEstoque[chaveVenda] <= 0:
                dicEstoque.pop(chaveVenda)
            
        else:
            dicEstoque[chaveVenda] = -int(tuplaVenda[0])
            if dicEstoque[chaveVenda] < 0:
                dicEstoque.pop(chaveVenda)
        
        print(dicEstoque)
        print(dicVenda) 
        
    #COMPRAS
    def registraTransacaoCompra():
        chaveCompra = produtoEntrada.get()
        quantidadeCompra = quantidadeEntrada.get()
        precoCompra = precoEntrada.get()
        tuplaCompra = (quantidadeCompra, precoCompra)
        if chaveCompra in dicCompra:
            listaCompra = dicCompra[chaveCompra]
            listaCompra.append(tuplaCompra)
            dicCompra[chaveCompra] = listaCompra#---------------------->>> ESCREVER NO ARQUIVO
        else:
            listaCompra = []
            listaCompra.append(tuplaCompra)
            dicCompra[chaveCompra] = listaCompra
        if chaveCompra in dicEstoque:
            dicEstoque[chaveCompra] += int(tuplaCompra[0])
            
        else:
            dicEstoque[chaveCompra] = int(tuplaCompra[0])
        
        print(dicCompra) 
        print(dicEstoque)

    #-----------------LAYOUT JANELA TRANSAÇAO--------------------
    janelaTransacao = tk.Tk()
    janelaTransacao.title("Registrar Transação")
    janelaTransacao.geometry("400x200+525+270")
    
    #--------------------LAYOUT DOS BOTOES--------------------------
    produto = tk.Label(janelaTransacao, text="Produto:")
    produto.place(x=20,y=20)
    
    produtoEntrada = tk.Entry(janelaTransacao,width="30")
    produtoEntrada.place(x=105,y=20)

    produtoQuantidade = tk.Label(janelaTransacao, text="Quantidade:")
    produtoQuantidade.place(x=20,y=50)

    quantidadeEntrada = tk.Entry(janelaTransacao,width="30" )
    quantidadeEntrada.place(x=105,y=50)

    produtoPreco = tk.Label(janelaTransacao, text="Preço:")
    produtoPreco.place(x=20,y=80)

    precoEntrada = tk.Entry(janelaTransacao, width="30")
    precoEntrada.place(x=105,y=80)

    botaoVenda = tk.Button(janelaTransacao, text="Registrar Venda", width="17", command=registraTransacaoVenda)
    botaoVenda.place(x=20,y=110)
    
    botaoCompra = tk.Button(janelaTransacao, text="Registrar Compra", width="17", command=registraTransacaoCompra)
    botaoCompra.place(x=190 ,y=110)

    botaoCancela = tk.Button(janelaTransacao, text="Cancelar", width="38", command=janelaTransacao.destroy)
    botaoCancela.place(x=20,y=140)
    botaoCancela["bg"] = "red"
    
    janelaTransacao.mainloop()

#------------------------------FUNÇAO JANELA GERENCIAMENTO DE USUARIO-----------------------------
def criaJanelaGerenciamento():
    #---------------------------FUNCIONAMENTO GERENCIAMENTO DE USUARIO -----------------------------
    def gerenciaUsuario():
        chaveNome = entradaNomeUsuario.get()
        cpf = entradaCpf.get()
        telefone = entradaTelefone.get()
        senha = entradaSenha.get()
        nivel = entradaNivel.get()        
        tuplaUsuario = (senha, nivel, telefone, cpf)
        if chaveNome in dicUsuario:
            dicUsuario[chaveNome] = tuplaUsuario#---------------------->>> ESCREVER NO ARQUIVO
        else:
            listaUsuario = []
            listaUsuario.append(tuplaUsuario)
            dicUsuario[chaveNome] = listaUsuario
        print(dicUsuario) 

    #---------------------------------FUNCIONAMENTO PESQUISA DE USUARIO----------------------------
    def pesquisaUsuario():
        pesquisaNome = pesquisaEntrada.get()
        if pesquisaNome in dicUsuario:
            resultadoNome["text"] = "Nome:",pesquisaNome
            resultadoCpf["text"] = "CPF:" ,dicUsuario[pesquisaNome][0][3]
            resultadoTelefone["text"] = "Telefone:" ,dicUsuario[pesquisaNome][0][2]
            resultadoNivel["text"] = "Nível:" ,dicUsuario[pesquisaNome][0][1]
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = "ERRO: Usuário não cadastrado no sistema" 
            resultadoTelefone["text"] = "" 
            resultadoNivel["text"] = "" 

    #------------------------------FUNCIONAMENTO BOTAO EXCLUIR------------------------------------
    def excluirUsuario():
        excluiNome = pesquisaEntrada.get()
        if excluiNome in dicUsuario:
            dicUsuario.pop(excluiNome)
            print(dicUsuario)
            resultadoNome["text"] = ""
            resultadoCpf["text"] = "" 
            resultadoTelefone["text"] = "" 
            resultadoNivel["text"] = "" 
            resultadoExclusao["text"] = "USUÁRIO EXCLUÍDO COM SUCESSO!"
        else:
            resultadoNome["text"] = ""
            resultadoCpf["text"] = "" 
            resultadoTelefone["text"] = "" 
            resultadoNivel["text"] = "" 
            resultadoExclusao["text"] = "IMPOSSÍVEL EXCLUIR"
            
    #--------------------------LAYOUT JANELA GERENCIAMENTO----------------------------
    
    janelaGerenciamento = tk.Tk()
    janelaGerenciamento.geometry("530x420+525+0")
    janelaGerenciamento.title("Gerenciamento de Usuário")

    #--------------------------BOTOES ADICIONAR USUARIO------------------------------
    nomeUsuario = tk.Label(janelaGerenciamento, text="Nome do usuário:")
    nomeUsuario.place(x=20,y=20)

    entradaNomeUsuario = tk.Entry(janelaGerenciamento, width="42")
    entradaNomeUsuario.place(x=150,y=20)

    cpfUsuario = tk.Label(janelaGerenciamento, text="CPF do usuário:")
    cpfUsuario.place(x=20,y=50)

    entradaCpf = tk.Entry(janelaGerenciamento, width="42")
    entradaCpf.place(x=150,y=50)

    telefoneUsuario = tk.Label(janelaGerenciamento, text="Telefone do usuário:")
    telefoneUsuario.place(x=20,y=80)

    entradaTelefone = tk.Entry(janelaGerenciamento, width="42")
    entradaTelefone.place(x=150,y=80)

    senhaUsuario = tk.Label(janelaGerenciamento, text="Senha do usuário:")
    senhaUsuario.place(x=20,y=110)

    entradaSenha = tk.Entry(janelaGerenciamento, width="42")
    entradaSenha.place(x=150,y=110)

    nivelUsuario = tk.Label(janelaGerenciamento, text="Digite o nível de acesso:\n\nNível 1:Acesso mínimo | Nível 2:Acesso intermediário | Nível 3: Acesso máximo")
    nivelUsuario.place(x=20,y=140)

    entradaNivel = tk.Entry(janelaGerenciamento, width="2")
    entradaNivel.place(x=340,y=140)

    botaoAddUsuario = tk.Button(janelaGerenciamento, text="Atualizar usuário", command=gerenciaUsuario)
    botaoAddUsuario.place(x=200,y=190)

    #-----------------------------------BOTOES PESQUISAR USUARIO-----------------------------------
    nomePesquisa = tk.Label(janelaGerenciamento, text="Nome:")
    nomePesquisa.place(x=20,y=270)

    pesquisaEntrada = tk.Entry(janelaGerenciamento, width="40")
    pesquisaEntrada.place(x=70, y=270)

    botaoPesquisar = tk.Button(janelaGerenciamento, text="Pesquisar", command=pesquisaUsuario)
    botaoPesquisar.place(x=400,y=267)
    #----------------------------------RESULTADO DA PESQUISA---------------------------------------
    resultadoNome = tk.Label(janelaGerenciamento, text="")
    resultadoNome.place(x=170,y=300)

    resultadoCpf = tk.Label(janelaGerenciamento, text="")
    resultadoCpf.place(x=170,y=315)

    resultadoTelefone = tk.Label(janelaGerenciamento, text="")
    resultadoTelefone.place(x=170,y=330)

    resultadoNivel = tk.Label(janelaGerenciamento, text="")
    resultadoNivel.place(x=170,y=345)
    #------------------------------BOTAO PARA EXCLUIR USUARIO---------------------------------------
    botaoExcluir = tk.Button(janelaGerenciamento, text="Excluir\nUsuário",height="3", command=excluirUsuario)
    botaoExcluir["bg"] = "red"
    botaoExcluir.place(x=70,y=300)
    #-----------------------------RESULTADO DA AÇAO EXCLUIR---------------------------------------
    resultadoExclusao = tk.Label(janelaGerenciamento, text="")
    resultadoExclusao.place(x=160,y=400)

#-----------------------------FUNÇAO CRIA JANELA PESQUISAR PRODUTO---------------------------------
def criaJanelaPesquisaProduto():
    
    #---------------------------FUNCIONAMENTO BOTOES PESQUISA PRODUTO-------------------------------
    def pesquisaProduto():
        pesquisaProdutoNome = entradaNomeProduto.get()
        if pesquisaProdutoNome in dicEstoque:
            produtoResultadoNome["text"] = "Nome:",pesquisaProdutoNome
            produtoResultadoQuantidade["text"] = "Qtd em estoque:",dicEstoque[pesquisaProdutoNome]
            janelaPesquisaProduto.geometry("415x140+525+270")
        else:
            produtoResultadoNome["text"] = pesquisaProdutoNome,"em falta!"
            produtoResultadoQuantidade["text"] = ""

    #-------------------------------LAYOUT JANELA PESQUISA PRODUTO---------------------------------
    janelaPesquisaProduto = tk.Tk()
    janelaPesquisaProduto.geometry("415x100+525+270")
    janelaPesquisaProduto.title("Pesquisa Produto")

    #-----------------------------LAYOUT BOTOES PESQUISA PRODUTO-----------------------------------
    nomeProduto = tk.Label(janelaPesquisaProduto, text="Nome do produto:")
    nomeProduto.place(x=20,y=20)

    entradaNomeProduto = tk.Entry(janelaPesquisaProduto, width="30")
    entradaNomeProduto.place(x=140, y=20)

    botaoProcurar = tk.Button(janelaPesquisaProduto, text="Pesquisar", command=pesquisaProduto)
    botaoProcurar.place(x=160,y=50)

    produtoResultadoNome = tk.Label(janelaPesquisaProduto, text="")
    produtoResultadoNome.place(x=140,y=80)

    produtoResultadoQuantidade = tk.Label(janelaPesquisaProduto, text="")
    produtoResultadoQuantidade.place(x=125,y=100)
    

#------------------------------------FUNÇAO TELA ADMIN--------------------------------------
def telaAdmin():
    #--------------------LAYOUT JANELA ADMIN----------------------
    window.destroy()
    janela = tk.Tk()
    janela.geometry("470x340+525+270")
    janela.title("Controle de Estoque - LPtech (Administrador)")

    #----------------------LAYOUT DOS BOTOES--------------------------
    botaoTransacao = tk.Button(janela, text="Registrar Transação", width="50", height="3", command=criaJanelaTransacao)
    botaoTransacao.place(x=20,y=20)

    botaoCadastro = tk.Button(janela, text="Gerenciamento de Usuário", width="50", height="3", command=criaJanelaGerenciamento)
    botaoCadastro.place(x=20,y=80)

    botaoPesquisa = tk.Button(janela, text="Pesquisar Produto", width="50", height="3", command=criaJanelaPesquisaProduto)
    botaoPesquisa.place(x=20,y=140)

    botaoHistorico = tk.Button(janela, text="Histórico de Transações", width="50", height="3")
    botaoHistorico.place(x=20,y=200)

    botaoEstoque = tk.Button(janela, text="Checar Estoque", width="50", height="3")
    botaoEstoque.place(x=20,y=260)

    janela.mainloop()
    
#----------------------------------FUNÇAO DE LOGIN---------------------------------
def acesso():
    botao1["bg"] = "green"
    usuario = entrada1.get()
    password = entrada2.get()
    if usuario == "admin" and password == "admin":
        telaAdmin()
    elif usuario == "admin2" and password == "admin2":
        criaJanelaGerenciamento()
    else:
        aviso["text"] = "Usuário ou senha incorretos"

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

botao1 = tk.Button(text = "Entrar", command = acesso)
botao1.place(x = 150, y=105)

window.mainloop()

