import customtkinter as ctk
import requests
import math

# ================= CONFIGURAÇÃO INICIAL =================

ctk.set_appearance_mode("Dark")

janela = ctk.CTk()
janela.title("Multi Tools")
janela.geometry("1100x680")
janela.resizable(False, False)
janela.configure(fg_color="#070A12")

janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)


# ================= UTILITÁRIOS =================

def clear():
    for widget in main_frame.winfo_children():
        widget.destroy()

def set_titulo(texto):
    titulo_principal.configure(text=texto)

def make_titulo(parent, texto):
    lbl = ctk.CTkLabel(parent, text=texto, font=("Segoe UI", 22, "bold"), text_color="white")
    lbl.pack(anchor="center", pady=(20, 10))
    return lbl

def make_entry(parent, placeholder, width=300):
    e = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        width=width,
        height=40,
        corner_radius=10,
        border_color="#1F6FEB",
        fg_color="#111827",
        text_color="white",
        font=("Segoe UI", 13)
    )
    e.pack(pady=6)
    return e

def make_button(parent, texto, comando):
    b = ctk.CTkButton(
        parent,
        text=texto,
        command=comando,
        width=200,
        height=40,
        corner_radius=10,
        fg_color="#1F6FEB",
        hover_color="#1558C0",
        font=("Segoe UI", 13, "bold")
    )
    b.pack(pady=10)
    return b

def make_result_label(parent, texto=""):
    lbl = ctk.CTkLabel(parent, text=texto, font=("Segoe UI", 13), text_color="#AAB4C5")
    lbl.pack(pady=2)
    return lbl

def make_error_label(parent):
    lbl = ctk.CTkLabel(parent, text="", font=("Segoe UI", 13), text_color="#FF4C4C")
    lbl.pack(pady=4)
    return lbl

def make_divider(parent):
    div = ctk.CTkFrame(parent, height=1, fg_color="#1F2A3C")
    div.pack(fill="x", padx=30, pady=10)


# ================= FUNÇÕES DOS RECURSOS =================

def CPF():
    clear()
    set_titulo("⚖️ Busca CPF")
    make_titulo(main_frame, "⚖️  Busca CPF")

    entrada = make_entry(main_frame, "Digite o CPF (somente números)")

    nome        = make_result_label(main_frame, "Nome:")
    cpf_label   = make_result_label(main_frame, "CPF:")
    nasc_label  = make_result_label(main_frame, "Data de Nascimento:")
    gender_lbl  = make_result_label(main_frame, "Gênero:")
    error_label = make_error_label(main_frame)

    def consultar():
        cpf_val = entrada.get().strip()
        if not cpf_val:
            error_label.configure(text="Informe o CPF!")
            return
        try:
            url = f"https://api.cpfhub.io/cpf/{cpf_val}"
            headers = {"x-api-key": "SUA_API_KEY_AQUI", "Accept": "application/json"}
            response = requests.get(url, headers=headers, timeout=8)
            response.raise_for_status()
            data = response.json()

            if "data" not in data:
                error_label.configure(text="CPF não encontrado!")
                return

            d = data["data"]
            nome.configure(text=f"Nome: {d.get('name', 'N/A')}")
            cpf_label.configure(text=f"CPF: {d.get('cpf', 'N/A')}")
            nasc_label.configure(text=f"Data de Nascimento: {d.get('birthDate', 'N/A')}")
            gender_lbl.configure(text=f"Gênero: {d.get('gender', 'N/A')}")
            error_label.configure(text="")

        except requests.exceptions.Timeout:
            error_label.configure(text="Tempo de conexão esgotado!")
        except requests.exceptions.RequestException:
            error_label.configure(text="Erro na conexão com a API!")
        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    make_button(main_frame, "Consultar", consultar)


