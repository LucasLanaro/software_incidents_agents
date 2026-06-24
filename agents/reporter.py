from llm import llm


def reporter_agent(state):
    prompt = f"""
Você é o Reporter Agent de um sistema multiagente de investigação de incidentes.

Sua função é consolidar a investigação em um relatório final claro, técnico e objetivo.

IMPORTANTE:
- Não invente novas evidências.
- Não crie novas hipóteses.
- Não invente responsáveis ou tempos estimados.
- Não afirme que configuração foi alterada se isso não estiver explicitamente nas evidências.
- Não transforme "payment-client recebeu 503 do PayFast" em "falha interna do payment-client".
- Diferencie claramente:
  causa externa provável = PayFast retornando 503/timeouts
  impacto interno = checkout-service retornando 500
- Use apenas as informações presentes na Working Memory.
- O relatório deve ser útil para uma equipe técnica.

DESCRIÇÃO DO INCIDENTE:
{state["incident_description"]}

EVIDÊNCIAS:
{state["evidences"]}

HIPÓTESES:
{state["hypotheses"]}

ANÁLISE CRÍTICA:
{state["critic_analysis"]}

RESOLUÇÃO:
{state["resolution"]}

TAREFA:
Gere o relatório final do incidente.

Formato da resposta:

# Relatório de Investigação de Incidente

## 1. Resumo Executivo

## 2. Evidências Mais Relevantes

## 3. Hipótese Mais Provável

## 4. Hipóteses Alternativas

## 5. Causa Raiz Provável

## 6. Ações Imediatas Recomendadas

## 7. Ações de Validação

## 8. Incertezas Restantes
"""

    response = llm.invoke(prompt)

    return {
        "final_report": response.content,
        "last_agent": "reporter"
    }