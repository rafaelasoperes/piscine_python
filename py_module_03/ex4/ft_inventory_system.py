import sys


def parse_parameter(param: str):
    i = 0
    colon_count = 0
    colon_index = -1

    while i < len(param):
        if param[i] == ":":
            colon_count += 1
            colon_index = i
        i += 1

    if colon_count != 1:
        return None, None, False

    item = param[:colon_index]
    quantity_str = param[colon_index + 1:]

    if item == "" or quantity_str == "":
        return None, None, False

    return item, quantity_str, True


def main() -> None:
    print("=== Inventory System ===")

    args = sys.argv[1:]
    inventory = {}
    i = 0

    while i < len(args):
        param = args[i]

        item, quantity_str, valid = parse_parameter(param)

        if valid is False:
            print(f"Error - invalid parameter '{param}'")
            i += 1
            continue

        if item in inventory:
            print(f"Redundant item '{item}' discarded")
            i += 1
            continue

        try:
            quantity = int(quantity_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            i += 1
            continue

        inventory.update({item: quantity})
        i += 1

    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of items: {total_quantity}")

    i = 0
    while i < len(item_list):
        item = item_list[i]
        quantity = inventory[item]

        if total_quantity != 0:
            percentage = round((quantity * 100) / total_quantity, 1)
        else:
            percentage = 0.0

        print(f"Item {item} represents {percentage}%")
        i += 1

    if len(item_list) > 0:
        most_item = item_list[0]
        least_item = item_list[0]

        i = 1
        while i < len(item_list):
            current_item = item_list[i]

            if inventory[current_item] > inventory[most_item]:
                most_item = current_item

            if inventory[current_item] < inventory[least_item]:
                least_item = current_item

            i += 1

        print(f"Item most abundant: {most_item} with quantity "
              f"{inventory[most_item]}")
        print(f"Item least abundant: {least_item} with quantity "
              f"{inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