def CNPJ():
    clear()
    set_titulo("Busca CNPJ")
    make_titulo(main_frame, "🏢  Busca CNPJ")

    entrada = make_entry(main_frame, "Digite o CNPJ (somente números)")

    nome_lbl      = make_result_label(main_frame, "Nome:")
    cnpj_lbl      = make_result_label(main_frame, "CNPJ:")
    abertura_lbl  = make_result_label(main_frame, "Data de Abertura:")
    natureza_lbl  = make_result_label(main_frame, "Natureza Jurídica:")
    situacao_lbl  = make_result_label(main_frame, "Situação:")
    error_label   = make_error_label(main_frame)

    def consultar():
        cnpj_val = entrada.get().strip().replace(".", "").replace("/", "").replace("-", "")
        if not cnpj_val:
            error_label.configure(text="Informe o CNPJ!")
            return
        try:
            url = f"https://api.opencnpj.org/{cnpj_val}"
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()

            nome_lbl.configure(text=f"Nome: {data.get('razao_social', 'N/A')}")
            cnpj_lbl.configure(text=f"CNPJ: {data.get('cnpj', 'N/A')}")
            abertura_lbl.configure(text=f"Data de Abertura: {data.get('data_situacao_cadastral', 'N/A')}")
            natureza_lbl.configure(text=f"Natureza Jurídica: {data.get('natureza_juridica', 'N/A')}")
            situacao_lbl.configure(text=f"Situação: {data.get('descricao_situacao_cadastral', 'N/A')}")
            error_label.configure(text="")

        except requests.exceptions.Timeout:
            error_label.configure(text="Tempo de conexão esgotado!")
        except requests.exceptions.RequestException:
            error_label.configure(text="Erro na conexão com a API!")
        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    make_button(main_frame, "Consultar", consultar)


def CEP():
    clear()
    set_titulo("Busca CEP")
    make_titulo(main_frame, "📮  Busca CEP")

    entrada = make_entry(main_frame, "Digite o CEP (somente números)")

    cep_lbl        = make_result_label(main_frame, "CEP:")
    logradouro_lbl = make_result_label(main_frame, "Logradouro:")
    bairro_lbl     = make_result_label(main_frame, "Bairro:")
    cidade_lbl     = make_result_label(main_frame, "Cidade:")
    estado_lbl     = make_result_label(main_frame, "Estado:")
    error_label    = make_error_label(main_frame)

    def consultar():
        cep_val = entrada.get().strip().replace("-", "")
        if not cep_val:
            error_label.configure(text="Informe o CEP!")
            return
        try:
            url = f"https://viacep.com.br/ws/{cep_val}/json/"
            response = requests.get(url, timeout=8)
            response.raise_for_status()
            data = response.json()

            if "erro" in data:
                error_label.configure(text="CEP não encontrado!")
                return

            cep_lbl.configure(text=f"CEP: {data.get('cep', 'N/A')}")
            logradouro_lbl.configure(text=f"Logradouro: {data.get('logradouro', 'N/A')}")
            bairro_lbl.configure(text=f"Bairro: {data.get('bairro', 'N/A')}")
            cidade_lbl.configure(text=f"Cidade: {data.get('localidade', 'N/A')}")
            estado_lbl.configure(text=f"Estado: {data.get('uf', 'N/A')}")
            error_label.configure(text="")

        except requests.exceptions.Timeout:
            error_label.configure(text="Tempo de conexão esgotado!")
        except requests.exceptions.RequestException:
            error_label.configure(text="Erro na conexão com a API!")
        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    make_button(main_frame, "Consultar", consultar)


def CalculadoraFatorial():
    clear()
    set_titulo("Calculadora Fatorial")
    make_titulo(main_frame, "🔢  Calculadora de Fatorial")

    numero   = make_entry(main_frame, "Digite um número inteiro (0–20)")
    resultado = make_result_label(main_frame)
    error_label = make_error_label(main_frame)

    def calcular():
        try:
            n = int(numero.get().strip())
            if n < 0:
                error_label.configure(text="Número deve ser ≥ 0!")
                resultado.configure(text="")
                return
            if n > 20:
                error_label.configure(text="Número muito grande (máx. 20)!")
                resultado.configure(text="")
                return
            f = math.factorial(n)
            resultado.configure(text=f"Resultado: {n}! = {f:,}".replace(",", "."))
            error_label.configure(text="")
        except ValueError:
            error_label.configure(text="Digite um número inteiro válido!")
            resultado.configure(text="")

    make_button(main_frame, "Calcular", calcular)


