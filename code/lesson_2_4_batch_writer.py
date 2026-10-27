
"""
Task 2.4: Batch Writer

Generates AI descriptions for academy courses using a loop.
Skips unavailable courses and tracks total tokens and time.
"""

from langchain.chat_models import init_chat_model

# Store course names and monthly fees in one dictionary.
products = {
    "Maths": 6000,
    "English": 5000,
    "Computer": 7000,
    "Physics": 6500,
    "Chemistry": 5500,
    "Old Evening Batch": 0
}

# Create the AI model once before starting the loop.
llm = init_chat_model(
    "llama3.2",
    model_provider="ollama",
    temperature=0.3
)

# Store generated descriptions and track total usage.
results = []
total_tokens = 0
total_seconds = 0

# Process each course and its price.
for name, price in products.items():

    # Skip unavailable courses without calling the AI.
    if price == 0:
        print(f"Skipping {name}: Not available.")
        continue

    print(f"Generating description for {name}...")

    # Ask the AI to write one sentence using the provided facts.
    response = llm.invoke(
        f"Write one short promotional sentence for the "
        f"{name} course at Bright Future Academy. "
        f"The monthly fee is PKR {price}. "
        "Use only these facts. Do not invent discounts or guarantees."
    )

    # Save each generated description with its course and price.
    results.append({
        "item": name,
        "price": price,
        "text": response.text
    })

    # Add token usage and processing time across all AI calls.
    total_tokens += (response.usage_metadata or {}).get("total_tokens", 0)
    total_seconds += response.response_metadata.get("total_duration", 0) / 1_000_000_000

# Print all generated descriptions as a numbered list.
print("\n========== COURSE DESCRIPTIONS ==========")

for number, row in enumerate(results, start=1):
    print(f"\n{number}. {row['item']} - PKR {row['price']}/month")
    print(f"   {row['text']}")

# Show the total descriptions, tokens, and processing time.
print("\n========== SUMMARY ==========")
print(f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")
