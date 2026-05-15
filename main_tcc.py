import customtkinter as ctk
from PIL import Image
import requests
import math


janela = ctk.CTk()
ctk.set_appearance_mode("Dark")


# ================= FUNÇÕES =================

def clear():
    for widget in main_frame.winfo_children():
        widget.destroy()


def trocar_tema():
    modo = ctk.get_appearance_mode()

    if modo == "Dark":
        ctk.set_appearance_mode("Light")
        janela.configure(fg_color="#F4F7FB")
        titulo_app.configure(text_color="#0D111C")
        header_frame.configure(fg_color="#FFFFFF")
        titulo_principal.configure(text_color="#000")
        subtitulo_app.configure(text_color="grey")
        area_principal.configure(fg_color="#F4F7FB")
        sidebar.configure(fg_color="#FFFFFF")
        main_frame.configure(fg_color="#F4F7FB")
        icon_label.configure(text="☀️")
    else:
        ctk.set_appearance_mode("Dark")
        janela.configure(fg_color="#070A12")
        header_frame.configure(fg_color="#0D111C")
        titulo_principal.configure(text_color="#f4f7fb")
        titulo_app.configure(text_color="white")
        subtitulo_app.configure(text_color="grey")
        area_principal.configure(fg_color="#070A12")
        sidebar.configure(fg_color="#0D111C")
        main_frame.configure(fg_color="#070A12")
        icon_label.configure(text="🌙")


# ================= FUNÇÕES DOS RECURSOS =================

def CPF():
    clear()
    titulo_principal.configure(text="Busca CPF")

    titulo = ctk.CTkLabel(main_frame, text="Busca CPF", font=("Segoe UI", 22, "bold"))
    titulo.pack(anchor="center", pady=20)

    def consultar():
        try:
            cpf = entrada.get()

            url = f"https://api.cpfhub.io/cpf/{cpf}"

            headers = {
                "x-api-key": "SUA_API_KEY_AQUI",
                "Accept": "application/json"
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            if "data" not in data:
                error_label.configure(text="CPF não encontrado!")
                return

            nome.configure(text=f"Nome: {data['data']['name']}")
            cpf_label.configure(text=f"CPF: {data['data']['cpf']}")
            data_nascimento.configure(text=f"Data de Nascimento: {data['data']['birthDate']}")
            gender.configure(text=f"Gênero: {data['data']['gender']}")
            error_label.configure(text="")

        except requests.exceptions.RequestException:
            error_label.configure(text="Erro na conexão com a API!")
        except KeyError:
            error_label.configure(text="Dados inválidos retornados pela API!")
        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    entrada = ctk.CTkEntry(main_frame, placeholder_text="Digite o CPF", width=300)
    entrada.pack(pady=10)

    consulta = ctk.CTkButton(main_frame, text="Consultar", command=consultar)
    consulta.pack(pady=10)

    nome = ctk.CTkLabel(main_frame, text="Nome: ", font=("Segoe UI", 13))
    nome.pack(padx=10)

    cpf_label = ctk.CTkLabel(main_frame, text="CPF: ", font=("Segoe UI", 13))
    cpf_label.pack(padx=10)

    data_nascimento = ctk.CTkLabel(main_frame, text="Data de Nascimento: ", font=("Segoe UI", 13))
    data_nascimento.pack(padx=10)

    gender = ctk.CTkLabel(main_frame, text="Gênero: ", font=("Segoe UI", 13))
    gender.pack(padx=10)

    error_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 13), text_color="red")
    error_label.pack(padx=10)


