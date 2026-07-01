def calculate_total(coffee, tea, sandwich):
    total = (coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)
    return total


def print_receipt(name, coffee, tea, sandwich, total):
    print("\n===== RECEIPT =====")
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("--------------------")
    print(f"Total = RM {total:.2f}")