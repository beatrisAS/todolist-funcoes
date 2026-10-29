<h1 align="center">✦ To-Do List no Terminal ✦</h1>

<p align="center">
  Uma lista de tarefas colorida feita em <b>Python</b>,<br>
  criada para praticar <b>funções</b> no Bootcamp de Análise de Dados da <b>Generation Brasil</b>.
</p>

---

## 📸 Visual

```
╭──────────────────────────────────────────────╮
│             ✦  MINHAS TAREFAS  ✦             │
├──────────────────────────────────────────────┤
│ ✔  1 │ Estudar funções                       │
│ ○  2 │ Fazer exercícios                      │
├──────────────────────────────────────────────┤
│ 1 › Adicionar       2 › Concluir/desfazer    │
│ 3 › Remover         4 › Limpar feitas        │
│ 0 › Sair                                     │
╰──────────────────────────────────────────────╯
  ✔ Tarefa concluída. Mandou bem!
```

No terminal, as cores aparecem de verdade: borda cinza, título em magenta, números do menu em ciano, tarefas concluídas em cinza e riscadas.

## ✨ Funcionalidades

- ➕ Adicionar tarefas
- ✔ Marcar como concluída (ou desfazer)
- 🗑 Remover tarefas
- 🧹 Limpar todas as tarefas concluídas de uma vez
- 💬 Mensagens coloridas de sucesso, erro e aviso
- 🛡 Entradas validadas: letras no lugar de números, número que não existe e nome vazio não quebram o programa

## 🚀 Como rodar

Você só precisa do **Python 3.6 ou superior**. Não há nada para instalar.

```bash
git clone https://github.com/beatrisAS/todolist-funcoes.git
cd todolist-funcoes
python todolist.py
```

> 💡 Use o terminal do VS Code ou o Windows Terminal para ver as cores e os símbolos corretamente.

## 🎮 Como usar

| Tecla | O que faz |
|:---:|---|
| `1` | Adicionar uma tarefa (digite o nome) |
| `2` | Concluir ou desfazer (digite o número da tarefa) |
| `3` | Remover (digite o número da tarefa) |
| `4` | Limpar todas as tarefas concluídas |
| `0` | Sair |

## 🧠 O que este projeto pratica sobre funções

Cada função faz **uma coisa só**. Veja onde cada conceito aparece no `todolist.py`:

| Conceito | Onde ver |
|---|---|
| Função simples, sem parâmetro | `topo()`, `divisoria()`, `base()` |
| **Parâmetros** | `linhaCaixa(conteudo, tamanho)`, `cortar(texto, limite)` |
| Parâmetros com **valor padrão** | `linhaMenu(tecla1, texto1, tecla2="", texto2="")` |
| **`return`** (devolver um valor) | `sucesso()`, `erro()`, `aviso()`, `cortar()`, `lerNumero()` |
| Função que **chama outras funções** | `mostrarTela()` chama `topo()`, `linhaCaixa()`, `linhaMenu()`... |
| `try/except` dentro de função | `lerNumero()` devolve `None` se a pessoa digitar letras |
| Funções que **devolvem mensagens** para o programa principal | `adicionarTarefa()`, `concluirTarefa()`, `removerTarefa()`, `limparFeitas()` |

## 🎨 Como personalizar

As cores e o tamanho ficam no topo do `todolist.py`:

```python
LARGURA = 48                          # largura da caixa
COR_BORDA = FRENTE_CINZA              # cor da borda
COR_DESTAQUE = FRENTE_CIANO_CLARO     # cor dos números e símbolos
COR_TITULO = FRENTE_MAGENTA_CLARO     # cor do título
```

Troque pelo nome de qualquer cor do `cores.py`, por exemplo `FRENTE_AZUL_CLARO` ou `FRENTE_VERDE_CLARO`. Para ver todas as cores e estilos disponíveis, rode:

```bash
python cores.py
```

Se aparecer `?` no lugar dos símbolos (`✔ ○ ✦ › │`), é a fonte do seu terminal. Troque por caracteres simples, como `v`, `o`, `*`, `>` e `|`.

## 📁 Estrutura

```
todolist-funcoes/
├── todolist.py    # o programa (funções + loop principal)
├── cores.py       # constantes de cores e estilos (códigos ANSI)
└── README.md
```

## 🔭 Ideias para evoluir

- [ ] Salvar as tarefas em um arquivo (hoje elas somem ao fechar o programa)
- [ ] Limpar a tela a cada volta do menu
- [ ] Adicionar prioridade (alta, média, baixa) com cores
- [ ] Editar o nome de uma tarefa
- [ ] Mostrar uma barra de progresso

## 👩‍💻 Autoria

Feito por **Beatris Antunes Silva** durante o Bootcamp de Análise de Dados da **Generation Brasil**.
