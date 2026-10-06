#This is how I first connected Python to Ollama.
import ollama

response = ollama.chat(model="llama3.2:3b", messages=[{"role": "user",
                                                       "content": "What is the capital of France?"}])

print(response["message"]["content"])