def CNPJ():
    clear()
    titulo_principal.configure(text="Busca CNPJ")

    titulo = ctk.CTkLabel(main_frame, text="Busca CNPJ", font=("Segoe UI", 22, "bold"))
    titulo.pack(anchor="center", pady=20)

    def consultar():
        try:
            cnpj = entrada.get()
            url = f"https://api.opencnpj.org/{cnpj}"
            response = requests.get(url)
            data = response.json()

            nome.configure(text=f"Nome: {data['razao_social']}")
            cnpj_label.configure(text=f"CNPJ: {data['cnpj']}")
            data_abertura.configure(text=f"Data de Abertura: {data['data_situacao_cadastral']}")
            natureza_juridica.configure(text=f"Natureza Jurídica: {data['natureza_juridica']}")
            error_label.configure(text="")

        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    entrada = ctk.CTkEntry(main_frame, placeholder_text="Digite o CNPJ", width=300)
    entrada.pack(pady=10)

    consulta = ctk.CTkButton(main_frame, text="Consultar", command=consultar)
    consulta.pack(pady=10)

    nome = ctk.CTkLabel(main_frame, text="Nome: ", font=("Segoe UI", 13))
    nome.pack(padx=10)

    cnpj_label = ctk.CTkLabel(main_frame, text="CNPJ: ", font=("Segoe UI", 13))
    cnpj_label.pack(padx=10)

    data_abertura = ctk.CTkLabel(main_frame, text="Data de Abertura: ", font=("Segoe UI", 13))
    data_abertura.pack(padx=10)

    natureza_juridica = ctk.CTkLabel(main_frame, text="Natureza Jurídica: ", font=("Segoe UI", 13))
    natureza_juridica.pack(padx=10)

    error_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 13), text_color="red")
    error_label.pack(padx=10)


def CEP():
    clear()
    titulo_principal.configure(text="Busca CEP")

    def consultarCEP():
        try:
            cep = entrada.get()
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)
            data = response.json()

            cep_label.configure(text=f"CEP: {data['cep']}")
            logradouro_label.configure(text=f"Logradouro: {data['logradouro']}")
            bairro_label.configure(text=f"Bairro: {data['bairro']}")
            estado_label.configure(text=f"Estado: {data['uf']}")
            error_label.configure(text="")

        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    titulo = ctk.CTkLabel(main_frame, text="Busca CEP", font=("Segoe UI", 22, "bold"))
    titulo.pack(anchor="center", pady=20)

    entrada = ctk.CTkEntry(main_frame, placeholder_text="Digite o CEP", width=300)
    entrada.pack(pady=10)

    consultar = ctk.CTkButton(main_frame, text="Consultar", command=consultarCEP)
    consultar.pack(pady=10)

    cep_label = ctk.CTkLabel(main_frame, text="CEP: ", font=("Segoe UI", 13))
    cep_label.pack(padx=10)

    logradouro_label = ctk.CTkLabel(main_frame, text="Logradouro: ", font=("Segoe UI", 13))
    logradouro_label.pack(padx=10)

    bairro_label = ctk.CTkLabel(main_frame, text="Bairro: ", font=("Segoe UI", 13))
    bairro_label.pack(padx=10)

    estado_label = ctk.CTkLabel(main_frame, text="Estado: ", font=("Segoe UI", 13))
    estado_label.pack(padx=10)

    error_label = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 13), text_color="red")
    error_label.pack(padx=10)


def CalculadoraFatorial():
    clear()
    titulo_principal.configure(text="Calculadora Fatorial")

    def fatorial():
        try:
            n = int(numero.get())
            f = 1

            for i in range(1, n + 1):
                f *= i

            resultado.configure(text=f"Resultado: {f}")

        except Exception:
            resultado.configure(text="Digite um número válido!")

    titulo = ctk.CTkLabel(main_frame, text="Calculadora de Fatorial", font=("Segoe UI", 22, "bold"))
    titulo.pack(pady=20)

    numero = ctk.CTkEntry(main_frame, placeholder_text="Digite um número", width=300)
    numero.pack(pady=10)

    botao_fatorial = ctk.CTkButton(main_frame, text="Calcular Fatorial", command=fatorial)
    botao_fatorial.pack(pady=10)

    resultado = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 13))
    resultado.pack(padx=10)


