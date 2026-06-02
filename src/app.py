import json
import pandas as pd
import requests
import streamlit as st

# ========== CONFIGURAÇÃO ==========

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# ========== CARREGAR DADOS ==========

# JSON
usuarios = json.load(open("data/usuarios.json", encoding="utf-8"))

metas_financeiras = json.load(
    open("data/metas_financeiras.json", encoding="utf-8")
)

assinaturas = json.load(
    open("data/assinaturas.json", encoding="utf-8")
)

alertas_financeiros = json.load(
    open("data/alertas_financeiros.json", encoding="utf-8")
)

# CSV
transacoes = pd.read_csv("data/transacoes.csv")

orcamentos = pd.read_csv("data/orcamentos.csv")

parcelamentos = pd.read_csv("data/parcelamentos.csv")

relatorios_mensais = pd.read_csv("data/relatorios_mensais.csv")

# =========================
# EXEMPLO DE UTILIZAÇÃO
# =========================

print("Usuários carregados:")
print(usuarios)

print("\nTransações:")
print(transacoes.head())

print("\nMetas financeiras:")
print(metas_financeiras)

print("\nOrçamentos:")
print(orcamentos)

# =========================
# EXEMPLO DE CONTEXTO
# =========================

contexto_usuario = {
    "dados_usuario": {
        "nome": "Carlos Silva",
        "perfil_financeiro": "Moderado",
        "renda_mensal": 4500.00,
        "objetivo_principal": "Economizar",
        "saldo_atual": 2930.60
    },

    "metas_financeiras": [
        {
            "objetivo": "Comprar notebook",
            "valor_atual": 1800.00,
            "valor_meta": 4500.00
        },
        {
            "objetivo": "Reserva de emergência",
            "valor_atual": 3200.00,
            "valor_meta": 10000.00
        }
    ],

    "ultimas_transacoes": [
        {
            "data": "02/05",
            "descricao": "Aluguel",
            "valor": -1500.00
        },
        {
            "data": "03/05",
            "descricao": "Supermercado",
            "valor": -320.50
        },
        {
            "data": "05/05",
            "descricao": "Cinema",
            "valor": -45.00
        },
        {
            "data": "07/05",
            "descricao": "Projeto freelancer",
            "valor": 800.00
        }
    ],

    "orcamentos": [
        {
            "categoria": "Alimentação",
            "valor_gasto": 540.00,
            "limite": 600.00
        },
        {
            "categoria": "Lazer",
            "valor_gasto": 180.00,
            "limite": 300.00
        }
    ],

    "alertas": [
        "Você gastou 35% a mais com alimentação este mês.",
        "Sua assinatura da Netflix vence em 3 dias."
    ]
}

# =========================
# SYSTEM PROMPT
# =========================


SYSTEM_PROMPT = """
Você é o Nexo Finance, um agente financeiro inteligente especializado em organização financeira pessoal.
Seu objetivo é auxiliar usuários comuns no controle de gastos, planejamento financeiro e criação de hábitos financeiros saudáveis de maneira simples, acessível e personalizada.
Você deve agir como um assistente consultivo, educativo e proativo, ajudando o usuário a entender sua situação financeira sem utilizar linguagem excessivamente técnica.

REGRAS:

1. Sempre baseie suas respostas nos dados fornecidos pelos arquivos JSON e CSV disponíveis no contexto.
2. Nunca invente informações financeiras, valores, transações ou metas que não estejam presentes nos dados.
3. Caso não possua informações suficientes para responder corretamente, informe claramente a limitação e solicite mais dados ao usuário.
4. Utilize linguagem simples, clara e acessível para facilitar o entendimento de usuários sem conhecimento financeiro avançado.
5. Gere análises financeiras personalizadas com base em:
   - transações
   - metas financeiras
   - orçamentos
   - assinaturas
   - parcelamentos
   - alertas financeiros
6. Identifique padrões de gastos excessivos e informe o usuário de forma educativa e preventiva.
7. Incentive hábitos financeiros saudáveis, como:
   - controle de despesas
   - planejamento financeiro
   - criação de reserva de emergência
   - acompanhamento de metas
8. Nunca forneça recomendações de investimento avançadas ou definitivas sem informações completas sobre perfil financeiro e tolerância a risco.
9. Nunca realize operações bancárias, transferências ou transações financeiras.
10. Priorize privacidade e segurança dos dados financeiros do usuário.
11. Quando possível, apresente:
   - resumos financeiros
   - alertas de gastos
   - comparações mensais
   - sugestões de economia
   - acompanhamento de metas
12. Mantenha comportamento profissional, amigável e organizado durante toda a interação.

EXEMPLOS DE COMPORTAMENTO:

- Informar gastos acima do orçamento mensal.
- Alertar sobre assinaturas recorrentes.
- Sugerir redução de despesas não essenciais.
- Mostrar evolução das metas financeiras.
- Explicar relatórios financeiros de forma simples.

LIMITAÇÕES:

- Você não substitui consultoria financeira profissional.
- Você depende exclusivamente dos dados fornecidos no contexto.
- Você pode apresentar limitações em análises com dados incompletos.
- Você não possui acesso automático a contas bancárias externas.
"""

# ========== CHAMAR NEXO FINANCE ==========

def perguntar(msg):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO FINANCEIRO:
{contexto_usuario}

Pergunta do usuário:
{msg}
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    return resposta.json()["response"]

# ========== INTERFACE NEXO FINANCE ==========

st.title("💰 Nexo Finance")

st.write("Seu agente de organização financeira pessoal.")

if pergunta := st.chat_input("Digite sua dúvida financeira..."):

    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando suas finanças..."):

        resposta = perguntar(pergunta)

        print(repr(resposta))
        st.chat_message("assistant").write(resposta)
