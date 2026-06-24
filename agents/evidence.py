from llm import llm

from tools.memory_loader import (
    load_logs,
    load_metrics,
    load_runbooks,
    load_system_knowledge,
    load_previous_incidents,
)


def evidence_agent(state):
    logs = load_logs()
    metrics = load_metrics()
    runbooks = load_runbooks()
    system_knowledge = load_system_knowledge()
    previous_incidents = load_previous_incidents()

    prompt = f"""
Você é o Evidence Agent de um sistema multiagente de investigação de incidentes.

Sua função NÃO é resolver o incidente.
Sua função é apenas coletar, filtrar e organizar evidências relevantes.

DESCRIÇÃO DO INCIDENTE:
{state["incident_description"]}

LOGS:
{logs}

MÉTRICAS:
{metrics}

CONHECIMENTO DO SISTEMA:
{system_knowledge}

RUNBOOKS:
{runbooks}

INCIDENTES ANTERIORES:
{previous_incidents}

TAREFA:
Extraia as evidências mais importantes para a investigação.

REGRAS:
- Não conclua a causa raiz ainda.
- Não proponha solução ainda.
- Foque apenas em sinais observáveis.
- Relacione logs, métricas, arquitetura e incidentes anteriores.
- Responda em português brasileiro.

Formato da resposta:

1. Evidências dos logs
2. Evidências das métricas
3. Evidências da arquitetura do sistema
4. Evidências dos runbooks
5. Similaridades com incidentes anteriores
6. Sinais que parecem menos relevantes
"""

    response = llm.invoke(prompt)

    return {
        "logs": logs,
        "metrics": metrics,
        "runbooks": runbooks,
        "system_knowledge": system_knowledge,
        "previous_incidents": str(previous_incidents),
        "evidences": response.content,
        "last_agent": "evidence"
    }