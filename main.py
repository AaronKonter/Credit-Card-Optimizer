def categories():
    data = {
        'dining': {'amex': '4x points', 'chase freedom': '3% cash back', 'chase sapphire preferred': '3x points'},
        'grocery': {'amex': '4x points', 'bonvoy': '3x points'},
        'everything_else': {'amex': '1x points', 'bonvoy': '2x points'},
        'gas_station': {'bonvoy': '3x points'},
        'drug_store': {'chase freedom': '3% cash back'},
        'online_grocery': {'chase sapphire preferred': '3x points'},
        'streaming_service': {'chase sapphire preferred': '3x points'},
    }

    return data


def category_check(data):
    if is_category == 'y':
        data = input('Which category is it?: ')

        return data
    else:
        print('Find a category in the data.')
        exit()


def optimizer(purchase_type, data):
    purchase_type = purchase_type.lower()
    purchase_type = purchase_type.replace(' ', '_')

    if purchase_type in data:
        for k, v in data.items():
            if purchase_type in k:
                for card, reward in v.items():
                    print(f"Your category of {k} using a {card.capitalize()} would give you {reward}.")


if __name__ == "__main__":
    print('Hi! Here are your current benefit categories:')
    for category in categories():
        print(" +" + category)

    is_category = input('Is your purchase in one of these categories? y/n: ')
    response = category_check(is_category)

    optimizer(response, categories())




