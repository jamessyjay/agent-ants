from pathlib import Path

PROMPT_DIR = Path("prompts")
DEFAULT_PROMPT_FILE = PROMPT_DIR / "default.txt"

def load_prompt(agent_name: str) -> str:
    """Load a system prompt for a specific agent.
    
    This function attempts to load a system prompt from a text file in the 'prompts'
    directory. If the file doesn't exist, a default prompt is returned.
    
    Args:
        agent_name (str): The name of the agent whose prompt to load
        
    Returns:
        str: The system prompt for the agent, or a default prompt if the file doesn't exist
    """
    prompt_file = PROMPT_DIR / f"{agent_name}.txt"
    if prompt_file.exists():
        return prompt_file.read_text(encoding="utf-8")
    return ""

def load_default_prompt() -> str:
    """Load the default system prompt."""
    return DEFAULT_PROMPT_FILE.read_text(encoding="utf-8")

def read_prompt_file(name: str) -> str:
    """Read a prompt file and return its content."""
    file_path = PROMPT_DIR / f"{name}.txt"
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    raise FileNotFoundError(f"Prompt file {file_path} does not exist.")