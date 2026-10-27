
"""
Task 2.1: AI Tutor

Uses a local Ollama AI model to explain topics based on the user's learning level.
"""

import time
from langchain.chat_models import init_chat_model

# Create the model once to avoid unnecessary initialization.
llm = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.2
)

# Clean user input to remove unwanted spaces.
topic = input("Topic: ").strip()
level = input("Level (beginner or expert): ").strip()

# The system message controls the AI's role and answer style.
system_text = (
    f"You are a helpful AI tutor. Explain topics at a {level} level. "
    "Answer in 3 short lines."
)

# Send the system instructions and user question to the model.
response = llm.invoke([
    {"role": "system", "content": system_text},
    {"role": "user", "content": f"Explain {topic}."}
])

print("\nAI Tutor:")
print(response.text)

# Convert Ollama's duration from nanoseconds to seconds.
seconds = response.response_metadata["total_duration"] / 1_000_000_000

# Handle missing token metadata safely.
total_tokens = (response.usage_metadata or {}).get("total_tokens", 0)

print(f"\n{total_tokens} tokens in {seconds:.1f} seconds")
