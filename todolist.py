from cores import *

tarefas = []

LARGURA = 48
COR_BORDA = FRENTE_CINZA
COR_DESTAQUE = FRENTE_CIANO_CLARO
COR_TITULO = FRENTE_MAGENTA_CLARO


# ---------------------------------------------------------------
# Mensagens (elas DEVOLVEM o texto pronto, quem imprime é a tela)
# ---------------------------------------------------------------
def sucesso(texto):
    return "  " + FRENTE_VERDE_CLARO + "✔ " + texto + RESET


def erro(texto):
    return "  " + FRENTE_VERMELHO_CLARO + "✖ " + texto + RESET


def aviso(texto):
    return "  " + FRENTE_CIANO + "• " + texto + RESET


# ---------------------------------------------------------------
# Desenho da caixa
# ---------------------------------------------------------------
def topo():
    print(COR_BORDA + "╭" + "─" * (LARGURA - 2) + "╮" + RESET)


def divisoria():
    print(COR_BORDA + "├" + "─" * (LARGURA - 2) + "┤" + RESET)


def base():
    print(COR_BORDA + "╰" + "─" * (LARGURA - 2) + "╯" + RESET)


def linhaCaixa(conteudo, tamanho):
    # 'conteudo' pode ter cores. 'tamanho' é quantas letras aparecem
    # na tela (as cores não ocupam espaço). Com ele completamos os
    # espaços e a borda da direita fica alinhada.
    espacos = LARGURA - 4 - tamanho
    print(COR_BORDA + "│" + RESET + " " + conteudo + " " * espacos + " " + COR_BORDA + "│" + RESET)


def linhaCentralizada(texto, cor):
    # Centraliza ANTES de colorir, assim o tamanho fica certo
    centralizado = texto.center(LARGURA - 4)
    linhaCaixa(cor + centralizado + RESET, LARGURA - 4)


def linhaMenu(tecla1, texto1, tecla2="", texto2=""):
    # Mostra até duas opções lado a lado: "1 › Adicionar    2 › Concluir"
    parte1 = COR_DESTAQUE + tecla1 + RESET + " " + COR_BORDA + "›" + RESET + " " + texto1
    tamanho1 = len(tecla1 + " › " + texto1)

    if tecla2 == "":
        linhaCaixa(parte1, tamanho1)
    else:
        parte2 = COR_DESTAQUE + tecla2 + RESET + " " + COR_BORDA + "›" + RESET + " " + texto2
        tamanho2 = len(tecla2 + " › " + texto2)
        espacos = " " * (20 - tamanho1)  # a segunda coluna começa na posição 20
        linhaCaixa(parte1 + espacos + parte2, 20 + tamanho2)


# ---------------------------------------------------------------
# Funções de apoio
# ---------------------------------------------------------------
def cortar(texto, limite):
    # Se o texto for muito grande, corta e coloca … no final
    if len(texto) > limite:
        return texto[: limite - 1] + "…"
    return texto


def lerNumero(pergunta):
    # Devolve o número digitado ou None se não for um número
    try:
        return int(input(COR_DESTAQUE + "❯ " + RESET + pergunta))
    except ValueError:
        return None


# ---------------------------------------------------------------
# Tela
# ---------------------------------------------------------------
def mostrarTela(mensagem):
    print()
    topo()
    linhaCentralizada("✦  MINHAS TAREFAS  ✦", COR_TITULO + ESTILO_NEGRITO)
    divisoria()

    if len(tarefas) == 0:
        linhaCaixa("", 0)
        linhaCentralizada("Nenhuma tarefa ainda.", FRENTE_CINZA)
        linhaCentralizada("Digite 1 para começar!", FRENTE_CINZA)
        linhaCaixa("", 0)
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            nome = cortar(tarefa["nome"], 36)
            tamanho = len(f"○ {numero:>2} │ {nome}")

            if tarefa["feita"]:
                simbolo = FRENTE_VERDE_CLARO + "✔" + RESET
                nome = FRENTE_CINZA + ESTILO_RISCADO + nome + RESET
            else:
                simbolo = COR_DESTAQUE + "○" + RESET

            conteudo = f"{simbolo} {FRENTE_AMARELO}{numero:>2}{RESET} {COR_BORDA}│{RESET} {nome}"
            linhaCaixa(conteudo, tamanho)

    divisoria()
    linhaMenu("1", "Adicionar", "2", "Concluir/desfazer")
    linhaMenu("3", "Remover", "4", "Limpar feitas")
    linhaMenu("0", "Sair")
    base()
    print(mensagem)


# ---------------------------------------------------------------
# Ações do menu (cada uma devolve uma mensagem)
# ---------------------------------------------------------------
def adicionarTarefa():
    nome = input("\n" + COR_DESTAQUE + "❯ " + RESET + "Nome da tarefa: ").strip()

    if nome == "":
        return erro("A tarefa não pode ficar vazia")

    tarefas.append({"nome": nome, "feita": False})
    return sucesso("Tarefa adicionada!")


def concluirTarefa():
    if len(tarefas) == 0:
        return erro("Não há tarefas para concluir")

    numero = lerNumero("\nNúmero da tarefa: ")

    if numero is None:
        return erro("Digite apenas números")
    if numero < 1 or numero > len(tarefas):
        return erro("Número inválido")

    tarefa = tarefas[numero - 1]
    tarefa["feita"] = not tarefa["feita"]  # liga e desliga

    if tarefa["feita"]:
        return sucesso("Tarefa concluída. Mandou bem!")
    return aviso("Tarefa voltou para pendente")


def removerTarefa():
    if len(tarefas) == 0:
        return erro("Não há tarefas para remover")

    numero = lerNumero("\nNúmero da tarefa: ")

    if numero is None:
        return erro("Digite apenas números")
    if numero < 1 or numero > len(tarefas):
        return erro("Número inválido")

    removida = tarefas.pop(numero - 1)
    return sucesso(f"Tarefa '{cortar(removida['nome'], 25)}' removida!")


def limparFeitas():
    pendentes = []
    for tarefa in tarefas:
        if not tarefa["feita"]:
            pendentes.append(tarefa)

    removidas = len(tarefas) - len(pendentes)

    if removidas == 0:
        return aviso("Nenhuma tarefa concluída para limpar")

    tarefas.clear()
    tarefas.extend(pendentes)
    return sucesso(f"{removidas} tarefa(s) concluída(s) removida(s)")


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
mensagem = aviso("Bem-vindo! Escolha uma opção do menu.")
opcao = ""

while opcao != "0":
    mostrarTela(mensagem)
    opcao = input("\n" + COR_DESTAQUE + "❯ " + RESET + "Opção: ")

    if opcao == "1":
        mensagem = adicionarTarefa()
    elif opcao == "2":
        mensagem = concluirTarefa()
    elif opcao == "3":
        mensagem = removerTarefa()
    elif opcao == "4":
        mensagem = limparFeitas()
    elif opcao == "0":
        mensagem = ""
    else:
        mensagem = erro("Opção inválida. Use 1, 2, 3, 4 ou 0")

print("\n" + COR_TITULO + "✦ Até logo! ✦" + RESET + "\n")
