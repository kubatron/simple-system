import csv
import itertools

"""Simple function to get a information,
about lenght all value which we are interested
"""
def valLen(val_str):
    x = [len(x) for x in val_str]
    return x
"""
Simple function to get information,
about dimensions list
"""
def is_list(x):
    return type(x) == list
"""
Error info to handle Exception (IndexError)
"""
def inf_err(d, h):
    inf = 'Error in data or headers.'
    print()
    print('_'*len(inf), sep='\n')
    print(inf)
    print('='*len(inf))
    print('Lenght of headers:', len(d), end=" ")
    print()
    print('Lenght of data:', len(h), end=" ")
    print()
    print('_'*len(inf), sep='\n')

"""
Main function to get input data like,
@data: list of data (list(), []) one or many dimensions
@headers: list of headers to format table
"""
def helper(a1, sepX=10, sepH=4):
    y = len(''.join(a1))
    lenA1 = len(a1)
    x = sepX * lenA1 + y - sepX + sepH
    mainSep = '='*x
    return mainSep, sepX, x, lenA1, y, sepH
"""
Function to show data and headers which you will put into two arguments
@data: is holding a nested dict() i.e.
data = { 0: {0: 'value0', 1: 'value1', 2: 'value2', 3: 'value3},
1: {0: 'value0', 1: 'value1', 2: 'value2', 3: 'value3} }
---
@headers: is holding list() i.e.
headers = ["first_head", "second_head"]
"""
def tab(data, headers):
    try:
        y1 = valLen(headers)
        a = helper(headers)
        #if any(map(is_list, data)):
        #    print(data)
        print('_'*a[2])
        for i, j in enumerate(headers):
            print(j, end=" "*a[1])
        print()
        print(a[0], sep='')
        for p_id, p_info in data.items():
            print()
            for key in p_info:
                tmp = y1[key] - len(p_info[key]) + a[1]
                print(p_info[key], end=" "*tmp)
        b = helper(p_info[key])
        print()
        print('='*b[2], b[4])
    except IndexError:
        inf_err(data, headers)
        print(data[len(headers)-len(data):])
        print(headers[len(data)-len(headers):])
print()

# ----------------------
# Example of using "tab"
# ----------------------
tab({0: {0: '3984', 1: 'Jakub', 2: 'Wydro', 3: '30.01.1989', 4: '0', 5: '374PL374PL374PL374PL374PL374PL374PL374PL374PL374PL'},
      1: {0: '4853', 1: 'Krystian', 2: 'Terrenko', 3: '30.01.1989', 4: '0', 5: '374PL'},
      2: {0: '4893', 1: 'Adrian', 2: 'Turbak', 3: '30.01.1989', 4: '0', 5: '374PL'},
      3: {0: '4893', 1: 'Adrian', 2: 'Turbak', 3: '30.01.1989', 4: '0', 5: '374PL'},
      4: {0: '4893', 1: 'Adrian', 2: 'Turbak', 3: '30.01.1989', 4: '0', 5: '374PL'},
      5: {0: '4893', 1: 'Adrian', 2: 'Turbak', 3: '30.01.1989', 4: '0', 5: '374PL'}
      }, ['ID', 'Name', 'Surname', 'Data urodzenia', 'Encrypted:', 'RIDdsadasdas'])
print()



# -----------------------------------------------------------
# Not finish yet, but is working
# You can open a .csv file and view a content in simple table
# -----------------------------------------------------------
with open('nowy.csv', newline='\n') as file:
    reader = csv.reader(file, dialect='excel', delimiter=' ')
    headings = next(reader)
    for x in headings:
        length = sum(len(s) for s in headings)    
        a = x.split(',')
        print(a)
        for i in a:
            calcS = 8 - len(i)
            if calcS == len(i):
                print('{0}'.format(i), end='\t')
            elif calcS != len(i):
                print('{0}'.format(i), end='\t')
    print()
    print(end='='*5)

    for x in reader:
        z = x[0].split(',')
        for m in range(0, len(z)):
            lenDat = len(''.join(z[m]))
            if m+1 == len(x):
                print()
            print(z[m], end='\t')
