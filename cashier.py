def get_invoice_items(items):
    invoice_items = [] 
    for item in items:
        item_quantity = item["quantity"]
        item_name = item["name"]
        item_subtotal = item["quantity"]*item["price"]
        values = f"{item_quantity} {item_name} {item_subtotal}KD"
        invoice_items.append(values)
    return invoice_items
    ...


def get_total(items):
    total = 0
    subtotals = []
    for item in items:
        item_subtotal = item["quantity"]*item["price"]
        subtotals.append(item_subtotal)
    total = sum(subtotals)
    return total
    ...


def print_receipt(invoice_items, total):
    print("""\
-------------------
receipt
-------------------""")
    for count,ele in enumerate(invoice_items):
        print(ele)
    print("-------------------")
    print(f'Total price: {total}KD')
    ...


def main():
    items = []
    while True:
        item_name = input("Item (enter \"done\" when finished):")
        if item_name == "done":
            break
        else:
            item_price = float(input("Item price:"))
            item_quantity = int(input("Item quantity:"))
            items.append({'name':item_name,'price':item_price,'quantity':item_quantity})
    invoice_items = get_invoice_items(items)
    total = get_total(items)
    print_receipt(invoice_items, total)
    ...


if __name__ == "__main__":
    main()
