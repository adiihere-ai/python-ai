
"""
Task 2.2: Personal Tutor with Memory

A chatbot that remembers recent conversations,
supports memory commands, and tracks user questions.
"""

from langchain.chat_models import init_chat_model

# Create the AI model only once.
llm = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.2
)

MAX_MESSAGES = 8

# Keep the tutor's instructions at the beginning of every conversation.
messages = [
    {
        "role": "system",
        "content": "You are a friendly AI tutor. Give clear and short answers."
    }
]

# Store questions separately for the final summary.
questions = []

print("AI Tutor with Memory")
print("Commands: /reset, /count, bye")

while True:
    text = input("\nYou: ").strip()

    if text == "":
        print("Please enter a question.")
        continue

    if text.lower() == "bye":
        print("Goodbye!")
        break

    elif text.lower() == "/reset":
        # Keep the tutor's role but remove previous conversation messages.
        messages = [messages[0]]
        print("Memory cleared.")
        continue

    elif text.lower() == "/count":
        print(f"Messages in memory: {len(messages)}")
        continue

    # Save the user's question before sending it to the AI.
    messages.append({"role": "user", "content": text})

    # Keep the system message and only the last 8 conversation messages.
    messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]

    response = llm.invoke(messages)
    answer = response.text

    print(f"\nTutor: {answer}")

    # Save the AI response so the next question has conversation context.
    messages.append({"role": "assistant", "content": answer})
    messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]

    # Handle missing token metadata safely.
    input_tokens = (response.usage_metadata or {}).get("input_tokens", 0)
    print(f"Input Tokens: {input_tokens}")

    # Track questions for the stretch-task summary.
    questions.append(text)

# Print the question summary after leaving the loop.
print("\n========== CHAT SUMMARY ==========")
print(f"Total Questions: {len(questions)}")

if len(questions) > 0:
    print(f"First Question: {questions[0]}")
    print(f"Last Question: {questions[-1]}")
