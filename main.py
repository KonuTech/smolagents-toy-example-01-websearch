import os
import sys

try:
    from smolagents import (
        CodeAgent,
        tool,
        OpenAIServerModel,
        LiteLLMModel,
        DuckDuckGoSearchTool,
    )
except ModuleNotFoundError:
    print("Error: The 'smolagents' module is not installed.")
    print("Please install it using: 'pip install smolagents[litellm]' ")
    sys.exit(1)

from smolagents import (
    tool,
    OpenAIServerModel,
    LiteLLMModel,
    DuckDuckGoSearchTool,
)
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize tools and models
search_tool = DuckDuckGoSearchTool(max_results=5)

model_openai = OpenAIServerModel(
    model_id="qwen2.5:7b",
    api_base="http://localhost:11434/v1/",
    api_key="ollama",
)

model_litellm = LiteLLMModel(
    model_id="ollama/qwen2.5:7b",
    api_base="http://localhost:11434",
    api_key="ollama",
)

# Select model based on environment variable
model_env_var = os.getenv("SMOLAGENTS_MODEL")
if model_env_var is None:
    print("Warning: SMOLAGENTS_MODEL environment variable not set. Defaulting to OpenAIServerModel.")
    model = model_openai
elif model_env_var == "LiteLLM":
    model = model_litellm
elif model_env_var == "OpenAI":
    model = model_openai
else:
    print(f"Warning: Invalid value for SMOLAGENTS_MODEL: {model_env_var}. Defaulting to OpenAIServerModel.")
    model = model_openai

# Initialize agent
agent = CodeAgent(tools=[search_tool], model=model)

def main():
    """Main entry point for the script."""
    if len(sys.argv) > 1:
        agent.run(sys.argv[1])
    else:
        print("Please provide an argument")

if __name__ == "__main__":
    main()

# example usage:
# SMOLAGENTS_MODEL="LiteLLM" python main.py "What is the capital of France?"
# SMOLAGENTS_MODEL="LiteLLM" python main.py "Write a function to calculate the factorial of a number."
# SMOLAGENTS_MODEL="LiteLLM" python main.py "What is the weather like today?"
# SMOLAGENTS_MODEL="LiteLLM" python main.py "What is the latest news on AI?"
