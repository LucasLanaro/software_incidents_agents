# Multi-Agent Incident Investigator

Projeto desenvolvido para explorar a implementação de sistemas multiagentes inspirados pelos conceitos apresentados no paper **CoALA (Cognitive Architectures for Language Agents)**.

A proposta do projeto é simular uma equipe de investigação de incidentes em software, onde diferentes agentes colaboram para analisar evidências, formular hipóteses, avaliar possíveis causas e produzir um relatório técnico final.

## Objetivo

Demonstrar como conceitos de arquiteturas cognitivas podem ser aplicados na construção de sistemas multiagentes utilizando LLMs.

Em vez de utilizar um único agente responsável por toda a investigação, o processo é dividido em papéis especializados que compartilham informações através de uma memória comum.

## Arquitetura

O sistema é composto pelos seguintes agentes:

* **Supervisor Agent**: controla o fluxo de execução e avalia a qualidade das respostas geradas pelos demais agentes.
* **Evidence Agent**: coleta e organiza evidências a partir de logs, métricas, runbooks, documentação e incidentes anteriores.
* **Hypothesis Agent**: gera hipóteses concorrentes para explicar o incidente.
* **Critic Agent**: analisa criticamente as hipóteses geradas, apontando forças, fraquezas e inconsistências.
* **Resolution Agent**: propõe ações de mitigação, validação e próximos passos.
* **Reporter Agent**: consolida toda a investigação em um relatório técnico final.

## Fluxo de Execução

```text
Supervisor
    ↓
Evidence Agent
    ↓
Supervisor
    ↓
Hypothesis Agent
    ↓
Supervisor
    ↓
Critic Agent
    ↓
Supervisor
    ↓
Resolution Agent
    ↓
Supervisor
    ↓
Reporter Agent
    ↓
Supervisor
    ↓
Finish
```

Após cada etapa, o Supervisor avalia a saída produzida pelo agente responsável. Caso a resposta não atenda aos critérios mínimos definidos, o agente pode ser executado novamente antes que o fluxo avance.

## Relação com o CoALA

Este projeto busca representar, de forma simplificada, alguns dos componentes descritos pelo framework CoALA:

| Conceito CoALA    | Implementação                                 |
| ----------------- | --------------------------------------------- |
| Working Memory    | Estado compartilhado do LangGraph             |
| Episodic Memory   | Histórico de incidentes anteriores            |
| Semantic Memory   | Conhecimento do sistema e documentação        |
| Procedural Memory | Runbooks operacionais                         |
| Retrieval         | Busca de evidências e incidentes similares    |
| Reasoning         | Geração de hipóteses e propostas de resolução |
| Evaluation        | Critic Agent e Supervisor Agent               |
| Decision Process  | Controle de fluxo realizado pelo Supervisor   |

## Estrutura do Projeto

```text
.
├── agents/
├── memory/
├── graph.py
├── state.py
├── llm.py
├── main.py
├── requirements.txt
└── README.md
```

## Dados Utilizados

A pasta `memory/` contém dados simulados utilizados para demonstração:

* logs de aplicação
* métricas de observabilidade
* runbooks operacionais
* conhecimento da arquitetura do sistema
* incidentes anteriores

Esses arquivos são exemplos utilizados para validar o comportamento dos agentes durante o desenvolvimento.

## Tecnologias

* Python
* LangGraph
* LangChain
* Ollama
* Qwen

## Execução

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o projeto:

```bash
python3 main.py
```

Durante a execução, o sistema exibe no terminal o fluxo dos agentes e as decisões tomadas pelo Supervisor até a geração do relatório final.