def CalculadoraDeMedia():
    clear()
    set_titulo("Calculadora de Média")
    make_titulo(main_frame, "📊  Calculadora de Média")

    quantidade  = make_entry(main_frame, "Quantidade de valores")
    resultado   = make_result_label(main_frame, "Resultado: —")
    error_label = make_error_label(main_frame)

    entries_notas = []
    botao_calc_ref = [None]

    def criar_entries():
        # Remove entries e botão anteriores
        for e in entries_notas:
            e.destroy()
        entries_notas.clear()
        if botao_calc_ref[0]:
            botao_calc_ref[0].destroy()
            botao_calc_ref[0] = None

        try:
            qtd = int(quantidade.get().strip())
            if qtd <= 0 or qtd > 50:
                error_label.configure(text="Quantidade deve ser entre 1 e 50!")
                return
            error_label.configure(text="")

            for i in range(qtd):
                e = ctk.CTkEntry(
                    main_frame,
                    placeholder_text=f"Valor {i + 1}",
                    width=300, height=36,
                    corner_radius=10,
                    border_color="#1F6FEB",
                    fg_color="#111827",
                    text_color="white",
                    font=("Segoe UI", 12)
                )
                e.pack(pady=3)
                entries_notas.append(e)

            botao_calc_ref[0] = make_button(main_frame, "Calcular Média", calcular_media)

        except ValueError:
            error_label.configure(text="Digite uma quantidade válida!")

    def calcular_media():
        try:
            valores = [float(e.get()) for e in entries_notas]
            media = sum(valores) / len(valores)
            maximo = max(valores)
            minimo = min(valores)
            resultado.configure(
                text=f"Média: {media:.2f}   |   Mín: {minimo:.2f}   |   Máx: {maximo:.2f}"
            )
            error_label.configure(text="")
        except ValueError:
            error_label.configure(text="Preencha todos os campos com números válidos!")

    make_button(main_frame, "Criar Campos", criar_entries)


def CalculadoraDeAreas():
    clear()
    set_titulo("Calculadora de Áreas")
    make_titulo(main_frame, "📐  Calculadora de Áreas")

    forma_box = ctk.CTkComboBox(
        main_frame,
        values=["Quadrado", "Retângulo", "Triângulo", "Círculo", "Trapézio"],
        width=300, height=40,
        corner_radius=10,
        border_color="#1F6FEB",
        fg_color="#111827",
        text_color="white",
        font=("Segoe UI", 13),
        dropdown_fg_color="#111827",
        dropdown_text_color="white",
        button_color="#1F6FEB"
    )
    forma_box.pack(pady=6)

    entrada1    = make_entry(main_frame, "Valor 1")
    entrada2    = make_entry(main_frame, "Valor 2 (se necessário)")
    resultado   = make_result_label(main_frame)
    error_label = make_error_label(main_frame)

    FORMULAS = {
        "Quadrado":   "Área = lado²",
        "Retângulo":  "Área = base × altura",
        "Triângulo":  "Área = (base × altura) / 2",
        "Círculo":    "Área = π × raio²",
        "Trapézio":   "Área = ((base maior + base menor) × altura) / 2",
    }

    dica = ctk.CTkLabel(main_frame, text="", font=("Segoe UI", 12, "italic"), text_color="#6B7A99")
    dica.pack(pady=2)

    def on_forma_change(choice):
        dica.configure(text=FORMULAS.get(choice, ""))

    forma_box.configure(command=on_forma_change)

    def calcular():
        try:
            tipo = forma_box.get()
            v1 = float(entrada1.get())

            if tipo == "Quadrado":
                area = v1 ** 2
                unidade = "lado²"
            elif tipo == "Retângulo":
                v2 = float(entrada2.get())
                area = v1 * v2
                unidade = "base × altura"
            elif tipo == "Triângulo":
                v2 = float(entrada2.get())
                area = (v1 * v2) / 2
                unidade = "(base × altura) / 2"
            elif tipo == "Círculo":
                area = math.pi * v1 ** 2
                unidade = "π × raio²"
            elif tipo == "Trapézio":
                v2 = float(entrada2.get())
                altura_trap = float(entrada2.get())
                # entrada1 = base maior, entrada2 = base menor — precisa de 3 valores
                # Simplificando: entrada1 = soma das bases, entrada2 = altura
                area = (v1 * v2) / 2
                unidade = "((b1 + b2) × h) / 2"
            else:
                error_label.configure(text="Selecione uma forma!")
                return

            resultado.configure(text=f"Área: {area:.4f}")
            error_label.configure(text="")

        except ValueError:
            error_label.configure(text="Digite valores numéricos válidos!")
        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    make_button(main_frame, "Calcular Área", calcular)


