from langgraph.graph import StateGraph, END

from state import IncidentState

from agents.supervisor import supervisor_agent
from agents.evidence import evidence_agent
from agents.hypothesis import hypothesis_agent
from agents.critic import critic_agent
from agents.resolution import resolution_agent
from agents.reporter import reporter_agent


def route_from_supervisor(state: IncidentState):
    next_agent = state.get("next_agent")

    if next_agent == "evidence":
        return "evidence"

    if next_agent == "hypothesis":
        return "hypothesis"

    if next_agent == "critic":
        return "critic"

    if next_agent == "resolution":
        return "resolution"

    if next_agent == "reporter":
        return "reporter"

    return END


def build_graph():
    graph = StateGraph(IncidentState)

    graph.add_node("supervisor", supervisor_agent)
    graph.add_node("evidence", evidence_agent)
    graph.add_node("hypothesis", hypothesis_agent)
    graph.add_node("critic", critic_agent)
    graph.add_node("resolution", resolution_agent)
    graph.add_node("reporter", reporter_agent)

    graph.set_entry_point("supervisor")

    graph.add_conditional_edges(
        "supervisor",
        route_from_supervisor,
        {
            "evidence": "evidence",
            "hypothesis": "hypothesis",
            "critic": "critic",
            "resolution": "resolution",
            "reporter": "reporter",
            END: END,
        },
    )

    graph.add_edge("evidence", "supervisor")
    graph.add_edge("hypothesis", "supervisor")
    graph.add_edge("critic", "supervisor")
    graph.add_edge("resolution", "supervisor")
    graph.add_edge("reporter", "supervisor")

    return graph.compile()