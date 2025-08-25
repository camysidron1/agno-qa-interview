"""
Question-Answering Agent using Agno Agents

This minimal agent answers simple factual questions and returns a Markdown-formatted
response with an answer and a citation. It is intentionally lightweight and
includes a couple of hardcoded examples so it runs without external API calls.
"""
from dataclasses import dataclass
from typing import Dict


@dataclass
class QAResult:
    output: str


class QuestionAnswerAgent:
    """A very small, self-contained agent.

    In a real-world scenario, you'd use Agno Agents with a model backend (e.g., Anthropic via
    the `anthropic` package) and a proper tool or retrieval layer. For this interview scaffold,
    we keep the behavior deterministic and offline by hardcoding a few examples.

    Output format must be:
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

    def answer(self, question: str) -> QAResult:
        key = question.strip().lower()
        entry = self._kb.get(key)
        if not entry:
            # Minimal fallback response
            out = (
                "**Answer:** I don't know\n"
                "**Citation:** https://example.com/unknown"
            )
            return QAResult(output=out)

        out = f"**Answer:** {entry['answer']}\n**Citation:** {entry['citation']}"
        return QAResult(output=out)

