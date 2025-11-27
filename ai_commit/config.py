import os
import json

CONFIG_PATH = os.path.expanduser("~/.ai-commit-config.json")

DEFAULT_CONFIG = {
    "model": "gemini-2.5-flash",
    "commit_style": "conventional",
    "tone": "developer",
    "api_key": None  # New field for the key
}

def load_config():
    """Load user config, falling back to defaults."""
    if not os.path.exists(CONFIG_PATH):
        return DEFAULT_CONFIG.copy()

    try:
        with open(CONFIG_PATH, "r") as f:
            user_cfg = json.load(f)
            return {**DEFAULT_CONFIG, **user_cfg}
    except:
        return DEFAULT_CONFIG.copy()

def save_config(config_dict):
    """Write config to ~/.ai-commit-config.json."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(config_dict, f, indent=2)