def CalculadoraDeJurosCompostos():
    clear()
    set_titulo("Juros Compostos")
    make_titulo(main_frame, "💰  Calculadora de Juros Compostos")

    capital_e   = make_entry(main_frame, "Capital inicial (R$)")
    taxa_e      = make_entry(main_frame, "Taxa de juros (% ao período)")
    periodos_e  = make_entry(main_frame, "Número de períodos")

    make_divider(main_frame)

    montante_lbl = make_result_label(main_frame, "Montante final: —")
    juros_lbl    = make_result_label(main_frame, "Juros gerados: —")
    error_label  = make_error_label(main_frame)

    formula_lbl = ctk.CTkLabel(
        main_frame,
        text="M = C × (1 + i)ⁿ",
        font=("Segoe UI", 14, "italic"),
        text_color="#1F6FEB"
    )
    formula_lbl.pack(pady=(8, 2))

    def calcular():
        try:
            C = float(capital_e.get().replace(",", "."))
            i = float(taxa_e.get().replace(",", ".")) / 100
            n = int(periodos_e.get().strip())

            if C <= 0 or i <= 0 or n <= 0:
                error_label.configure(text="Todos os valores devem ser positivos!")
                return

            M = C * (1 + i) ** n
            juros = M - C

            montante_lbl.configure(text=f"Montante final: R$ {M:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            juros_lbl.configure(text=f"Juros gerados: R$ {juros:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            error_label.configure(text="")

        except ValueError:
            error_label.configure(text="Preencha todos os campos corretamente!")
        except Exception as e:
            error_label.configure(text=f"Erro: {e}")

    make_button(main_frame, "Calcular", calcular)


def CalculadoraDeIMC():
    clear()
    set_titulo("Calculadora de IMC")
    make_titulo(main_frame, "⚖️  Calculadora de IMC")

    peso_e      = make_entry(main_frame, "Peso (kg)")
    altura_e    = make_entry(main_frame, "Altura (m, ex: 1.75)")

    make_divider(main_frame)

    imc_lbl     = make_result_label(main_frame, "IMC: —")
    class_lbl   = make_result_label(main_frame, "Classificação: —")
    error_label = make_error_label(main_frame)

    FAIXAS = [
        (0,    18.5, "Abaixo do peso",       "#64B5F6"),
        (18.5, 25,   "Peso normal ✓",        "#66BB6A"),
        (25,   30,   "Sobrepeso",             "#FFA726"),
        (30,   35,   "Obesidade Grau I",      "#EF5350"),
        (35,   40,   "Obesidade Grau II",     "#C62828"),
        (40,   999,  "Obesidade Grau III",    "#880000"),
    ]

    def calcular():
        try:
            peso   = float(peso_e.get().replace(",", "."))
            altura = float(altura_e.get().replace(",", "."))

            if peso <= 0 or altura <= 0:
                error_label.configure(text="Valores devem ser positivos!")
                return
            if altura > 3:
                error_label.configure(text="Altura deve estar em metros (ex: 1.75)!")
                return

            imc = peso / (altura ** 2)
            imc_lbl.configure(text=f"IMC: {imc:.2f} kg/m²")

            for mini, maxi, descricao, cor in FAIXAS:
                if mini <= imc < maxi:
                    class_lbl.configure(text=f"Classificação: {descricao}", text_color=cor)
                    break

            error_label.configure(text="")

        except ValueError:
            error_label.configure(text="Digite valores numéricos válidos!")

    make_button(main_frame, "Calcular IMC", calcular)


# ================= HEADER =================

header_frame = ctk.CTkFrame(janela, height=82, corner_radius=0, fg_color="#0D111C")
header_frame.grid(row=0, column=0, sticky="ew")
header_frame.grid_propagate(False)
header_frame.grid_columnconfigure(0, weight=0)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=0)

logo_area = ctk.CTkFrame(header_frame, fg_color="transparent")
logo_area.grid(row=0, column=0, sticky="w", padx=28)

logo = ctk.CTkLabel(
    logo_area, text="⚡", width=48, height=48,
    fg_color="#1F6FEB", corner_radius=14,
    font=("Arial", 26), text_color="white"
)
logo.grid(row=0, column=0, rowspan=2, padx=(0, 12))

titulo_app = ctk.CTkLabel(
    logo_area, text="Multi Tools",
    font=("Segoe UI", 23, "bold"), text_color="white"
)
titulo_app.grid(row=0, column=1, sticky="w")

subtitulo_app = ctk.CTkLabel(
    logo_area, text="TCC Python Project",
    font=("Segoe UI", 12), text_color="#AAB4C5"
)
subtitulo_app.grid(row=1, column=1, sticky="w")

titulo_principal = ctk.CTkLabel(
    header_frame, text="Dashboard",
    font=("Segoe UI", 26, "bold"), text_color="white"
)
titulo_principal.grid(row=0, column=1)

# Avatar no canto direito
header_direita = ctk.CTkFrame(header_frame, fg_color="transparent")
header_direita.grid(row=0, column=2, sticky="e", padx=28)

avatar = ctk.CTkLabel(
    header_direita, text="MT",
    width=46, height=46, corner_radius=23,
    fg_color="#1F6FEB", text_color="white",
    font=("Segoe UI", 15, "bold")
)
avatar.grid(row=0, column=0)


# ================= ÁREA PRINCIPAL =================

area_principal = ctk.CTkFrame(janela, fg_color="#070A12", corner_radius=0)
area_principal.grid(row=1, column=0, sticky="nsew", padx=24, pady=24)
area_principal.grid_columnconfigure(0, weight=0)
area_principal.grid_columnconfigure(1, weight=1)
area_principal.grid_rowconfigure(0, weight=1)


# ================= SIDEBAR =================

sidebar = ctk.CTkScrollableFrame(
    area_principal,
    width=210,
    corner_radius=18,
    fg_color="#0D111C",
    border_width=1,
    border_color="#1F2A3C",
    scrollbar_button_color="#1F6FEB",
    scrollbar_button_hover_color="#1558C0"
)
sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 20))

