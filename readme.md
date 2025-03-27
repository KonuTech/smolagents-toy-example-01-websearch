Agent Websearch Tool - a toy Example

1:
python3 -m venv .venv

2:
source .venv/bin/activate

3:
ollama run qwen2.5:7b

4:
pip install -r requirements.txt

5:
env > .env

6:
SMOLAGENTS_MODEL="LiteLLM" python main.py "What is the capital of France?"
SMOLAGENTS_MODEL="LiteLLM" python main.py "Write a function to calculate the factorial of a number."
SMOLAGENTS_MODEL="LiteLLM" python main.py "What is the weather like today?"
SMOLAGENTS_MODEL="LiteLLM" python main.py "What is the latest news on AI?"
