# Código da Aplicação

Esta pasta contém o código-fonte do agente **Nexo Finance**, desenvolvido para auxiliar usuários na organização financeira pessoal por meio de uma interface conversacional integrada a uma LLM local executada com Ollama.

## Estrutura Utilizada

```text
src/
├── app.py                     # Aplicação principal (Streamlit)
├── data/
│   ├── usuarios.json
│   ├── metas_financeiras.json
│   ├── assinaturas.json
│   ├── alertas_financeiros.json
│   ├── transacoes.csv
│   ├── orcamentos.csv
│   ├── parcelamentos.csv
│   └── relatorios_mensais.csv
├── requirements.txt
└── README.md
```

## Dependências Utilizadas

### requirements.txt

```text
streamlit
pandas
requests
```

## Pré-requisitos

* Python 3.10 ou superior
* Ollama instalado
* Modelo LLM baixado localmente (GPT-OSS ou equivalente)

Exemplo:

```bash
ollama pull gpt-oss:20b
```

## Como Rodar

### 1. Criar e ativar ambiente virtual

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Iniciar o Ollama

```bash
ollama serve
```

### 4. Executar a aplicação

```bash
streamlit run app.py
```

## Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* Requests
* Ollama
* GPT-OSS
* JSON
* CSV
