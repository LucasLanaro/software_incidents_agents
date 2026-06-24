from llm import llm


def critic_agent(state):
    prompt = f"""
Você é o Critic Agent de um sistema multiagente de investigação de incidentes.

Sua função é avaliar criticamente as hipóteses geradas.

IMPORTANTE:
- Você NÃO deve criar novas hipóteses principais.
- Você NÃO deve propor solução final.
- Você deve tentar refutar, enfraquecer ou fortalecer as hipóteses existentes.
- Use apenas as evidências e hipóteses presentes na Working Memory.
- Não introduza fatores que não aparecem nas evidências.

DESCRIÇÃO DO INCIDENTE:
{state["incident_description"]}

EVIDÊNCIAS COLETADAS:
{state["evidences"]}

HIPÓTESES GERADAS:
{state["hypotheses"]}

TAREFA:
Avalie criticamente cada hipótese.

Formato da resposta:

1. Avaliação da hipótese principal
   - Pontos que fortalecem:
   - Pontos que enfraquecem:
   - Inconsistências:
   - Veredito parcial:

2. Avaliação da hipótese alternativa
   - Pontos que fortalecem:
   - Pontos que enfraquecem:
   - Inconsistências:
   - Veredito parcial:

3. Avaliação da hipótese menos provável
   - Pontos que fortalecem:
   - Pontos que enfraquecem:
   - Inconsistências:
   - Veredito parcial:

4. Ranking crítico das hipóteses
   - 1º lugar:
   - 2º lugar:
   - 3º lugar:

5. Evidência mais decisiva até agora
6. Maior incerteza restante
- Não crie nomes novos para hipóteses.
- Use exatamente as hipóteses recebidas.
- Não introduza causas como rede, servidor, demanda ou capacidade se elas não estiverem nas hipóteses originais.
- Se uma hipótese estiver mal formulada, critique isso explicitamente.
"""

    response = llm.invoke(prompt)

    return {
        "critic_analysis": response.content,
        "last_agent": "critic"
    }