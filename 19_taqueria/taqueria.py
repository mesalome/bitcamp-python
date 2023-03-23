def main():
    taqueria()

def taqueria():
    n = 0
    items = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }
    while True:
        try: 
            user_order = input("Item: ")
            for item in items:
                if user_order.lower() == item.lower():
                    n += float(items[item])
                    print ("Total: $", n)
        except EOFError:
            break

main()