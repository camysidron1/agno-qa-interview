"""
Evaluation Agent placeholder (Agno-based scaffold).

Interview task: Implement an agent that validates and evaluates the
QuestionAnswerAgent's output.

This class is defined around the Agno framework by default. You are expected to
use the `agno` Agent inside `evaluate` to drive the evaluation if you choose an
LLM-assisted route. Load ANTHROPIC_API_KEY from your environment.
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any
import os

from agno import Agent as AgnoAgent  # type: ignore
from agno.models import Anthropic  # type: ignore


@dataclass
class EvaluationResult:
    """Structured result for evaluation.

    Attributes:
        passed: Whether the QA output passed all checks.
        reason: Short, human-readable explanation.
        details: Optional structured fields such as detected answer/citation,
                 format flags, or scoring if you implement it.
    """
    passed: bool
    reason: str
    details: Optional[Dict[str, Any]] = None


class EvaluationAgent:
    """Candidate TODOs (Agno-first design):

    Implement the following:
      1) Format validation
         - Ensure the text has exactly two lines in Markdown:
           **Answer:** <short factual answer>
           **Citation:** <URL>
         - Validate that the citation looks like a URL (e.g., starts with http or https).

      2) Correctness/quality judgment
         - For the minimal demo, you can implement a tiny rule-based judge:
           - Given the original question and the QA output, check if the answer
             matches expected answers for known questions (e.g., capital of France is "Paris").
         - Alternatively, design an LLM-based judge using Anthropic via Agno.

      3) Return a structured evaluation
         - Use EvaluationResult(passed: bool, reason: str, details: dict)
         - Consider including fields like {"format_ok": bool, "answer": str, "citation": str}

    Keep it simple, readable, and well-documented. Add unit tests if time permits.
    """

    def __init__(self) -> None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        # Build an Agno Agent to serve as the judge. The exact prompt/usage is up to the candidate.
        self._judge: Optional[AgnoAgent] = None
        if api_key:
            model = Anthropic(api_key=api_key, model="claude-3-haiku-20240307")
            self._judge = AgnoAgent(
                model=model,
                system_prompt=(
                    "You are an evaluation agent. Given a question and an agent's output,\n"
                    "1) Verify the output format (two lines: Answer and Citation).\n"
                    "2) Judge factual correctness concisely.\n"
                    "Respond with JSON: {\"format_ok\":bool, \"correct\":bool, \"reason\":str}."
                ),
            )

    def evaluate(self, question: str, qa_output: str) -> EvaluationResult:
        """Evaluate the QA output against the expected format and correctness.

        TODO: Implement this method.
        Suggested steps:
          - Parse qa_output to extract `answer` and `citation` using regex or string methods.
          - Validate the format and URL.
          - Judge correctness for known questions (e.g., "What is the capital of France?")
            and/or call `self._judge.run(...)` to use the Agno Agent you built above.
          - Return an EvaluationResult with pass/fail and an explanation.
        """
        raise NotImplementedError("EvaluationAgent.evaluate is not implemented. Complete this in the interview.")

