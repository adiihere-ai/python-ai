
"""
Task 1.8: Business Helper Bot

A simple rule-based chatbot for an AI automation business.
It answers common questions and prepares AI prompts for
questions it cannot understand.
"""

# Asking once makes the conversation more personal.
name = input("Enter your name: ").strip().title()

message_count = 0
unanswered_count = 0

print(f"\nWelcome, {name}!")
print("Welcome to AI Automation Services.")
print("Ask a question or type 'bye' to exit.")

while True:
    # Cleaning messages helps recognize different capitalizations and spaces.
    message = input("\nYou: ").strip().lower()

    if message == "":
        print("Bot: Please type a question.")
        continue

    message_count = message_count + 1

    if message == "bye":
        print(f"Bot: Goodbye, {name}!")
        break

    # Complaints are checked first so urgent issues get priority.
    elif "late" in message or "complaint" in message:
        print("Bot: Sorry about that. Our manager will call you.")

    elif message == "hi" or message.startswith("hi ") or message == "hello":
        print(f"Bot: Hello, {name}! How can I help you?")

    elif "hours" in message or "open" in message:
        print("Bot: We are open Monday to Saturday, 9 AM to 6 PM.")

    elif "fee" in message or "price" in message or "cost" in message:
        print("Bot: Our service fees start from PKR 5,000.")

    elif "services" in message or "automation" in message:
        print("Bot: We offer AI chatbots and business automation.")

    elif "track" in message or "order status" in message:
        print("Bot: Please contact our support team for your order status.")

    else:
        unanswered_count = unanswered_count + 1

        # Unknown questions become prompts for an AI model in Module 2.
        ai_prompt = f"Answer this customer question about AI services: {message}"

        print("Bot: I don't have an answer for that yet.")
        print(f"AI Prompt: {ai_prompt}")

print("\n========== CHAT SUMMARY ==========")
print(f"Customer: {name}")
print(f"Total Messages: {message_count}")
print(f"Unanswered Questions: {unanswered_count}")
