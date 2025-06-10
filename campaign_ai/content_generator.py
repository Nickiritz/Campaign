from typing import List, Dict
import os

try:
    import openai
except ImportError:  # pragma: no cover - optional dependency
    openai = None


MODEL = os.environ.get("OPENAI_MODEL", "gpt-4")


def generate_text(prompt: str, max_tokens: int = 100) -> str:
    """Generate text using OpenAI API if available."""
    if openai is None:
        return f"[Mocked response for prompt: {prompt[:30]}...]"

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"].strip()


def create_product_blurb(product: Dict) -> str:
    prompt = (
        f"Skriv en kort og salgbar beskrivelse på dansk af produktet '{product.get('title')}'."
    )
    return generate_text(prompt, max_tokens=60)


def create_campaign_title(theme: str) -> str:
    prompt = f"Find på en kreativ dansk kampagnetitel for temaet '{theme}'."
    return generate_text(prompt, max_tokens=10)
