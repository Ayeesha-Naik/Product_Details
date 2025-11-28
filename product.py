# product.py

def format_product_info(product_id, name, quantity, price):
    """
    Accepts product details and returns a well-formatted string.
    
    Parameters:
    - product_id: str or int
    - name: str
    - quantity: int
    - price: float
    
    Returns:
    - str: Formatted product information
    """
    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        return "Invalid input for quantity or price."

    return f"Product ID: {product_id}\nName: {name}\nQuantity: {quantity}\nPrice: ${price:.2f}"