def CalculadoraDeMedia():
    clear()
    titulo_principal.configure(text="Calculadora de Média")

    entries_notas = []

    titulo = ctk.CTkLabel(main_frame, text="Calculadora de Média", font=("Segoe UI", 22, "bold"))
    titulo.pack(pady=20)

    quantidade = ctk.CTkEntry(main_frame, placeholder_text="Digite a quantidade de valores", width=300)
    quantidade.pack(pady=10)

    resultado = ctk.CTkLabel(main_frame, text="Resultado:", font=("Segoe UI", 16))
    resultado.pack(padx=10, pady=10)

    def Media():
        try:
            soma = 0

            for entry in entries_notas:
                soma += float(entry.get())

            media = soma / len(entries_notas)
            resultado.configure(text=f"Resultado: {media:.2f}")

        except Exception:
            resultado.configure(text="Digite valores válidos!")

    def criar_entrys():
        for entry in entries_notas:
            entry.destroy()

        entries_notas.clear()

        try:
            qtd = int(quantidade.get())

            for i in range(qtd):
                entry = ctk.CTkEntry(main_frame, placeholder_text=f"Digite o valor {i + 1}", width=300)
                entry.pack(pady=5)
                entries_notas.append(entry)

            botao_media = ctk.CTkButton(main_frame, text="Calcular Média", command=Media)
            botao_media.pack(pady=10)

        except Exception:
            resultado.configure(text="Digite uma quantidade válida!")

    botao_criar = ctk.CTkButton(main_frame, text="Criar Entrys", command=criar_entrys)
    botao_criar.pack(pady=10)


def CalculadoraDeAreas():
    clear()
    titulo_principal.configure(text="Calculadora de Áreas")

    titulo = ctk.CTkLabel(main_frame, text="Calculadora de Áreas", font=("Segoe UI", 22, "bold"))
    titulo.pack(pady=20)

    entrada = ctk.CTkComboBox(main_frame, values=["Quadrado", "Retângulo", "Triângulo"], width=300)
    entrada.pack(pady=10)

    entrada1 = ctk.CTkEntry(main_frame, placeholder_text="Digite o valor 1", width=300)
    entrada1.pack(pady=10)

    entrada2 = ctk.CTkEntry(main_frame, placeholder_text="Digite o valor 2", width=300)
    entrada2.pack(pady=10)

    resultado = ctk.CTkLabel(main_frame, text="Resultado:", font=("Segoe UI", 16))
    resultado.pack(padx=10, pady=10)

    def Area():
        try:
            tipo = entrada.get()

            if tipo == "Quadrado":
                lado = float(entrada1.get())
                area = lado * lado

            elif tipo == "Retângulo":
                base = float(entrada1.get())
                altura = float(entrada2.get())
                area = base * altura

            elif tipo == "Triângulo":
                base = float(entrada1.get())
                altura = float(entrada2.get())
                area = (base * altura) / 2

            else:
                resultado.configure(text="Selecione uma forma!")
                return

            resultado.configure(text=f"Resultado: {area}")

        except Exception:
            resultado.configure(text="Digite valores válidos!")

    botao_area = ctk.CTkButton(main_frame, text="Calcular Área", command=Area)
    botao_area.pack(pady=10)


def CalculadoraDeJurosCompostos():
    clear()
    titulo_principal.configure(text="Juros Compostos")

    titulo = ctk.CTkLabel(main_frame, text="Calculadora de Juros Compostos", font=("Segoe UI", 22, "bold"))
    titulo.pack(pady=20)

    aviso = ctk.CTkLabel(main_frame, text="Função ainda não implementada.", font=("Segoe UI", 15))
    aviso.pack(pady=20)


