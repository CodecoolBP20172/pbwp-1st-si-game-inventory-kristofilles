# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification
from collections import Counter, OrderedDict
import csv
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
added_items = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Displays the inventory.


def display_inventory(inv):
    print("Inventory: ")
    for attribute, value in inv.items():
        print('{}  {}'.format(value, attribute))
    print("Total number of items: %d" % sum(inv.values()))

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inv, added_items):
    my_list = []
    for key in added_items:
        if key in my_list:
            continue
        else:
            my_list.append(key)
            count = added_items.count(key)
            if key in inv:
                inv[key] += count
            else:
                inv[key] = count
    return inv

# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inv, order=input):
    order = input(" :")
    ascending_inv = OrderedDict(sorted(inv.items(), key=lambda t: t[1]))
    descending_inv = OrderedDict(sorted(inv.items(), key=lambda t: t[1], reverse=True))
    print("Inventory: ")
    print("  count    item name")
    print("---------------------")
    if order == "":
        for k, v in inv.items():
            print(str(v).ljust(3, ' '), k.rjust(17, ' '))
    elif order == "count,asc":
        for k, v in ascending_inv.items():
            print(str(v).ljust(3, ' '), k.rjust(17, ' '))
    elif order == "count,desc":
        for k, v in descending_inv.items():
            print(str(v).ljust(3, ' '), k.rjust(17, ' '))
    print("---------------------")
    print("Total number of items: %d" % sum(inv.values()))

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).


def import_inventory(inv, filename="import_inventory.csv"):
    with open(filename, "r") as inputstream:
        for line in inputstream:
            currentline = line.split(",")
        inv = add_to_inventory(inv, currentline)
    return inv

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).


def export_inventory(inv, filename=None):
    if filename is None:
        filename = "export_inventory.csv"
    with open(filename, "w") as csvfile:
        exp_inv = Counter(inv)
        writer = csv.writer(csvfile, exp_inv.elements())
        writer.writerow(exp_inv.elements())


inv = add_to_inventory(inv, added_items)
order = input
print_table(inv, order)
import_inventory(inv, 'import_inventory.csv')
export_inventory(inv, filename=None)
