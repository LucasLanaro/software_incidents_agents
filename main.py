from graph import build_graph


app = build_graph()

initial_state = {
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
    "last_agent": None,

    "supervisor_reasoning": None,
    "supervisor_history": [],

    "quality_check": None,
    "retry_count": 0,
    "max_retries": 1,
}

final_state = initial_state.copy()

print("\n🚀 Iniciando investigação multiagente...\n")

for step in app.stream(initial_state):
    node_name = list(step.keys())[0]
    node_output = step[node_name]

    final_state.update(node_output)

    print("\n==============================")
    print(f"NODE EXECUTADO: {node_name}")
    print("==============================")

    if node_name == "supervisor":
        print("Próximo agente:", node_output.get("next_agent"))
        print("Motivo:", node_output.get("supervisor_reasoning"))

    elif node_name == "evidence":
        print("Evidence Agent finalizou extração de evidências.")

    elif node_name == "hypothesis":
        print("Hypothesis Agent gerou hipóteses.")

    elif node_name == "critic":
        print("Critic Agent avaliou as hipóteses.")

    elif node_name == "resolution":
        print("Resolution Agent propôs resolução.")

    elif node_name == "reporter":
        print("Reporter Agent gerou relatório final.")

print("\n✅ Investigação finalizada.\n")

print("\n\n===== FINAL REPORT =====\n")
print(final_state.get("final_report"))

print("\n\n===== SUPERVISOR HISTORY =====\n")
for i, decision in enumerate(final_state.get("supervisor_history", []), start=1):
    print(f"\n--- Decision {i} ---")
    print(decision)