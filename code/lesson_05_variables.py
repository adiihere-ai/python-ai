
"""
Task 1.5: AI Model Profile Card

Displays an AI model's details and estimates
chat usage costs based on token consumption.
"""

# Model details are stored separately to make the profile easy to update.
model_name = "gemma3:1b"
context_window = 32768
price_per_1k_tokens = 0.0
runs_locally = True

print("========== AI MODEL PROFILE ==========\n")

print(f"Model Name: {model_name} | Type: {type(model_name)}")
print(f"Context Window: {context_window} | Type: {type(context_window)}")
print(f"Price per 1K Tokens: PKR {price_per_1k_tokens} | Type: {type(price_per_1k_tokens)}")
print(f"Runs Locally: {runs_locally} | Type: {type(runs_locally)}")

# Token usage is needed to estimate the cost of each conversation.
tokens_per_chat = int(input("\nEnter tokens per chat: "))

chat_cost = (tokens_per_chat / 1000) * price_per_1k_tokens

print(f"Estimated Cost per Chat: PKR {round(chat_cost, 2)}")

# Daily chat volume helps estimate expenses over a 30-day period.
chats_per_day = int(input("Enter chats per day: "))

monthly_cost = chat_cost * chats_per_day * 30

print(f"Estimated Monthly Cost: PKR {round(monthly_cost, 2)}")
