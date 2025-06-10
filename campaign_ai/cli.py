import argparse
from .product_selector import load_products, select_products
from .content_generator import create_campaign_title, create_product_blurb
from .pdf_generator import generate_catalog


def main():
    parser = argparse.ArgumentParser(description="Generate marketing campaign materials")
    parser.add_argument("product_file", help="Path to JSON file with products")
    parser.add_argument("theme", help="Campaign theme")
    parser.add_argument("--limit", type=int, default=10, help="Limit number of products")
    parser.add_argument("--output", default="catalog.pdf", help="Output PDF file")
    args = parser.parse_args()

    products = load_products(args.product_file)
    selected = select_products(products, args.theme, limit=args.limit)

    title = create_campaign_title(args.theme)
    for p in selected:
        p["description"] = create_product_blurb(p)

    generate_catalog(selected, args.output, title)
    print(f"Generated {args.output} with {len(selected)} products")


if __name__ == "__main__":
    main()