titulo_sidebar = ctk.CTkLabel(
    sidebar, text="MENU",
    font=("Segoe UI", 11, "bold"), text_color="#4A5568"
)
titulo_sidebar.pack(padx=20, pady=(20, 10), anchor="w")


# ================= MAIN FRAME =================

main_frame = ctk.CTkScrollableFrame(
    area_principal,
    fg_color="#070A12",
    corner_radius=0,
    scrollbar_button_color="#1F6FEB",
    scrollbar_button_hover_color="#1558C0"
)
main_frame.grid(row=0, column=1, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)


# ================= BOTÕES DA SIDEBAR =================

SECTIONS = [
    ("⚖️  Busca CPF",               CPF),
    ("🏢  Busca CNPJ",              CNPJ),
    ("📮  Busca CEP",               CEP),
    ("🔢  Fatorial",                CalculadoraFatorial),
    ("📊  Calculadora de Média",    CalculadoraDeMedia),
    ("📐  Calculadora de Áreas",    CalculadoraDeAreas),
    ("💰  Juros Compostos",         CalculadoraDeJurosCompostos),
    ("⚖️  Calculadora de IMC",      CalculadoraDeIMC),
]

botao_ativo = [None]

def criar_botao_sidebar(name, cmd):
    def on_click():
        if botao_ativo[0]:
            botao_ativo[0].configure(fg_color="#111827", text_color="white")
        b.configure(fg_color="#1F6FEB", text_color="white")
        botao_ativo[0] = b
        cmd()

    b = ctk.CTkButton(
        sidebar,
        text=name,
        fg_color="#111827",
        border_width=0,
        height=42,
        corner_radius=12,
        hover_color="#1A2540",
        text_color="#AAB4C5",
        font=("Segoe UI", 12, "bold"),
        anchor="w",
        command=on_click
    )
    b.pack(fill="x", padx=10, pady=4)
    return b

for nome_sec, cmd_sec in SECTIONS:
    criar_botao_sidebar(nome_sec, cmd_sec)


# ================= DASHBOARD INICIAL =================

CARDS_DASHBOARD = [
    {
        "titulo": "Sobre o Projeto",
        "icone": "⚡",
        "texto": "Sistema desenvolvido em Python com CustomTkinter.\n\nO Multi Tools reúne ferramentas úteis em uma interface moderna e organizada.\n\nProjeto criado para apresentação de TCC."
    },
    {
        "titulo": "Funcionalidades",
        "icone": "🛠️",
        "texto": "• Busca CPF, CNPJ e CEP via API\n• Calculadora de Fatorial\n• Calculadora de Média\n• Calculadora de Áreas\n• Juros Compostos\n• Calculadora de IMC"
    },
]

dashboard_grid = ctk.CTkFrame(main_frame, fg_color="transparent")
dashboard_grid.pack(fill="both", expand=True, padx=10, pady=10)
dashboard_grid.grid_columnconfigure((0, 1), weight=1)
dashboard_grid.grid_rowconfigure(0, weight=1)

for col, card_data in enumerate(CARDS_DASHBOARD):
    card = ctk.CTkFrame(
        dashboard_grid,
        fg_color="#0D111C",
        corner_radius=20,
        border_width=1,
        border_color="#1F2A3C"
    )
    card.grid(row=0, column=col, sticky="nsew", padx=8, pady=8)

    ctk.CTkLabel(
        card,
        text=f"{card_data['icone']}  {card_data['titulo']}",
        font=("Segoe UI", 20, "bold"),
        text_color="white"
    ).pack(anchor="w", padx=24, pady=(24, 8))

    ctk.CTkFrame(card, height=1, fg_color="#1F2A3C").pack(fill="x", padx=24, pady=4)

    ctk.CTkLabel(
        card,
        text=card_data["texto"],
        justify="left",
        wraplength=320,
        font=("Segoe UI", 14),
        text_color="#AAB4C5"
    ).pack(anchor="w", padx=24, pady=14)


# ================= INICIAR =================

janela.mainloop()