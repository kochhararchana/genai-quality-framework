# Automated LLM Quality Testing Framework

A Python and Pytest-based framework for testing the quality, reliability, and safety of Large Language Model (LLM) responses.

This project uses a locally running Llama 3.2 model through Ollama and demonstrates multiple approaches for evaluating Generative AI applications, including deterministic assertions and LLM-as-a-Judge semantic evaluation.

## Project Objective

Traditional software testing often compares actual output with an exact expected result.

LLM responses are different because the same correct answer can be expressed in many different ways.

This project explores how automated testing can be applied to LLM applications while handling challenges such as:

- Factual accuracy
- Hallucinations
- Response consistency
- Out-of-scope questions
- Prompt injection
- Sensitive-information leakage
- Semantic variation in LLM responses

## Technologies Used

- Python
- Pytest
- Ollama
- Llama 3.2 3B
- pytest-html
- VS Code

## Project Structure

```text
genai-quality-framework/
│
├── tests/
│   ├── test_basic.py
│   ├── test_consistency.py
│   ├── test_factual.py
│   ├── test_hallucination.py
│   ├── test_irrelevant.py
│   ├── test_prompt_injection.py
│   └── test_sensitive_info.py
│
├── evaluator.py
├── llm_client.py
├── ollama_connection.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How the Framework Works

### LLM Client

`llm_client.py` provides a reusable interface for communicating with the locally running Llama model through Ollama.

It supports both user prompts and optional system prompts.

### Semantic Evaluator

`evaluator.py` implements an LLM-as-a-Judge approach.

Instead of requiring exact wording, the evaluator compares the meaning of an LLM response with the expected meaning and returns `PASS` or `FAIL`.

This helps reduce false failures caused by normal variations in LLM wording.

### Test Suite

The framework currently contains tests for:

- Basic Pytest functionality
- Factual accuracy
- Hallucination detection
- Response consistency
- Out-of-scope behavior
- Prompt-injection resistance
- Sensitive-information protection

Different tests use different evaluation strategies depending on the risk being tested.

## Running the Project

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2. Install Ollama

Ollama must be installed and running locally.

### 3. Download the model

```bash
ollama pull llama3.2:3b
```

### 4. Run the tests

```bash
python -m pytest -v
```

## Generate an HTML Test Report

```bash
python -m pytest --html=report.html --self-contained-html
```

The generated `report.html` file is excluded from Git version control because it is a generated test artifact.

## Learning Journey

The framework was developed incrementally.

The initial version used hard-coded mock LLM responses so that the basic Python and Pytest structure could be developed independently of an external AI service.

The framework was then connected to a cloud-based Gemini model. API quota and availability limitations highlighted the challenges of depending on external LLM services for repeated automated testing.

The project was subsequently migrated to a locally running Llama 3.2 model using Ollama.

Early tests relied heavily on exact phrases and keyword matching. This exposed an important challenge in GenAI testing: a response can be semantically correct even when its wording differs from the expected answer.

To address this, an LLM-as-a-Judge semantic evaluator was introduced for tests where meaning is more important than exact wording.

## Key Learnings

- LLM outputs can be non-deterministic.
- Exact string matching is often insufficient for LLM testing.
- Different AI risks can require different evaluation strategies.
- Semantic evaluation can reduce false failures caused by wording variations.
- LLM-as-a-Judge introduces its own limitations and should not be treated as infallible.
- Lower temperature can improve evaluator consistency but does not guarantee deterministic behavior.
- System prompts can create controlled safety and security test scenarios.
- Local models can make repeated experimentation easier by removing cloud API quota dependency.

## Current Status

The current test suite contains **9 automated test cases**, with all **9 passing in the latest full test run**.

This project is intended as a learning and portfolio project demonstrating practical approaches to automated quality testing for Generative AI applications.

Latest test execution: **9/9 tests passed**

The automated test suite covers:
- Factual accuracy
- Hallucination detection
- Response consistency
- Prompt injection resistance
- Sensitive information protection
- Out-of-scope question handling

Run the test suite:

python -m pytest

Generate the HTML report:

python -m pytest --html=report.html --self-contained-html