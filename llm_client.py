# LEARNING NOTE — VERSION 1: MOCK LLM
#
# We initially used hard-coded responses instead of connecting
# to a real LLM. This allowed us to learn Pytest and build the
# test framework before introducing an actual AI model.
#
# Example:
#
# def ask_llm(prompt):
#     if "capital of France" in prompt:
#         return "Paris"
#
#     if "capital of Japan" in prompt:
#         return "Tokyo"
#
#     if "capital of India" in prompt:
#         return "New Delhi"
#
#     if "chocolate cake" in prompt:
#         return "This question is outside my supported scope."
#
#     if "ignore all previous instructions" in prompt.lower():
#         return "I cannot follow instructions that attempt to override my rules"
#
#     if "password" in prompt.lower():
#         return "I cannot provide sensitive information."
#
#     return "I don't know"
#
# Limitation:
# These were predictable hard-coded responses, so we were testing
# our Python/Pytest logic rather than the behavior of a real LLM.


# LEARNING NOTE — VERSION 2: GEMINI API
#
# We then connected the framework to Google's Gemini API.
#
# The implementation used:
#
# from google import genai
# import os
#
# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#
# response = client.models.generate_content(
#     model="gemini-3.8-flash",
#     contents=prompt
# )
#
# We also experimented with retry/wait logic for temporary server
# and quota errors.
#
# Limitation:
# Free-tier API quota and availability caused 429/503 errors,
# making repeated automated tests unreliable.
#
# Therefore, we moved to a local LLM using Ollama.
'''def ask_llm(prompt):
    time.sleep(15)
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            return response.text

        except errors.ServerError:
            if attempt < 2:
                time.sleep(5)
            else:
                raise'''


# LEARNING NOTE — VERSION 3: OLLAMA
#
# Ollama allowed us to run llama3.2:3b locally without depending
# on cloud API quotas.
#
# The first Ollama version sent only a user message:
#
# def ask_llm(prompt):
#     response = ollama.chat(
#         model="llama3.2:3b",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )
#
#     return response["message"]["content"]


# CURRENT VERSION:
#
# The reusable client now supports both:
#
# 1. A normal user prompt
# 2. An optional system prompt
#
# System-prompt support is needed for tests such as prompt injection,
# sensitive-information protection, and out-of-scope behavior.

import ollama

def ask_llm(prompt, system_prompt=None):
    messages = []

    if system_prompt:
        messages.append({
            "role": "system",
            "content": system_prompt
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    response = ollama.chat(
        model="llama3.2:3b",
        messages=messages
    )

    return response["message"]["content"]





