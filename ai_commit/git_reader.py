from git import Repo
from pathlib import Path

def get_staged_diff(repo_path: str = ".") -> str:
    """Return the diff text for staged changes."""
    repo = Repo(Path(repo_path).resolve())
    if repo.is_dirty(index=True, working_tree=False):
        diff_text = repo.git.diff("--cached")
        return diff_text
    return ""
