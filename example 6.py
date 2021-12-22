# Задание 6
product = {
    "Наименование": str,
    "Цена": int,
    "Колличество": int,
    "Еденица измерения": str,
}
product_list = []
product_counter = 1

while True:
    decision = input(f"Товар = {len(product_list)}, записать? [y/n]").lower()
    if decision == 'n':
        break
    else:
        product_info = {}
        for property_name, property_type in product.items():
            user_input = input(f"Запишите в поле'{property_name}':  ")
            product_info[property_name] = property_type(user_input)

        product_list.append((product_counter, product_info))
        product_counter += 1
product_analytics = {}
for analytics_key in product.keys():
    item_list = []
    for unit in product_list:
        item_list.append(unit[1][analytics_key])
    product_analytics[analytics_key] = item_list
print(product_analytics)
