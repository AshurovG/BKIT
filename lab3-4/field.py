goods = [
    {'title': 'Ковер', 'price': 1500, 'color': 'green', 'amount': 200},
    {'title': 'Диван для отдыха', 'price': 5000, 'color': 'yellow', 'amount': 50},
    {'title': 'Стол маленький', 'price': 2500, 'color': 'white', 'amount': 100},
    {'title': 'Ваза для цветов', 'price': 1000, 'color': 'blue', 'amount': 350},
]


def field(items, *args):
    try:
        assert len(args) > 0
        r = [{} for i in range(len(items))]
        for i in range(len(items)):
            for key in items[i]:
                if key in args:
                    r[i][key] = items[i][key]
        return r
    except:
        return "Not list of dicts as argument passed"


if __name__ == "__main__":
    print(field(goods, 'title', 'price'))
