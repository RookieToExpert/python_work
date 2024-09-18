# #List of the ppl who will be invited to dinner
# dinner_list = ["Lebron","Rose","Kelly"]
# print(f"Here is the list of all the guest for today's dinner \n{dinner_list}")

# #Kelly is not attending the dinner, jenny weill come instead, announce this message
# print(f"{dinner_list[-1]} is not able to attend the dinner, but Jenny will come instead.")
# del dinner_list[-1]
# dinner_list.append('Jenny')
# print(f"Here is the new list: {dinner_list}")

# #We found a bigger table, will announce erveryone
# print(f"\nhey {dinner_list[0]}, we have a bigger dinner table, more ppl will come!")
# print(f"\nhey {dinner_list[1]}, we have a bigger dinner table, more ppl will come!")
# print(f"\nhey {dinner_list[2]}, we have a bigger dinner table, more ppl will come!")

# #We have Kobe in the house, will put him in the first spot, and Michael in the middle and me at the end.
# dinner_list.insert(0, 'Kobe')
# dinner_list.insert(2, 'Michael')
# dinner_list.append('Ray')
# print(f"\nHey guys, new list is coming, please take a look: \n{dinner_list}")

# #Table is reserverd already, we have to change to a smaller table that can hlod only two ppl
# print(dinner_list)
# removed_list = []
# removed_list.append(dinner_list.pop(0))
# removed_list.append(dinner_list.pop(0))
# removed_list.append(dinner_list.pop(0))
# removed_list.append(dinner_list.pop(0))
# print(f"\nHere is the list that not join the dinner: \n{removed_list}")
# print(f"\nHere is the list that can join the dinner: \n{dinner_list}")

# #Had a wonderful dinner, will clean the list
# del dinner_list[0]
# del dinner_list[0]
# print(dinner_list)


#3-8 List of locations
locations = ['BeiJing', 'ShangHai', 'DongGuan', 'ChengDu']
print(f"\nHere is the list of lication we gonna visit: \n{locations}")
print(f"\nHere is the alphabetical order of the list of lication we gonna visit: \n{sorted(locations)}")
print(f"\nHere is the reverse-alphabetical order of the list of lication we gonna visit: \n{sorted(locations, reverse=True)}")
print(f"\nHere is the list of lication we gonna visit: \n{locations}")
locations.reverse()
print(f"\nHere is reverse order of the list of lication we gonna visit: \n{locations}")
locations.sort()
print(f"\nHere is the permanent alphabetical order of the list of lication we gonna visit: \n{locations}")
locations.sort(reverse=True)
print(f"\nHere is the permanent reverse-alphabetical order of the list of lication we gonna visit: \n{locations}")
