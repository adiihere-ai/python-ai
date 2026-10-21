
"""
Task 1.7: Smart Model Router

Selects an AI model based on the task type
and estimates the cost of processing tokens.
"""

# Cleaning the input helps recognize task types consistently.
task_type = input("Enter task type (code, private, chat): ").strip().lower()
tokens = int(input("Enter number of tokens: "))
user_plan = input("Enter your plan (free or paid): ").strip().lower()

# Different tasks need different models and pricing.
if task_type == "code":
    model = "Code AI Model"
    price_per_1k_tokens = 0.80
elif task_type == "private":
    model = "Ollama (Local)"
    price_per_1k_tokens = 0.0
elif task_type == "chat":
    model = "Chat AI Model"
    price_per_1k_tokens = 0.40
else:
    model = "Ollama (Local)"
    price_per_1k_tokens = 0.0

cost = (tokens / 1000) * price_per_1k_tokens

# Long requests may exceed a model's preferred input length.
if tokens > 4000:
    print("Warning: Request is too long.")
else:
    print("Length is fine.")

# Free users may need an upgrade for longer requests.
if user_plan == "free" and tokens > 2000:
    print("Upgrade to send long requests.")

print(f"Chosen Model: {model}")
print(f"Estimated Cost: PKR {cost:.2f}")
