from llm import llm


def hypothesis_agent(state):
    prompt = f"""
Você é o Hypothesis Agent de um sistema multiagente de investigação de incidentes.

Sua função é gerar hipóteses de causa raiz com base nas evidências coletadas.

IMPORTANTE:
- Você ainda NÃO deve decidir a causa raiz final.
- Você deve gerar hipóteses concorrentes.
- Cada hipótese deve ter evidências a favor, evidências contra e nível de confiança.
- Use somente as informações disponíveis na Working Memory.

DESCRIÇÃO DO INCIDENTE:
{state["incident_description"]}

EVIDÊNCIAS COLETADAS:
{state["evidences"]}

TAREFA:
Gere hipóteses plausíveis para a causa do incidente.

Formato da resposta:

1. Hipótese principal
   - Descrição:
   - Evidências a favor:
   - Evidências contra:
   - Confiança: baixa / média / alta

2. Hipótese alternativa
   - Descrição:
   - Evidências a favor:
   - Evidências contra:
   - Confiança: baixa / média / alta

3. Hipótese menos provável
   - Descrição:
   - Evidências a favor:
   - Evidências contra:
   - Confiança: baixa / média / alta

Finalize com:
- Hipótese mais forte até o momento
- Informações adicionais que seriam úteis para confirmar
"""

    response = llm.invoke(prompt)

    return {
        "hypotheses": response.content,
        "last_agent": "hypothesis"
    }