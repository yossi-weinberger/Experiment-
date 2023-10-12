"""This program calculates the amount of a tip per person.
written by Yossi Weinberger"""

#User input
print("\nHi, welcome to the tip calculator :)\n")
sum_price = float(input("Please write the total amount of the invoice: \n"))
participants = int(input("Please write the the number of diners: \n"))
tip_percentage = float(input("Please write how much tip you want to give (in percentages): \n"))

#Vars and calculation
tip = (sum_price / 100 * tip_percentage)/participants
tip_shekel = int(tip)
tip_agorot = int((tip - tip_shekel)*100)

#Format (jost for show off)
format_sum_price = "{:.2f}".format(sum_price)

#result print
print(f"For {participants} diners in a meal that cost {format_sum_price} NIS "
      f"\nEach diner has to pay: {tip_shekel} Shekel and {tip_agorot} Agorot.")

#program exit
end = input("Press enter to exit")

