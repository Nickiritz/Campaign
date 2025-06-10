# Campaign AI

This project provides a simple CLI utility to generate Danish marketing materials.

Features:
- Selects products from a JSON database using a theme keyword.
- Generates campaign text using the OpenAI API if available (falls back to mocked responses otherwise).
- Creates a PDF catalog of selected products using `fpdf`.

## Usage

```
python -m campaign_ai.cli products.json "Sommer" --limit 5 --output catalog.pdf
```

See `sample_products.json` for the expected product format.
