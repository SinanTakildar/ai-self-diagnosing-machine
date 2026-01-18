# AI Self-Diagnosing Machine 🛠️

An intelligent diagnostic layer that translates cryptic machine error codes into human-readable repair instructions using Python and RAG (Retrieval-Augmented Generation).

## How it Works
1. **Log Monitoring**: Python reads raw error logs (e.g., `Error 0x45B`).
2. **Context Injection**: The script retrieves relevant troubleshooting steps from a technical manual.
3. **LLM Translation**: OpenAI GPT interprets the data to provide clear "Fix-it" steps for operators.

## Tech Stack
- Python
- OpenAI API (GPT-4)
- RAG (Knowledge Base Integration)