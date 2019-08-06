import csv

def generate_dict(filename):
    prefix_dict = {}

    with open(filename) as file:
        rows = csv.reader(file)

        for (type, prefix, rate) in rows:
            path = prefix_dict
            for (i, j) in enumerate(prefix):
                if j not in path:
                    path[j] = {'type': {}}
                if i == len(prefix) - 1:
                    if 'rate' not in path[j] or rate < path[j]['rate']:
                        path[j]['operator'] = type
                        path[j]['rate'] = rate
                else: path = path[j]['type']
    return prefix_dict

def select_operator(num, prefix_dict):
    operator = None
    price = None
    node = prefix_dict
    for i in num:
        if i not in node:break
        if 'operator' in node[i]:
            operator = node[i]['operator']
            price = node[i]['rate']
        node = node[i]['type']
    if operator == None:return None
    else:return {'operator': operator, 'price': price}

if __name__ == '__main__':
    num = input('Enter key to search : ')
    while not num.isdigit():
        num = input('Please enter the numeric digits: ')
    prefix_dict = generate_dict('sample_price_lists copy.csv')
    result = select_operator(num, prefix_dict)
    if result == None:print('No matching prefix found.')
    else:print(result)
