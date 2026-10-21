
"""
Task 1.4: Business Prompt Builder

Generates a personalized AI prompt using business information
provided by the user.
"""

# User-specific information helps make the AI prompt relevant.
name = input("Enter your name: ").strip()
business = input("Enter your business type: ").strip()
problem = input("Enter your biggest business problem: ").strip()

# A clear and structured prompt helps AI provide focused solutions.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(f"\nWelcome, {name}!")
print(f"\n{prompt}")
