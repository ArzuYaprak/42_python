import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = {}
    i = 1

    while i < len(sys.argv):
        argument = sys.argv[i]
        i += 1

        try:
            item_key, item_value = argument.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{argument}'")
            continue

        if item_key == "" or item_value == "":
            print(f"Error - invalid parameter '{argument}'")
            continue

        if item_key in inventory:
            print(f"Redundant item '{item_key}' - discarding")
            continue

        try:
            quantity = int(item_value)
        except ValueError as error:
            print(f"Quantity error for '{item_key}': {error}")
            continue

        inventory[item_key] = quantity

    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    if len(inventory) > 0:
        i = 0
        while i < len(item_list):
            item_key = item_list[i]
            if total_quantity == 0:
                percentage = 0.0
            else:
                percentage = round(
                    inventory[item_key] / total_quantity * 100, 1
                )
            print(f"Item {item_key} represents {percentage}%")
            i += 1

        most_item = item_list[0]
        least_item = item_list[0]
        i = 1
        while i < len(item_list):
            item_key = item_list[i]

            if inventory[item_key] > inventory[most_item]:
                most_item = item_key
            if inventory[item_key] < inventory[least_item]:
                least_item = item_key
            i += 1

        print(
            f"Item most abundant: {most_item} "
            f"with quantity {inventory[most_item]}"
        )
        print(
            f"Item least abundant: {least_item} "
            f"with quantity {inventory[least_item]}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
