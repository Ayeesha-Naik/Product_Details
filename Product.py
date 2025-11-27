def format_product_info(product_id: str, name: str, quantity: int, price: float) -> str:
    """
    Create a human-readable summary of product details.

    Args:
        product_id (str): Unique identifier for the product.
        name (str): Name of the product.
        quantity (int): Quantity in stock.
        price (float): Price per unit.

    Returns:
        str: Formatted product information.
    """

    # Basic validation to prevent CI pipeline failures
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return (
        "Product Information:\n"
        f"ID        : {product_id}\n"
        f"Name      : {name}\n"
        f"Quantity  : {quantity}\n"
        f"Price     : ${price:.2f}\n"
    )


if _name_ == "_main_":
    # Simple test to ensure Jenkins CI runs the file without errors
    print(format_product_info("P1001", "Sample Product", 10, 19.99))
