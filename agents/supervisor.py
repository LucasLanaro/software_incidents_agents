from llm import llm


def deterministic_next_agent(state):
    if state.get("evidences") is None:
        return "evidence", "Ainda não existem evidências."

    if state.get("hypotheses") is None:
        return "hypothesis", "Evidências aprovadas. Gerar hipóteses."

    if state.get("critic_analysis") is None:
        return "critic", "Hipóteses aprovadas. Executar análise crítica."

    if state.get("resolution") is None:
        return "resolution", "Análise crítica aprovada. Gerar resolução."

    if state.get("final_report") is None:
        return "reporter", "Resolução aprovada. Gerar relatório final."

    return "finish", "Fluxo concluído."


def get_last_output(state):
    last_agent = state.get("last_agent")

    if last_agent == "evidence":
        return state.get("evidences")

    if last_agent == "hypothesis":
        return state.get("hypotheses")

    if last_agent == "critic":
        return state.get("critic_analysis")

    if last_agent == "resolution":
        return state.get("resolution")

    if last_agent == "reporter":
        return state.get("final_report")

    return None


def evaluate_last_output(state):
    last_agent = state.get("last_agent")
    last_output = get_last_output(state)

    if last_agent is None or last_output is None:
        return True, "Nenhum agente anterior para avaliar."

    prompt = f"""
Você é o Supervisor Evaluator de um sistema multiagente de investigação de incidentes.

Sua função é avaliar se a saída do último agente está boa o suficiente para avançar.

Último agente executado:
{last_agent}

Descrição do incidente:
{state["incident_description"]}

Saída gerada pelo último agente:
{last_output}

Critérios gerais:
- A resposta deve ser útil para investigação de incidente.
- A resposta não deve inventar informações fora da Working Memory.
- A resposta deve cumprir o papel do agente.
- A resposta deve ser clara e técnica.

Critérios específicos:

Se last_agent = evidence:
- Deve listar evidências de logs.
- Deve listar evidências de métricas.
- Deve usar conhecimento do sistema.
- Deve comparar com incidentes anteriores.
- Não deve fechar causa raiz final.

Se last_agent = hypothesis:
- Deve gerar hipóteses concorrentes.
- Deve ter evidências a favor e contra.
- Deve indicar confiança.
- Não deve fechar resolução final.

Se last_agent = critic:
- Deve avaliar as hipóteses.
- Deve apontar pontos fortes e fracos.
- Deve ranquear hipóteses.
- Não deve criar hipóteses principais novas.

Se last_agent = resolution:
- Deve indicar causa raiz provável.
- Deve separar mitigação de validação.
- Deve reconhecer incertezas.
- Não deve inventar responsáveis ou tempos estimados.

Se last_agent = reporter:
- Deve consolidar relatório final.
- Deve ser útil para equipe técnica.
- Não deve criar novas evidências ou hipóteses.

Responda exatamente neste formato:

APPROVED: yes|no
REASON: motivo curto
"""

    response = llm.invoke(prompt)
    content = response.content.strip()

    approved = False

    for line in content.splitlines():
        if line.startswith("APPROVED:"):
            value = line.replace("APPROVED:", "").strip().lower()
            approved = value == "yes"

    return approved, content


def supervisor_agent(state):
    history = state.get("supervisor_history", [])
    retry_count = state.get("retry_count", 0)
    max_retries = state.get("max_retries", 1)

    approved, quality_check = evaluate_last_output(state)

    if not approved and retry_count < max_retries:
        next_agent = state.get("last_agent")
        reason = (
            f"Saída do agente '{next_agent}' reprovada. "
            f"Reexecutando o mesmo agente. Retry {retry_count + 1}/{max_retries}."
        )
        retry_count += 1

    else:
        next_agent, reason = deterministic_next_agent(state)
        retry_count = 0

        if not approved and state.get("last_agent") is not None:
            reason = (
                f"Saída anterior não foi aprovada, mas max_retries foi atingido. "
                f"Avançando por segurança. {reason}"
            )

    history.append(
        f"LAST_AGENT: {state.get('last_agent')}\n"
        f"QUALITY_CHECK:\n{quality_check}\n"
        f"NEXT_AGENT: {next_agent}\n"
        f"REASON: {reason}"
    )

    return {
        "next_agent": next_agent,
        "supervisor_reasoning": reason,
        "supervisor_history": history,
        "quality_check": quality_check,
        "retry_count": retry_count,
    }