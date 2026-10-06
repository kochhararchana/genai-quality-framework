from llm_client import ask_llm

def test_response_consistency():
    question = "What is the capital of India?"

    response1 = ask_llm(question)
    response2 = ask_llm(question)
    response3 = ask_llm(question)

    assert "New Delhi" in response1
    assert "New Delhi" in response2
    assert "New Delhi" in response3