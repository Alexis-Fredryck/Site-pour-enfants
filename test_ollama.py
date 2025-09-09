import ollama

response = ollama.chat(
    model="gemma3:4b",
    messages=[{"role": "user", "content": "Ecris-moi une phrase"}]
)

print(response["message]["content])