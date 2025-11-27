import google.generativeai as genai
import json

def generate_commit_message_local(
    diff_text: str,
    api_key: str,
    model: str = "gemini-2.5-flash",
    commit_type: str = None,
    commit_style: str = "conventional",
    tone: str = "developer"
) -> dict:
    """
    Generate commit message with advanced
    customization for commit type, style, and tone.
    """
    
    if not api_key:
        return {"title": "Error", "body": ["API Key is missing. Run 'ai-commit config --key YOUR_KEY'"]}

    # -------------------------------------------------------
    # 1. Restore the detailed definitions (from your original code)
    # -------------------------------------------------------
    
    style_instruction = ""
    if commit_style == "conventional":
        style_instruction = (
            "STYLE: Follow 'Conventional Commits' strictly. "
            "Format: <type>(<scope>): <description>. "
            "Types: feat, fix, docs, style, refactor, test, chore, ci, perf."
        )
    else:
        style_instruction = (
            "STYLE: Write a natural, clear commit summary like a human developer. "
            "Do not use prefixes like 'feat:' or 'fix:' unless necessary."
        )

    tone_instruction = ""
    if tone == "developer":
        tone_instruction = (
            "TONE: Technical, concise, and direct. Use active verbs. "
            "Focus on 'what' changed and 'why' in technical terms."
        )
    else: # manager
        tone_instruction = (
            "TONE: High-level and descriptive. Avoid heavy jargon. "
            "Focus on business value, user impact, and the 'big picture'."
        )

    type_instruction = ""
    if commit_type:
        type_instruction = f"CONSTRAINT: You MUST use the commit type '{commit_type}'."
    else:
        type_instruction = "TASK: Analyze the diff and infer the most appropriate commit type (feat, fix, chore, etc)."

    # -------------------------------------------------------
    # 2. Build the "Mega Prompt"
    # -------------------------------------------------------
    prompt = f"""
    You are an expert Git Commit Assistant.

    {style_instruction}
    {tone_instruction}
    {type_instruction}

    RULES:
    - Title must be 50-72 characters max.
    - Body must be a bullet list (2-5 points).
    - NEVER mention filenames explicitly in the title.
    - OUTPUT MUST BE PURE JSON.

    Required JSON Structure:
    {{
      "type": "<inferred or forced type>",
      "title": "<the commit title>",
      "body": ["<bullet point 1>", "<bullet point 2>"]
    }}

    Here is the git diff:
    {diff_text[:15000]} 
    """
    # Note: Gemini Flash can handle massive diffs (1M tokens), 
    # so we raised the limit from 4000 to 15000 chars safely.

    # -------------------------------------------------------
    # 3. Call the API
    # -------------------------------------------------------
    try:
        genai.configure(api_key=api_key)
        model_instance = genai.GenerativeModel(model)

        response = model_instance.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )

        return json.loads(response.text)

    except Exception as e:
        return {
            "type": "chore",
            "title": "chore: manual commit (AI Error)",
            "body": [f"Error: {str(e)}", "Please check your API key or internet connection."]
        }