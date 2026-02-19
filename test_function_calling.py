from __future__ import annotations

from pathlib import Path

from google import genai
from google.genai import types


def load_api_key() -> str:
    env_path = Path("smart_resume_agent") / ".env"
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("GOOGLE_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("GOOGLE_API_KEY not found")


def main() -> None:
    client = genai.Client(api_key=load_api_key())

    fn = types.FunctionDeclaration(
        name="add",
        description="Add two integers",
        parameters={
            "type": "object",
            "properties": {
                "a": {"type": "integer"},
                "b": {"type": "integer"},
            },
            "required": ["a", "b"],
        },
    )

    tools = [types.Tool(function_declarations=[fn])]

    try:
        resp = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="What is 2+3? Use the add tool.",
            config=types.GenerateContentConfig(tools=tools),
        )
        # Print a minimal view
        print("ok")
        print(resp.text)
    except Exception as e:
        print("error")
        print(type(e).__name__)
        print(str(e))


if __name__ == "__main__":
    main()
