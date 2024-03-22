from schemas import Order


def transform_order(orders):
    products_dict = {}
    total_price=0
    for order in orders:
        total_price+=order["total_price"]
        for product in order["products"]:
            product_name = product["product_name"]
            quantity = product["quantity"]
            price = product["price"]
            if product_name in products_dict:
                products_dict[product_name]["quantity"] += quantity
                products_dict[product_name]["price"] = price
            else:
                products_dict[product_name] = {"quantity": quantity, "price": price}
    lst = [{"product_name": k, "quantity": v["quantity"], "price": v["price"]} for k, v in products_dict.items()]
    result=Order(user_id=orders[0]["external_id"],total_price=total_price,products=lst)
    return result.model_dump()