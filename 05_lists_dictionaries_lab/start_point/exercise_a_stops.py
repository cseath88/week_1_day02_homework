stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list

stops.append("Edinburgh Waverly")

#2. Add "Glasgow Queen St" to the start of the list

stops.insert(0, "Glasgow Queen Street")

#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

stops.insert(4, "Polmont")

#4. Print out the index position of "Linlithgow"

print("Linlithgow is index position 3.")

#5. Remove "Livingston" from the list using its name

stops.remove("Livingston")

#6. Delete "Cumbernauld" from the list by index

# del stops[2]

#7. Print the number of stops there are in the list

# number_of_stops = len(stops)
# print("The number of stops is: " + str(number_of_stops))     #cant have string and int in same print, must convert int to string

#8. Sort the list alphabetically

# alphabetical_list = sorted(stops)

#9. Reverse the positions of the stops in the list

# stops.reverse()

#10 Print out all the stops using a for loop

for stop in stops:
    print(stop)

