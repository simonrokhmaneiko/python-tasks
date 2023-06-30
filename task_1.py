# A string of city names separated with space is passed into function.
# A function should return a string of lengths of city names separated by space.
# Example:
# "Amsterdam Utrecht Groningen"  ==>  "9 7 9"

def cities_len(cities):
    cities = cities.split()
    lst = []
    
    for i in cities:
        lst.append(len(i))

    return lst
