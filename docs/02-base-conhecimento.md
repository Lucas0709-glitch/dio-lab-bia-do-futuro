# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Nexo Finance |
|---------|---------|---------------------|
| `usuarios.json` | JSON | Armazenar informações básicas e perfil financeiro do usuário |
| `transacoes.csv` | CSV | Registrar receitas, despesas e analisar padrões de gastos |
| `metas_financeiras.json` | JSON | Definir e acompanhar objetivos financeiros do usuário |
| `orcamentos.csv` | CSV | Controlar limites de gastos por categoria |
| `assinaturas.json` | JSON | Monitorar cobranças recorrentes e serviços ativos |
| `parcelamentos.csv` | CSV | Acompanhar compras parceladas e despesas futuras |
| `alertas_financeiros.json` | JSON | Gerar notificações sobre gastos excessivos, vencimentos e economia |
| `relatorios_mensais.csv` | CSV | Consolidar análises financeiras mensais do usuário |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não utilizei os dados mockados, na verdade recriei meus próprios dados baseados no problema que o agente irá solucionar

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

O agente utiliza bibliotecas Python como `json` e `pandas` para carregar os arquivos da base de conhecimento.  

Os arquivos `.json` são carregados utilizando a biblioteca `json`, permitindo acesso às informações estruturadas dos usuários, metas financeiras, assinaturas e alertas.  

Os arquivos `.csv` são carregados utilizando a biblioteca `pandas`, facilitando análise de transações, orçamentos, parcelamentos e relatórios financeiros.  

Todos os dados são carregados no início da execução do agente e utilizados durante a sessão para gerar análises financeiras, recomendações e respostas personalizadas.

```Python 
import json
import pandas as pd

# =========================
# CARREGAMENTO DOS ARQUIVOS JSON
# =========================

with open("usuarios.json", "r", encoding="utf-8") as arquivo:
    usuarios = json.load(arquivo)

with open("metas_financeiras.json", "r", encoding="utf-8") as arquivo:
    metas_financeiras = json.load(arquivo)

with open("assinaturas.json", "r", encoding="utf-8") as arquivo:
    assinaturas = json.load(arquivo)

with open("alertas_financeiros.json", "r", encoding="utf-8") as arquivo:
    alertas_financeiros = json.load(arquivo)

# =========================
# CARREGAMENTO DOS ARQUIVOS CSV
# =========================

transacoes = pd.read_csv("transacoes.csv")

orcamentos = pd.read_csv("orcamentos.csv")

parcelamentos = pd.read_csv("parcelamentos.csv")

relatorios_mensais = pd.read_csv("relatorios_mensais.csv")

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
```

### Como os dados são usados no prompt?

#### Contextualização do Usuário
Os dados do perfil financeiro do usuário, como renda mensal, objetivos financeiros e saldo disponível, são utilizados para personalizar as respostas do agente.

#### Análise de Transações
As transações registradas nos arquivos CSV são consultadas dinamicamente para identificar padrões de gastos, despesas recorrentes e comportamento financeiro.

#### Utilização de Metas e Orçamentos
As metas financeiras e limites de orçamento são inseridos no contexto do prompt para que o agente acompanhe progresso financeiro e gere recomendações adequadas.

#### Geração de Alertas
Os dados de assinaturas, vencimentos e gastos excessivos são utilizados para criar alertas e notificações preventivas durante a interação.

#### Construção Dinâmica do Prompt
O agente consulta os arquivos JSON e CSV conforme a necessidade da conversa, adicionando ao prompt apenas as informações relevantes para gerar respostas contextualizadas e personalizadas.

---

## Exemplo de Contexto Montado

> Exemplo de como os dados financeiros são organizados e enviados para o agente.

```text
Dados do Usuário:
- Nome: Carlos Silva
- Perfil Financeiro: Moderado
- Renda Mensal: R$ 4.500,00
- Objetivo Principal: Economizar
- Saldo Atual: R$ 2.930,60

Metas Financeiras:
- Comprar notebook: R$ 1.800 / R$ 4.500
- Reserva de emergência: R$ 3.200 / R$ 10.000

Últimas Transações:
- 02/05: Aluguel - R$ 1.500
- 03/05: Supermercado - R$ 320,50
- 05/05: Cinema - R$ 45,00
- 07/05: Projeto freelancer + R$ 800,00

Orçamentos:
- Alimentação: R$ 540 / R$ 600
- Lazer: R$ 180 / R$ 300

Alertas:
- Você gastou 35% a mais com alimentação este mês.
- Sua assinatura da Netflix vence em 3 dias.
```
