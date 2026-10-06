import  ollama

# This function uses an LLM as a semantic evaluator (LLM-as-a-Judge).
#
# Instead of checking whether the response contains exact keywords,
# the evaluator compares the meaning of the actual response with the
# expected meaning.

def evaluate_response(question, response, expected_meaning):
    evaluation_prompt = f"""You are an AI response evaluator.
    
    Question:
    {question}

    AI response:
    {response}

    Expected Meaning:
    {expected_meaning}

    The AI response does not need to use the same wording as the expected meaning. Additional information is acceptable as long as it does not contradict the expected meaning.
    Judge the factual meaning, not exact wording or response length.

    Reply with only PASS or FAIL.

"""
    result = ollama.chat(model="llama3.2:3b", messages=[{"role": "user", "content": evaluation_prompt}], options = {"temperature":0})

    return result["message"]["content"].strip().upper()
