"""
Entry point demo: runs the QuestionAnswerAgent and prints output.
Includes a commented stub for invoking the EvaluationAgent.
"""
import os
from dotenv import load_dotenv

from question_answer_agent import QuestionAnswerAgent
# from eval_agent import EvaluationAgent


def main() -> None:
    # Load environment variables from .env if present
    load_dotenv()

    # If using Anthropic (optional extension), ANTHROPIC_API_KEY should be set
    _ = os.getenv("ANTHROPIC_API_KEY", "")

    qa = QuestionAnswerAgent()

    question = "What is the capital of France?"
    result = qa.answer(question)

    print("Question:", question)
    print("\nAgent Output:\n" + result.output)

    # Example of how EvaluationAgent would be used (to be implemented by candidate):
    # evaluator = EvaluationAgent()
    # eval_result = evaluator.evaluate(question, result.output)
    # print("\nEvaluation Result:")
    # print(eval_result)


if __name__ == "__main__":
    main()

