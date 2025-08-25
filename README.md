# Agno QA Interview Scaffold

This repository provides a minimal example using the Agno Agents framework. It includes a simple Question-Answering Agent (the "source agent"). Your interview task is to implement an Evaluation Agent that validates and evaluates the source agent's output.

## What you'll build (Interview Task)
Implement the EvaluationAgent in `src/eval_agent.py` so it can:
- Validate the output format:
  - Must be Markdown with two lines:
    - `**Answer:** <short factual answer>`
    - `**Citation:** <URL>`
- Judge the correctness/quality of the answer.
- Return a structured evaluation (e.g., pass/fail + explanation + optional score).

You can use any reasonable approach (string parsing, regex, calling an LLM via Agno/Anthropic, etc.). Be prepared to discuss trade-offs.

## Running the example
Prereqs:
- Python 3.9+

Recommended: use a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
python -m pip install -U pip
pip install -r requirements.txt
```

Environment variables (optional for Anthropic-based extensions):
```bash
cp .env.example .env
# Edit .env to set ANTHROPIC_API_KEY if needed
```

Run the demo:
```bash
python src/main.py
```

## Project structure
```
.
├── README.md
├── requirements.txt
├── .env.example
└── src
    ├── question_answer_agent.py
    ├── eval_agent.py
    └── main.py
```

## Notes
- The QuestionAnswerAgent includes a couple of hardcoded examples so it runs offline (no API calls required).
- If you extend it to use Anthropic (via Agno), ensure ANTHROPIC_API_KEY is set in `.env` and loaded via `python-dotenv`.
- Keep your EvaluationAgent minimal but clear and well-tested if possible.
