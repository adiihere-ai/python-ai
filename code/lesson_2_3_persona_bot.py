
"""
Task 2.3: Persona Bot with Real Facts

A tuition academy chatbot that uses business facts,
supports different personalities, and provides prices
directly without calling the AI.
"""

from langchain.chat_models import init_chat_model

# Keep model settings in one dictionary for easy updates.
config = {
    "model": "llama3.2",
    "temperature": 0.3,
    "max_messages": 8
}

# These are example academy details for this assignment.
facts = {
    "name": "Bright Future Academy",
    "hours": "Monday to Saturday, 9 AM to 6 PM",
    "location": "Lahore, Pakistan",
    "prices": {
        "maths": 6000,
        "english": 5000,
        "computer": 7000
    }
}

# Each persona changes the tone without changing business facts.
personas = {
    "friendly": "Be warm, helpful, and conversational.",
    "formal": "Be professional, polite, and concise.",
    "sales": "Be enthusiastic and encourage enrollment without inventing offers."
}

llm = init_chat_model(
    config["model"],
    model_provider="ollama",
    temperature=config["temperature"]
)

current_persona = "friendly"
style = personas[current_persona]

# The system message provides the business facts and limits unsupported claims.
rules = (
    f"You are an assistant for {facts['name']}. "
    f"Location: {facts['location']}. "
    f"Opening hours: {facts['hours']}. "
    f"Available subjects and monthly prices in PKR: {facts['prices']}. "
    "Only use these facts. "
    "If information is missing, say you do not know. "
    "Keep answers short."
)

messages = [
    {"role": "system", "content": f"{rules} Your style: {style}."}
]

print(f"Welcome to {facts['name']}!")
print("Commands: /persona friendly|formal|sales, /price item, /add item price, /count, /reset, bye")

while True:
    text = input("\nYou: ").strip()

    if text == "":
        print("Please enter a question.")
        continue

    if text.lower() == "bye":
        print("Goodbye!")
        break

    elif text.lower() == "/reset":
        messages = [messages[0]]
        print("Conversation memory cleared.")
        continue

    elif text.lower() == "/count":
        print(f"Messages in memory: {len(messages)}")
        continue

    elif text.lower().startswith("/persona "):
        name = text[9:].strip().lower()
        style = personas.get(name, personas["friendly"])

        current_persona = name if name in personas else "friendly"
        messages[0]["content"] = f"{rules} Your style: {style}."

        print(f"Persona changed to {current_persona}.")
        continue

    elif text.lower().startswith("/price "):
        item = text[7:].strip().lower()

        # Dictionary lookup provides an exact price without an AI call.
        if item in facts["prices"]:
            print(f"{item.title()}: PKR {facts['prices'][item]}")
        else:
            print("Sorry, this subject is not on our menu.")
        continue

    elif text.lower().startswith("/add "):
        parts = text[5:].strip().split()

        # Validate the price before adding it to the dictionary.
        if len(parts) == 2 and parts[1].isdigit():
            item = parts[0].lower()
            price = int(parts[1])

            facts["prices"][item] = price

            # Refresh the facts so the AI receives the new price.
            rules = (
                f"You are an assistant for {facts['name']}. "
                f"Location: {facts['location']}. "
                f"Opening hours: {facts['hours']}. "
                f"Available subjects and monthly prices in PKR: {facts['prices']}. "
                "Only use these facts. "
                "If information is missing, say you do not know. "
                "Keep answers short."
            )

            messages[0]["content"] = f"{rules} Your style: {style}."
            print(f"Added {item.title()} for PKR {price}.")
        else:
            print("Usage: /add subject price (example: /add biology 5000)")
        continue

    # Send normal questions with the recent conversation history.
    messages.append({"role": "user", "content": text})
    messages = [messages[0]] + messages[1:][-config["max_messages"]:]

    response = llm.invoke(messages)
    answer = response.text

    print(f"\nBot: {answer}")

    messages.append({"role": "assistant", "content": answer})
    messages = [messages[0]] + messages[1:][-config["max_messages"]:]
