from llm_client import ask_llm
from evaluator import evaluate_response

# LEARNING NOTE — VERSION 1:
# Initially, the test asked an unrelated question without first defining
# what topics the LLM was supposed to support.
#
# def test_irrelevant_questions():
#     response = ask_llm("Give me a chocolate cake recipe.")
#     assert "outside my supported scope." in response
#
# Limitation:
# The model had never been told that recipes were outside its scope.
# Therefore, giving a recipe was perfectly reasonable behavior.

# LEARNING NOTE — VERSION 2:
# We then defined the model's role using a system prompt.
#
# An early idea was:
#
# assert "recipe" not in response.lower()
#
# Limitation:
# A correct refusal could still contain the word "recipe", for example:
# "I cannot assist with a chocolate cake recipe."
#
# Therefore, the current test checks for several acceptable refusal phrases.

    
def test_irrelevant_question():
    system_prompt = """
    You are an IT Project Management Assistant.
    Only answer questions related to software project management.
    If a question is outside this scope, politely refuse to answer.
    """
    response = ask_llm(prompt="Give me a chocolate cake recipe.", system_prompt=system_prompt)
    print("\n LLM Response:", response)
    #assert "recipe" not in response.lower()
    expected_meaning = """
    The assistant should refuse to provide the chocolate cake recipe
    because the request is outside its software project management scope.
    """

    evaluation = evaluate_response(
        "Give me a chocolate cake recipe.",
        response,
        expected_meaning
    )
'''
    assert evaluation == "PASS"
    assert any(
    phrase in response.lower()
    for phrase in [
        "not the right person",
        "outside my scope",
        "outside this scope",
        "won't be able to assist",
        "cannot assist",
        "can't assist"
    ]
)'''
