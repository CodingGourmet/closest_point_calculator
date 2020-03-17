from math import sqrt
from operator import itemgetter
"""Given a series of three dimensional points (x, y, z), calculate which are closest to the origin and print them from 
   closest to furthest away. If a two dimensional point is included, z will be assumed to be zero. If a point has
   more than three values, all values after the third will be ignored. Please enter either int or float values only"""


def calculate_length(list1):
    try:
        big_list = []
        for item in list1:
            # check if element is (x,y) or (x,y,z)
            if len(item) == 2:
                temp_z = 0
            else:
                temp_z = item[2]
            x, y, z = item[0], item[1], temp_z
            w = sqrt(x**2 + y**2 + z**2)
            small_list = [x, y, z, w]
            big_list.append(small_list)
        return big_list
    except TypeError:
        # if the input is not numeric print error and exit
        print("Please only enter numeric values for (x, y, z)")
        exit()
    except IndexError:
        # if the input only contained one element, print error and exit
        print("Check to see if list items are a minimum of two elements.")
        exit()


# you can pass the points in as a list, tuple, or combination, since both are indexed the same way,
# and then the result is returned as a list.
points = ([4, 4, 4], (8, 1, 9), (7, 6, 5), (7, 7, 7), [2.45, -4], (0, 0, -3))
master_list = calculate_length(points)

sorted_master = sorted(master_list, key=itemgetter(3))
for items in sorted_master:
    print("point ({}, {}, {}) is {:.3f} from center".format(items[0], items[1], items[2], items[3]))
    # I realize that this may be streamlined, but I opted for readability
