import pytest
from llm_client import ask_llm
from evaluator import evaluate_response

# LEARNING NOTE — VERSION 1:
# Initially, factual accuracy was tested using simple keyword matching:
#
# def test_factual_question(question, expected_answer):
#     response = ask_llm(question)
#     assert expected_answer in response
#
# Example:
# If expected_answer = "Paris", the test checked whether "Paris"
# appeared somewhere in the LLM response.
#
# Limitation:
# Keyword matching checks text, not meaning.
# As the framework became more advanced, we moved to semantic evaluation
# using an LLM-as-a-Judge.

@pytest.mark.parametrize("question, expected_meaning", [("What is the capital of France?", "The capital of France is Paris."),
    ("What is the capital of Japan?", "The capital of Japan is Tokyo"),
    ("What is the capital of India?", "The capital of India is New Delhi"),])

def test_factual_question(question, expected_meaning):
    response = ask_llm(question)
    evaluation = evaluate_response(question, response, expected_meaning)

    #assert "PASS" in evaluation.upper()
    assert evaluation == "PASS"
    





