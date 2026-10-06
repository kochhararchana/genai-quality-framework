from llm_client import ask_llm

# LEARNING NOTE — VERSION 1:
# Initially, the hallucination test expected specific wording:
#
# def test_hallucination_unknown_question():
#     response = ask_llm("Who was the first person to land on Mars?")
#
#     assert any(
#         phrase in response.lower()
#         for phrase in [
#             "no human has landed on mars",
#             "no person has landed on mars",
#             "no one has landed on mars",
#             "nobody has landed on mars"
#         ]
#     )
#
# Limitation:
# The LLM returned correct answers such as:
# "No human has yet landed on Mars."
#
# The meaning was correct, but the exact phrases did not match.

# LEARNING NOTE — VERSION 2:
# We made the keyword check more flexible:
#
#def test_hallucination_unknown_question():
#    response = ask_llm("Who was the first person to land on Mars?")

#    response_lower = response.lower()

    #assert "mars" in response_lower

#    assert any(
#        phrase in response_lower
#        for phrase in [
#            "no human",
#            "no person",
#            "no one",
#            "nobody",
#            "never"
#        ]
#    )
#
# Limitation:
# We were still trying to predict all the possible ways an LLM
# could express the same meaning.


    #assert "no human has landed on Mars" in response
    #assert "I don't know" in response

# LEARNING NOTE — VERSION 3:
# We introduced evaluate_response() to perform semantic evaluation.
#
# Instead of asking:
# "Does the response contain one of my predefined phrases?"
#
# We now ask:
# "Is the response factually consistent with the expected meaning?"
#
# The evaluator uses an LLM-as-a-Judge approach.

from evaluator import evaluate_response

def test_hallucination_unknown_question():
    question = "Who was the first person to land on Mars"
    response = ask_llm(question)
    expected_meaning = "No human has landed on Mars"

    evaluation = evaluate_response(question, response, expected_meaning)

    print("\n LLM:", response)
    print("\n EVALUATOR VERDICT:", evaluation)

    #assert "PASS" in evaluation.upper()
    assert evaluation == "PASS"
