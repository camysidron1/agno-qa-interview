"""
Evaluation Agent placeholder.

Interview task: Implement an agent that validates and evaluates the
QuestionAnswerAgent's output.

You may choose a minimal deterministic approach (regex, parsing) or an
LLM-assisted approach using Agno + Anthropic. If using an LLM, load
ANTHROPIC_API_KEY from the environment (e.g., via python-dotenv).
"""
from dataclasses import dataclass
from typing import Optional, Dict, Any


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
    """Candidate TODOs:

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

    def evaluate(self, question: str, qa_output: str) -> EvaluationResult:
        """Evaluate the QA output against the expected format and correctness.

        TODO: Implement this method.
        Suggested steps:
          - Parse qa_output to extract `answer` and `citation` using regex or string methods.
          - Validate the format and URL.
          - Judge correctness for known questions (e.g., "What is the capital of France?")
            or leave hooks for a model-based judge.
          - Return an EvaluationResult with pass/fail and an explanation.
        """
        raise NotImplementedError("EvaluationAgent.evaluate is not implemented. Complete this in the interview.")

