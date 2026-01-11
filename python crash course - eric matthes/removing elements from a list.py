# TIY 3.4: Guest List

guests = ["virginia", "marvin john", "myr jessica", "mae joyce"]

print(f"Welcome {guests[0].title()}!")
print(f"Welcome {guests[1].title()}!")
print(f"Welcome {guests[2].title()}!")
print(f"Welcome {guests[3].title()}!")

print(len(guests))

# TIY 3.5: Changing Guest List

absent = guests.pop(2)
guests.append("mark")
came = guests[3]

guest_list = guests

print(f"\n{absent.title()} can't make it today :< but {came.title()} came, so... \nWelcome {came.title()}")

print(f"\nUpdated list of guests:\n{guests[0].title()}\n{guests[1].title()}\n{guests[2].title()}\n{guests[3].title()}")

print(len(guests))

# TIY 3.6 More Guests

print(f"\nNew tables are coming, so we're expecting more guests....")

guests.insert(0, "juan")
guests.insert(3, "yumi")
guests.append("johanan")

print(f"\nWelcome to the new people {guests[0].title()}, {guests[3].title()}, and {guests[6].title()}.")

print(f"\nHere are the updated list of guests: \n{guests[0].title()}\n{guests[1].title()}\n{guests[2].title()}\n{guests[3].title()}\n{guests[4].title()}\n{guests[5].title()}\n{guests[6].title()}")

print(len(guests))

# TIY 3.7 Shrinking Guest List:

print(f"\nUnfortunately... we can only accept two invitations since only two chairs are left so...")

uninvited_1 = guests.pop()

print(f"\nWe're sorry but there is no space for {uninvited_1.title()} anymore")

uninvited_2 = guests.pop()

print(f"\nAlso to {uninvited_2.title()}, we're really sorry :<")

print(f"\nbut here is the list of the people who are still invited: \n{guests[0].title()}\n{guests[1].title()}\n{guests[2].title()}\n{guests[3].title()}\n{guests[4].title()}")

print(f"\nSome people are unable to came and are going to be removed in the guest list.")

print(len(guests))

del guests[4]

print(f"\n Updated List: \n{guests}")
print(len(guests))

del guests[3]

print(f"\n Updated List: \n{guests}")
print(len(guests))