def CalculadoraDeIMC():
    clear()
    titulo_principal.configure(text="Calculadora de IMC")

    def IMC():
        try:
            peso = float(entrada_peso.get())
            altura = float(entrada_altura.get())

            calculo = peso / (altura * altura)
            resultado.configure(text=f"Resultado: {calculo:.2f}")

            if calculo < 18.5:
                classificacao.configure(text="Classificação: Abaixo do peso")
            elif calculo < 25:
                classificacao.configure(text="Classificação: Peso normal")
            elif calculo < 30:
                classificacao.configure(text="Classificação: Sobrepeso")
            else:
                classificacao.configure(text="Classificação: Obesidade")

        except Exception:
            resultado.configure(text="Digite valores válidos!")
            classificacao.configure(text="Classificação:")

    titulo = ctk.CTkLabel(main_frame, text="Calculadora de IMC", font=("Segoe UI", 22, "bold"))
    titulo.pack(pady=20)

    entrada_peso = ctk.CTkEntry(main_frame, placeholder_text="Digite o peso", width=300)
    entrada_peso.pack(pady=10)

    entrada_altura = ctk.CTkEntry(main_frame, placeholder_text="Digite a altura", width=300)
    entrada_altura.pack(pady=10)

    botao_imc = ctk.CTkButton(main_frame, text="Calcular IMC", command=IMC)
    botao_imc.pack(pady=10)

    resultado = ctk.CTkLabel(main_frame, text="Resultado: ", font=("Segoe UI", 13))
    resultado.pack(padx=10)

    classificacao = ctk.CTkLabel(main_frame, text="Classificação: ", font=("Segoe UI", 13))
    classificacao.pack(padx=10)


# ================= CONFIGURAÇÃO =================

janela.title("TCC Python - Multi Tools")
janela.geometry("1100x680")
janela.resizable(False, False)
janela.configure(fg_color="#070A12")

janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)


# ================= HEADER =================

header_frame = ctk.CTkFrame(
    janela,
    height=82,
    corner_radius=0,
    fg_color="#0D111C"
)
header_frame.grid(row=0, column=0, sticky="ew")
header_frame.grid_propagate(False)

header_frame.grid_columnconfigure(0, weight=0)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=0)

logo_area = ctk.CTkFrame(header_frame, fg_color="transparent")
logo_area.grid(row=0, column=0, sticky="w", padx=28)

logo = ctk.CTkLabel(
    logo_area,
    text="⚡",
    width=48,
    height=48,
    fg_color="#1F6FEB",
    corner_radius=14,
    font=("Arial", 26),
    text_color="white"
)
logo.grid(row=0, column=0, rowspan=2, padx=(0, 12))

titulo_app = ctk.CTkLabel(
    logo_area,
    text="Multi Tools",
    font=("Segoe UI", 23, "bold"),
    text_color="white"
)
titulo_app.grid(row=0, column=1, sticky="w")

subtitulo_app = ctk.CTkLabel(
    logo_area,
    text="TCC Python Project",
    font=("Segoe UI", 12),
    text_color="#AAB4C5"
)
subtitulo_app.grid(row=1, column=1, sticky="w")

titulo_principal = ctk.CTkLabel(
    header_frame,
    text="Dashboard",
    font=("Segoe UI", 26, "bold"),
    text_color="white"
)
titulo_principal.grid(row=0, column=1)

header_direita = ctk.CTkFrame(header_frame, fg_color="transparent")
header_direita.grid(row=0, column=2, sticky="e", padx=28)

icon_label = ctk.CTkLabel(
    header_direita,
    text="🌙",
    font=("Arial", 22),
    text_color="white"
)
icon_label.grid(row=0, column=0, padx=(0, 10))

switch_tema = ctk.CTkSwitch(
    header_direita,
    text="",
    command=trocar_tema,
    width=45,
    progress_color="#1F6FEB"
)
switch_tema.grid(row=0, column=1, padx=(0, 18))

avatar = ctk.CTkLabel(
    header_direita,
    text="EP",
    width=46,
    height=46,
    corner_radius=23,
    fg_color="#1F6FEB",
    text_color="white",
    font=("Segoe UI", 15, "bold")
)
avatar.grid(row=0, column=2)


# ================= ÁREA PRINCIPAL =================

area_principal = ctk.CTkFrame(
    janela,
    fg_color="#070A12",
    corner_radius=0
)
area_principal.grid(row=1, column=0, sticky="nsew", padx=24, pady=24)

area_principal.grid_columnconfigure(0, weight=0)
area_principal.grid_columnconfigure(1, weight=1)
area_principal.grid_rowconfigure(0, weight=1)


