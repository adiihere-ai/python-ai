# Python for AI

**Abdul Ahad** | Python for AI Course

## About This Project

This repository documents my practical learning journey in Python, Generative AI, and AI automation through hands-on exercises and real-world applications.

## Career Goal

To become an **AI Automation Specialist**, developing intelligent solutions that streamline business operations, improve efficiency, and solve real-world challenges.

## How to Run

Run the project using:

```bash
uv run main.py
```

To run an individual lesson:

```bash
uv run code/lesson_08_mini_chatbot.py
```

### Module 2 — AI Applications

**Task 2.1 — AI Tutor**

```bash
uv run code/lesson_2_1_first_ai_call.py
```

**Task 2.2 — Personal Tutor with Memory**

```bash
uv run code/lesson_2_2_chat_memory.py
```

## Lessons Completed

### Module 1 — Python Fundamentals

- **1.1 — AI Career Introduction:** Python variables, f-strings, and career aspirations.
- **1.2 — Toolkit Proof:** Development environment verification and first Ollama interaction.
- **1.3 — Client-Ready Repository:** GitHub repository organization, documentation, and version control.
- **1.4 — Business Prompt Builder:** User input, f-strings, and personalized AI prompt generation.
- **1.5 — AI Model Profile Card:** Python data types, type checking, and AI token cost calculations.
- **1.6 — Prompt Cleaner:** String methods, text formatting, token estimation, and prompt optimization.
- **1.7 — Smart Model Router:** Conditional statements, AI model selection, token limits, and cost estimation.
- **1.8 — Business Helper Bot:** Rule-based chatbot, intent recognition, customer support, fallback AI prompts, and conversation tracking.

### Module 2 — AI Applications

- **2.1 — AI Tutor:** LangChain and Ollama integration, personalized AI explanations, token usage tracking, and response time measurement.
- **2.2 — Personal Tutor with Memory:** Conversation history management, memory limits, reset commands, token tracking, and question summaries.

## Task 1.8 — Business Helper Bot Design

**Business:** AI Automation Services

**Purpose:** To help customers get quick answers about AI services, pricing, business hours, and support requests.

### Intent Design Table

| Intent | Example Customer Message | Expected Bot Response |
|---|---|---|
| Complaint | my order is late | Sorry about that. Our manager will call you. |
| Greeting | hi | Hello! How can I help you? |
| Opening Hours | What are your HOURS? | We are open Monday to Saturday, 9 AM to 6 PM. |
| Fees | how much is the fee | Our service fees start from PKR 5,000. |
| Services | what services do you offer? | We offer AI chatbots and business automation. |
| Order Status | track my order | Please contact our support team for your order status. |
| Unknown Question | which one is best? | Fallback message with an AI prompt for Module 2. |
| Empty Input | (press Enter) | Please type a question. |
| Goodbye | BYE | Goodbye message and conversation summary. |

*Business hours and fees are example values used for this learning project.*

### Chatbot Features

- Cleans customer messages for consistent intent recognition.
- Prioritizes complaints before other requests.
- Answers common business questions using predefined rules.
- Generates AI prompts for unanswered questions.
- Tracks total messages and unanswered questions.
- Displays a conversation summary when the user exits.

## Tools & Technologies

- Python
- uv
- Git & GitHub
- Ollama (`gemma3:1b`, `llama3.2`)
- LangChain
- Visual Studio Code

---

**Author:** Abdul Ahad
**Course:** Python for AI
