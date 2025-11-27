import pytest
from product import format_product_info

def test_format_product_info_output():
    """Test that the function returns a correctly formatted string."""
    result = format_product_info("P123", "Widget", 5, 9.99)

    assert "product information" in result
    assert "ID:    P123" in result
    assert "Name:  Widget" in result
    assert "Qty:   5" in result
    assert "Price: $9.99" in result


def test_negative_quantity_raises_error():
    """Quantity must not be negative."""
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        format_product_info("P123", "Widget", -1, 9.99)


def test_negative_price_raises_error():
    """Price must not be negative."""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        format_product_info("P123", "Widget", 5, -9.99)


def test_price_formatting():
    """Price should be rounded to two decimal places."""
    result = format_product_info("P123", "Widget", 5, 9.999)
    assert "Price: $10.00" in result