# LangGraph Agent Memory Layers

LangGraph agents use multiple layers of memory to handle information, context, and reasoning. These memory layers help agents learn, recall, and make decisions efficiently.

---

## 1. Short-Term Memory (STM)
- **Purpose:** Holds information temporarily during an ongoing conversation or task.
- **Characteristics:**
  - Fast access and transient.
  - Cleared or updated frequently.
- **Use Case:** Remembering user input or context within the current session.

---

## 2. Long-Term Memory (LTM)
- **Purpose:** Stores information persistently for future reference.
- **Characteristics:**
  - Durable and retrievable across sessions.
  - Can be updated with new experiences.
- **Use Case:** Storing knowledge, previous interactions, or learned behaviors.

---

## 3. Factual Memory
- **Purpose:** Stores concrete facts and objective knowledge.
- **Characteristics:**
  - Structured and verifiable.
  - Often used for reference or answering factual questions.
- **Use Case:** Remembering definitions, numbers, dates, or established data.

---

## 4. Episodic Memory
- **Purpose:** Stores experiences and events with context.
- **Characteristics:**
  - Includes “what,” “when,” and “where” of events.
  - Helps agent learn from past experiences.
- **Use Case:** Remembering specific conversations, user preferences, or previous actions.

---

## 5. Semantic Memory
- **Purpose:** Stores meanings, concepts, and relationships.
- **Characteristics:**
  - Abstract knowledge rather than concrete events.
  - Supports reasoning, inference, and understanding.
- **Use Case:** Understanding concepts, relationships between entities, or generalized knowledge.

---

## Summary
| Memory Layer       | Purpose                                  | Example Use Case                              |
|-------------------|------------------------------------------|-----------------------------------------------|
| Short-Term Memory | Temporary context during tasks           | Current conversation context                  |
| Long-Term Memory  | Persistent knowledge and experiences     | User history, learned behaviors               |
| Factual Memory    | Objective, verifiable information        | Dates, numbers, facts                          |
| Episodic Memory   | Contextual experiences and events        | Previous conversations or actions             |
| Semantic Memory   | Concepts, meanings, and relationships   | Understanding concepts or entity relationships|

---

**References:**
- LangGraph Documentation: [https://www.langgraph.com/docs](https://www.langgraph.com/docs)
- Memory in AI Agents: S. Franklin, “Artificial Minds” (2014)



## configuration of MEM0
