ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def select_max_fit(diff):
    min_cost = min([item["cost"] for item in ITEMS.values()])
    if diff < min_cost:
        return None

    calorie_intake_per_product = {
        k: ITEMS[k]["calories"] / ITEMS[k]["cost"] for k in ITEMS
    }
    while calorie_intake_per_product:
        item = max(
            calorie_intake_per_product, key=lambda k: calorie_intake_per_product[k]
        )
        if ITEMS[item]["cost"] <= diff:
            return item
        else:
            calorie_intake_per_product.pop(item)


def final_calorie_intake(products):
    return sum(
        [ITEMS[item]["calories"] * quantity for item, quantity in products.items()]
    )


def find_food_greedy(total_cost):
    if not total_cost:
        return {}

    current = 0
    result = {}

    while current <= total_cost:
        item = select_max_fit(total_cost - current)
        if not item:
            break
        current += ITEMS[item]["cost"]
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return (result, final_calorie_intake(result))


def find_food_dynamic(total_cost):
    calorie_intake_variants = [0] * (total_cost + 1)
    result = [{} for _ in range(total_cost + 1)]

    for i in range(1, total_cost + 1):
        for item, info in ITEMS.items():
            if (
                info["cost"] <= i
                and calorie_intake_variants[i]
                < calorie_intake_variants[i - info["cost"]] + info["calories"]
            ):
                calorie_intake_variants[i] = (
                    calorie_intake_variants[i - info["cost"]] + info["calories"]
                )
                result[i] = result[i - info["cost"]].copy()
                result[i][item] = result[i].get(item, 0) + 1

    return (result[total_cost], final_calorie_intake(result[total_cost]))


if __name__ == "__main__":
    amount = 643

    print("------------------------------------------------------")
    print("Products selection by greedy algo")
    print("------------------------------------------------------")
    products, calories = find_food_greedy(amount)
    print("Products:", products)
    print("Calories:", calories)
    print("------------------------------------------------------")

    print()

    print("------------------------------------------------------")
    print("Products selection by dynamic algo")
    print("------------------------------------------------------")
    products, calories = find_food_dynamic(amount)
    print("Products:", products)
    print("Calories:", calories)
    print("------------------------------------------------------")