# ================= SIDEBAR =================

sidebar = ctk.CTkFrame(
    area_principal,
    width=230,
    corner_radius=24,
    fg_color="#0D111C",
    border_width=1,
    border_color="#1F6FEB"
)
sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 22))
sidebar.grid_propagate(False)

titulo_sidebar = ctk.CTkLabel(
    sidebar,
    text="MENU",
    font=("Segoe UI", 13, "bold"),
    text_color="#AAB4C5"
)
titulo_sidebar.grid(row=0, column=0, padx=24, pady=(26, 14), sticky="w")


# ================= MAIN FRAME =================

main_frame = ctk.CTkFrame(
    area_principal,
    fg_color="#070A12",
    corner_radius=0
)
main_frame.grid(row=0, column=1, sticky="nsew")

main_frame.grid_columnconfigure((0, 1), weight=1)
main_frame.grid_rowconfigure(0, weight=1)


# ================= BOTÕES =================

sections = [
    ("Busca CPF", CPF),
    ("Busca CNPJ", CNPJ),
    ("Busca CEP", CEP),
    ("Calculadora Fatorial", CalculadoraFatorial),
    ("Calculadora de Média", CalculadoraDeMedia),
    ("Calculadora de Áreas", CalculadoraDeAreas),
    ("Calculadora de Juros Compostos", CalculadoraDeJurosCompostos),
    ("Calculadora de IMC", CalculadoraDeIMC)
]

for i, (name, cmd) in enumerate(sections, start=1):
    button = ctk.CTkButton(
        sidebar,
        text=name,
        fg_color="#111827",
        border_color="#1F6FEB",
        border_width=1,
        height=44,
        bg_color="transparent",
        corner_radius=14,
        width=180,
        hover_color="#1F6FEB",
        text_color="white",
        font=("Segoe UI", 13, "bold"),
        anchor="w",
        command=cmd
    )
    button.grid(row=i, column=0, padx=20, pady=6, sticky="ew")


# ================= DASHBOARD INICIAL =================

card_sobre = ctk.CTkFrame(
    main_frame,
    fg_color="#111827",
    corner_radius=24,
    border_width=1,
    border_color="#1F6FEB"
)
card_sobre.grid(row=0, column=0, sticky="nsew", padx=(0, 12), pady=10)

titulo_sobre = ctk.CTkLabel(
    card_sobre,
    text="Sobre",
    font=("Segoe UI", 26, "bold"),
    text_color="white"
)
titulo_sobre.pack(anchor="w", padx=26, pady=(26, 10))

texto_sobre = ctk.CTkLabel(
    card_sobre,
    text="""Sistema desenvolvido em Python com CustomTkinter.

O objetivo do Multi Tools é reunir várias ferramentas úteis em uma interface moderna, simples e organizada.

Projeto criado para apresentação de TCC.""",
    justify="left",
    wraplength=340,
    font=("Segoe UI", 15),
    text_color="#AAB4C5"
)
texto_sobre.pack(anchor="w", padx=26, pady=10)


card_conteudo = ctk.CTkFrame(
    main_frame,
    fg_color="#111827",
    corner_radius=24,
    border_width=1,
    border_color="#1F6FEB"
)
card_conteudo.grid(row=0, column=1, sticky="nsew", padx=(12, 0), pady=10)

titulo_conteudo = ctk.CTkLabel(
    card_conteudo,
    text="Conteúdo",
    font=("Segoe UI", 26, "bold"),
    text_color="white"
)
titulo_conteudo.pack(anchor="w", padx=26, pady=(26, 10))

texto_conteudo = ctk.CTkLabel(
    card_conteudo,
    text="""• Busca CPF
• Busca CNPJ
• Busca CEP
• Calculadora Fatorial
• Calculadora de Média
• Calculadora de Áreas
• Juros Compostos
• Calculadora de IMC""",
    justify="left",
    font=("Segoe UI", 15),
    text_color="#AAB4C5"
)
texto_conteudo.pack(anchor="w", padx=26, pady=10)


janela.mainloop()
