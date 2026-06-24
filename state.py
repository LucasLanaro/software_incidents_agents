from typing import TypedDict, Optional


class IncidentState(TypedDict):
    incident_description: str

    logs: Optional[str]
    metrics: Optional[str]
    runbooks: Optional[str]
    system_knowledge: Optional[str]
    previous_incidents: Optional[str]

    evidences: Optional[str]
    hypotheses: Optional[str]
    critic_analysis: Optional[str]
    resolution: Optional[str]
    final_report: Optional[str]

    next_agent: Optional[str]
    last_agent: Optional[str]

    supervisor_reasoning: Optional[str]
    supervisor_history: list[str]

    quality_check: Optional[str]
    retry_count: int
    max_retries: int