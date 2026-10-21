
"""
Task 1.6: Prompt Cleaner

Cleans user input, analyzes question length,
and generates a structured AI prompt.
"""

# Cleaning input improves readability and consistency.
name = input("Enter your name: ").strip().title()
question = input("Enter your question: ").strip().capitalize()

# Replacing inappropriate language makes the prompt more professional.
question = question.replace("stupid", "unclear")

# Estimating tokens helps predict AI usage costs.
characters = len(question)
estimated_tokens = round(characters / 4)
mentions_python = "python" in question.lower()

# Limiting the question keeps the final prompt concise.
clean_question = question[:150]

prompt = f"""
========== AI PROMPT ==========

User: {name}
Question: {clean_question}

Please provide a clear, accurate, and beginner-friendly answer.
"""

print("\n========== PROMPT ANALYSIS ==========")
print(f"Name: {name}")
print(f"Characters: {characters}")
print(f"Estimated Tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")

print(prompt)

# A sample token rate demonstrates how AI usage costs can be estimated.
price_per_1k_tokens = 0.50
estimated_cost = (estimated_tokens / 1000) * price_per_1k_tokens

print(f"Estimated Cost: PKR {estimated_cost:.2f}")
