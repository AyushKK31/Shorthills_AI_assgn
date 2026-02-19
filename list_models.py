from __future__ import annotations

from pathlib import Path

from google import genai


def load_api_key() -> str:
    env_path = Path("smart_resume_agent") / ".env"
    if not env_path.exists():
        raise SystemExit(f"Missing {env_path}")

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("GOOGLE_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")

    raise SystemExit("GOOGLE_API_KEY not found in smart_resume_agent/.env")


def main() -> None:
    api_key = load_api_key()
    client = genai.Client(api_key=api_key)

    models = list(client.models.list())
    print(f"models: {len(models)}")

    for m in models:
        name = getattr(m, "name", "")
        supported = (
            getattr(m, "supported_actions", None)
            or getattr(m, "supported_generation_methods", None)
            or getattr(m, "supported_methods", None)
        )
        # Keep output compact: name + methods/actions
        print(name, supported)


if __name__ == "__main__":
    main()
