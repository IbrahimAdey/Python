class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def get_total(self):
        return self.price * self.quantity

cart = []

while True:
    name = input("Enter product name (or 'done'): ")
    if name.lower() == 'done':
        break
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    cart.append(Product(name, price, quantity))

total = sum(p.get_total() for p in cart)
vat = total * 0.075
discount = total * 0.10
final_total = total + vat - discount

print("\n=== SEMICOLON STORE INVOICE ===")
for p in cart:
    print(f"{p.name} x{p.quantity} - {p.get_total():.2f}")
print(f"Subtotal: {total:.2f}")
print(f"VAT (7.5%): {vat:.2f}")
print(f"Discount (10%): {discount:.2f}")
print(f"Total Due: {final_total:.2f}")