import click
import subprocess
import os
import sys

# 🔇 SILENCE GOOGLE LOGS
os.environ["GRPC_VERBOSITY"] = "NONE"  
os.environ["GLOG_minloglevel"] = "3" 
os.environ["ABSL_LOG_LEVEL"] = "fatal"

# Ensure these imports match your folder structure
from commit_genie.git_reader import get_staged_diff
from commit_genie.model import generate_commit_message_local
from commit_genie.config import load_config, save_config


@click.group()
@click.version_option()
def cli():
    """AI Commit - Generate commit messages using."""
    pass


# -----------------------------------------------------
# ⚙️ CONFIG COMMAND
# -----------------------------------------------------
@cli.command()
@click.option("--key", help="Set your Google Gemini API Key.")
@click.option("--model", help="Default model (e.g. gemini-2.5-flash).")
@click.option("--tone", type=click.Choice(["developer", "manager"]), help="Default tone.")
@click.option("--style", type=click.Choice(["conventional", "natural"]), help="Default commit style.")
def config(key, model, tone, style):
    """Configure API keys and defaults."""
    cfg = load_config()

    if key:
        # Clean the key just in case user pasted quotes or spaces
        clean_key = key.strip().replace('"', '').replace("'", "")
        cfg["api_key"] = clean_key
        click.echo("🔑 API Key saved!")
    
    if model:
        cfg["model"] = model
    if tone:
        cfg["tone"] = tone
    if style:
        cfg["commit_style"] = style

    save_config(cfg)
    click.echo("✅ Configuration updated.")


# -----------------------------------------------------
# 🧠 MAIN COMMIT COMMAND
# -----------------------------------------------------
@cli.command()
@click.option("--type", "commit_type", default=None, help="Force commit type (feat, fix, etc.)")
@click.option("--model", help="Override default model.")
@click.option("--tone", type=click.Choice(["developer", "manager"]), help="Override tone.")
@click.option("--style", type=click.Choice(["conventional", "natural"]), help="Override style.")
@click.option("--auto", is_flag=True, help="Automatically commit without confirmation.")
def commit(commit_type, model, tone, style, auto):
    """Generate commit message and commit changes."""

    # -------------------------------
    # 1. Load Config & Check Key
    # -------------------------------
    cfg = load_config()
    api_key = cfg.get("api_key")

    if not api_key:
        click.echo("⚠️ Google API Key not found!")
        click.echo("Get a free key here: https://aistudio.google.com/app/apikey")
        
        # Ask for key securely
        api_key_input = click.prompt("Paste your API Key here", hide_input=True)
        
        # Clean input (remove accidental spaces or quotes from copy-paste)
        api_key = api_key_input.strip().replace('"', '').replace("'", "")
        
        # Save immediately
        cfg["api_key"] = api_key
        save_config(cfg)
        click.echo("✅ Key saved safely.")

    # -------------------------------
    # 2. Determine Settings (CLI Override > Config > Default)
    # -------------------------------
    final_model = model or cfg.get("model", "gemini-2.5-flash")
    final_tone = tone or cfg.get("tone", "developer")
    final_style = style or cfg.get("commit_style", "conventional")

    # -------------------------------
    # 3. Read Staged Changes
    # -------------------------------
    diff_text = get_staged_diff()

    if not diff_text.strip():
        click.echo("⚠️ No staged changes found. Run 'git add' first.")
        return

    # -------------------------------
    # 4. Generate Message
    # -------------------------------
    click.echo(f"🧠 Generating message ({final_tone}/{final_style})...")

    msg = generate_commit_message_local(
        diff_text=diff_text,
        api_key=api_key,
        model=final_model,
        commit_type=commit_type,
        commit_style=final_style,
        tone=final_tone
    )

    # Format the output
    title = msg.get("title", "chore: update code")
    body_list = msg.get("body", [])
    body = "\n".join(f"- {b}" for b in body_list)

    full_message = f"{title}\n\n{body}" if body else title

    # -------------------------------
    # 5. Preview & Confirm
    # -------------------------------
    click.echo("\n" + "="*30)
    click.echo(click.style(title, fg="green", bold=True))
    if body:
        click.echo(body)
    click.echo("="*30 + "\n")

    if auto or click.confirm("Commit this message?"):
        run_commit(full_message)
    else:
        click.echo("❌ Canceled.")


# -----------------------------------------------------
# 🧱 HELPER: Run git commit safely
# -----------------------------------------------------
def run_commit(full_message):
    try:
        # We use --no-verify to prevent infinite loops if the user
        # has other git hooks installed.
        subprocess.run(
            ["git", "commit", "-m", full_message, "--no-verify"],
            check=True
        )
        click.echo("✅ Commit created!")
    except subprocess.CalledProcessError as e:
        click.echo(f"❌ Git commit failed: {e}")


if __name__ == "__main__":
    cli()