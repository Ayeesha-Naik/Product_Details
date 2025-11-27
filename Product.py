# product.py
import sys

def format_product_info(product_id, name, quantity, price):
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        return "Invalid input for quantity or price."

    return (
        "========== Product Information ==========\n"
        f"Product ID   : {product_id}\n"
        f"Name         : {name}\n"
        f"Quantity     : {quantity}\n"
        f"Price        : ${price:.2f}\n"
        "========================================"
    )

def main():
    if len(sys.argv) != 5:
        print("Usage: python product.py <Product_id> <Product_name> <Quantity> <Price>")
        sys.exit(1)

    product_id, name, quantity, price = sys.argv[1:5]
    result = format_product_info(product_id, name, quantity, price)
    print(result)

if __name__ == "__main__":
    main()
