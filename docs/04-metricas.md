# Avaliação e Métricas

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de Meta Financeira
- **Pergunta:** "Como está minha meta de comprar um notebook?"
- **Resposta esperada:** Informar que a meta é de R$ 4.500,00 e que já foram acumulados R$ 1.800,00.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Consulta de Orçamento
- **Pergunta:** "Quanto já gastei com lazer?"
- **Resposta esperada:** Informar que foram gastos R$ 180,00 de um orçamento de R$ 300,00.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Verificação de Alertas
- **Pergunta:** "Tenho algum alerta financeiro?"
- **Resposta esperada:** Informar que houve aumento de 35% nos gastos com alimentação e que a assinatura da Netflix vence em 3 dias.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Pergunta Fora do Escopo
- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** Informar que o agente é especializado em organização financeira e não possui informações meteorológicas.
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 5: Informação Não Disponível
- **Pergunta:** "Qual é o saldo da minha conta bancária principal?"
- **Resposta esperada:** Informar que não possui acesso direto a contas bancárias externas e depende apenas dos dados fornecidos.
- **Resultado:** [ ] Correto  [X] Incorreto

### Teste 6: Consulta de Transações
- **Pergunta:** "Quais foram minhas últimas transações?"
- **Resposta esperada:** Exibir aluguel (R$ 1.500,00), supermercado (R$ 320,50), cinema (R$ 45,00) e projeto freelancer (+R$ 800,00).
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Resultados

Após a execução dos testes, foi possível verificar que o agente Nexo Finance conseguiu utilizar corretamente os dados disponibilizados no contexto para responder às solicitações do usuário.

**O que funcionou bem:**

* Consultou corretamente o progresso das metas financeiras.
* Identificou e apresentou valores de orçamento e gastos de forma precisa.
* Exibiu alertas financeiros cadastrados na base de dados.
* Listou corretamente as transações registradas no histórico.
* Manteve linguagem clara, acessível e adequada ao público-alvo.
* Reconheceu perguntas fora do escopo financeiro e informou suas limitações.
* Foi capaz de gerar orientações e sugestões de economia com base nos dados fornecidos.

**O que pode melhorar:**

* Em algumas respostas, forneceu recomendações financeiras sem explicar claramente que se tratavam apenas de sugestões.
* A resposta sobre saldo da conta bancária pode gerar ambiguidade, pois o agente utilizou o saldo presente no contexto mesmo sem possuir integração com instituições bancárias.
* Algumas respostas foram mais extensas do que o necessário para perguntas objetivas.
* Poderia apresentar indicadores financeiros em formatos mais visuais, como percentuais e resumos estruturados.
* Poderia justificar melhor os cálculos utilizados ao apresentar metas e projeções financeiras.
* Pode ser aprimorado para diferenciar informações efetivamente cadastradas de interpretações geradas a partir dos dados.
