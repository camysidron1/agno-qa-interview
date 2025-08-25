"""
Question-Answering Agent defined with Agno Agents

This agent is defined using the Agno framework and is expected to produce a
Markdown-formatted response with an answer and a citation.

To ensure the project runs in a deterministic way during the demo, the agent
includes a couple of hardcoded examples. For unknown questions, it uses an
Anthropic-backed Agno Agent, which requires ANTHROPIC_API_KEY to be set.
"""
from dataclasses import dataclass
from typing import Dict, Optional
import os

from agno import Agent as AgnoAgent  # type: ignore
from agno.models import Anthropic  # type: ignore


@dataclass
class QAResult:
    output: str


class QuestionAnswerAgent:
    """An Agno-based QA agent with deterministic examples.

    Output format must be exactly:
    **Answer:** <short factual answer>
    **Citation:** <URL>
    """

    def __init__(self) -> None:
        # Minimal knowledge base
        self._kb: Dict[str, Dict[str, str]] = {
            "what is the capital of france?": {
                "answer": "Paris",
                "citation": "https://en.wikipedia.org/wiki/Paris",
            },
            "who wrote pride and prejudice?": {
                "answer": "Jane Austen",
                "citation": "https://en.wikipedia.org/wiki/Jane_Austen",
            },
        }
        self._agno_agent: Optional[AgnoAgent] = self._build_agno_agent()

    def _build_agno_agent(self) -> Optional[AgnoAgent]:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            return None
        model = Anthropic(api_key=api_key, model="claude-3-haiku-20240307")
        agent = AgnoAgent(
            model=model,
            system_prompt=(
                "You are a factual QA agent. Answer succinctly and always respond in this exact Markdown format:\n"
                "**Answer:** <short factual answer>\n"
                "**Citation:** <URL>\n"
                "If you are unsure, say 'I don't know' and use https://example.com/unknown as the citation."
            ),
        )
        return agent

    def answer(self, question: str) -> QAResult:
        key = question.strip().lower()
        entry = self._kb.get(key)
        if entry:
            out = f"**Answer:** {entry['answer']}\n**Citation:** {entry['citation']}"
            return QAResult(output=out)

        if self._agno_agent is None:
            raise RuntimeError(
                "Agno agent is not configured. Set ANTHROPIC_API_KEY in your environment (.env) to handle unknown questions."
            )

        resp = self._agno_agent.run(
            f"Question: {question}\n"
            "Answer in the required format."
        )
        text = getattr(resp, "content", None) or str(resp)
        return QAResult(output=text.strip())

