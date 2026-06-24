from agents.evidence import evidence_agent
from agents.hypothesis import hypothesis_agent
from agents.critic import critic_agent
from agents.resolution import resolution_agent
from agents.reporter import reporter_agent


state = {
    "incident_description": "Após o deploy da versão 2.3.1, clientes começaram a receber erro 500 ao finalizar compras no checkout.",

    "logs": None,
    "metrics": None,
    "runbooks": None,
    "system_knowledge": None,
    "previous_incidents": None,

    "evidences": None,
    "hypotheses": None,
    "critic_analysis": None,
    "resolution": None,
    "final_report": None,

    "next_agent": None,
    "supervisor_reasoning": None,
    "supervisor_history": [],
}

state.update(evidence_agent(state))
state.update(hypothesis_agent(state))
state.update(critic_agent(state))
state.update(resolution_agent(state))
state.update(reporter_agent(state))

print("\n===== FINAL REPORT =====\n")
print(state["final_report"])