from llm import llm


def resolution_agent(state):
    prompt = f"""
Você é o Resolution Agent de um sistema multiagente de investigação de incidentes.

Sua função é propor a resolução mais provável com base nas evidências,
hipóteses e análise crítica.

IMPORTANTE:
- Agora você pode indicar a causa raiz mais provável.
- Não invente novas evidências.
- Não ignore incertezas.
- Não invente responsáveis ou tempos estimados.
- Não proponha testes de carga se não houver evidência de sobrecarga.
- Não afirme mudança de configuração se ela não estiver nas evidências.
- Diferencie causa raiz provável de ações de mitigação.
- Use somente informações presentes na Working Memory.

DESCRIÇÃO DO INCIDENTE:
{state["incident_description"]}

EVIDÊNCIAS:
{state["evidences"]}

HIPÓTESES:
{state["hypotheses"]}

ANÁLISE CRÍTICA:
{state["critic_analysis"]}

TAREFA:
Gere uma proposta de resolução do incidente.

Formato da resposta:

1. Causa raiz provável
   - Descrição:
   - Confiança: baixa / média / alta
   - Justificativa:

2. Ações imediatas de mitigação
   - Ação 1:
   - Ação 2:
   - Ação 3:

3. Ações de validação
   - Como confirmar a causa raiz:
   - Quais dados verificar:
   - Quais sinais devem melhorar após a mitigação:

4. Riscos se nada for feito

5. Próximos passos recomendados
"""

    response = llm.invoke(prompt)

    return {
        "resolution": response.content,
        "last_agent": "resolution"
    }