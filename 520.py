#coding:utf-8
stuff = {'name':'Zed', 'age':36, 'height': 6*12+2}

print stuff['name']
print stuff['age']
print stuff['height']
stuff['city'] = "San Francisco"

print stuff['city']
stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff



print stuff

cities = {'CA':'San Francisco','MI':'Detroit','FL':'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):

    if  state in themap:
        return themap[state]
    else:
        return "Not found"

# ok pay attention!

cities['_find'] = find_city

while True:
    print "State? (ENTER to quit)"
    state = raw_input("> ")
    if not state: break

    city_found = cities['_find'](cities, state)
    print city_found

