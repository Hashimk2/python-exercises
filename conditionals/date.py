# # # find the next day
# # # if user inputs yyyy,m(m),d(d), print the next day all in ints
# # # edge cases
# # # if user inputs end of month, print next month first day
# # # all months dont have same # of days
# # # if user inputs 12/31, print the next year and change the month to 1 and 1st day
# # # cant concatenate ints, only str's
# # # year
# # # print(str(month_input) +  '/' + str(day_input)  +  '/' + str(year_input + 1))

# # # year and month
# # # print(str(month_input) +  '/' + str(day_input)  +  '/' + str(year_input + 1))
# # # print(str(month_input + 1) +  '/' + str(day_input + 1)  +  '/' + str(year_input + 1))

# year_input = int(input("Enter the current year: "))

# leap_year = year_input % 4

# month_input = int(input("Enter the current month as a number (i.e. March = 3): "))
# day_input = int(input("Enter the current day: "))
# if (day_input == 31) or (month_input == 2 and day_input == 28) or (month_input == 4 and day_input == 30) or (month_input == 6 and day_input == 30) or (month_input == 9 and day_input == 30) or (month_input == 11 and day_input == 30):
#     print('Tomorrow is: ' + str(year_input) + '/' + str(month_input + 1) + '/' + str(1))
# else:
#      print('')

# date_input = str(month_input) + '/' + str(day_input + 1) + '/' + str(year_input)

# print('Tommorow is: ' + str(month_input) +  '/' + str(day_input + 1)  +  '/' + str(year_input))

# if (day_input != 31) or (month_input != 2 and day_input != 28) or (month_input != 4 and day_input != 30) or (month_input != 6 and day_input != 30) or (month_input != 9 and day_input != 30) or (month_input != 11 and day_input != 30):
#       print(date_input)
# else:
#      print('')



# if (month_input == 2 and day_input == 28 and year_input == leap_year):
#     print('Tommorow is: ' + str(month_input) +  '/' + str(day_input + 1)  +  '/' + str(year_input))
# else:
#      print('')

# # if (month_input == 2 and day_input == 28 and year_input == year_input % 4):
# #     print('Tommorow is: ', str(day_input + 1), str(month_input + 1), str(year_input))


# print('')
# print('The last date on the screen will be the date if tommorow. IGNORE THE OTHER DATES ON TOP! ')
# print('')
# year_input = int(input("Enter a year: "))
# print('')
# month_input = int(input("Enter a month: "))
# print('')
# day_input = int(input("Enter a day: "))

# print ('Tommorow is: ', year_input, '-', month_input, '-', day_input + 1)

# january = 1

# leap_year = year_input % 4

# # end_day = 31, 30, 29, 28


# if (month_input == 1 or month_input == 3 or month_input == 5 or month_input == 7 or month_input == 8 or month_input == 10):
#     if (day_input == 31):
#         print('Tommorow is: ', year_input, '-', month_input, '-', 1)
#     elif (month_input == 12):
#          if (day_input == 31):
#             print('Tommorow is: ', year_input + 1, '-', 1, '-', january)
# elif (month_input == 2 and leap_year != 0):
#     if (day_input == 28):
#         print('Tommorow is: ', year_input , '-', 3, '-', 1)
# elif (month_input == 4 or month_input == 6 or month_input == 9 or month_input == 11):
#     if (day_input == 30):
#           print('Tommorow is: ', year_input,'-', month_input, '-', 1)
#     elif (month_input == 2):
#         if (leap_year == 0 and day_input == 29):
#             print('Tommorow is: ', year_input , '-' ,3, '-', 1)
#         elif (day_input == 28 and leap_year == 0):
#             print('Tommorow is: ', year_input, '-', 2, '-', 29)
#     elif (month_input == 12):
#         if (day_input == 31):
#            print('Tommorow is: ', year_input, '-', 1, '-', 1)
#     elif (month_input == 2 and leap_year == 0):
#         if (day_input == 29):
#             print('Tommorow is: ', year_input, '-', 3, '-', 1)
#     elif (month_input == 2 and leap_year == 0):
#         if (day_input == 28):
#             print('Tommorow is: ', year_input , '-' '2', '-', 29)
#     else:
#         print('Tommorow is: ', year_input, '-', month_input, '-', day_input + 1)



# print('')
# print('The last date on the screen will be the date of tommorow. IGNORE THE OTHER DATES ON TOP! ')
# print('')
# year_input = int(input("Enter a year: "))
# print('')
# month_input = int(input("Enter a month: "))
# print('')
# day_input = int(input("Enter a day: "))




# january = 1

# leap_year = year_input % 4

# end_day = 31, 30, 29, 28


# if (month_input == 1 or month_input == 3 or month_input == 5 or month_input == 7 or month_input == 8 or month_input == 10):
#     if (day_input == 31):
#         print('Tommorow is: ', year_input, '-', month_input + 1, '-', 1)
#     elif (month_input == 12 and day_input == 31):
#       print('Tommorow is: ', year_input + 1, '-', 1, '-', 1)
# elif (month_input == 2 and leap_year != 0):
#     if (day_input == 28):
#         print('Tommorow is: ', year_input , '-', 3, '-', 1)
# elif (month_input == 4 or month_input == 6 or month_input == 9 or month_input == 11):
#     if (day_input == 30):
#           print('Tommorow is: ', year_input,'-', month_input, '-', 1)
#     elif (month_input == 2):
#         if (leap_year == 0 and day_input == 29):
#             print('Tommorow is: ', year_input , '-' ,3, '-', 1)
#         elif (day_input == 28 and leap_year == 0):
#             print('Tommorow is: ', year_input, '-', 2, '-', 29)
#     elif (month_input == 12):
#         if (day_input == 31):
#            print('Tommorow is: ', year_input, '-', 1, '-', 1)
#     elif (month_input == 2 and leap_year == 0):
#         if (day_input == 29):
#             print('Tommorow is: ', year_input, '-', 3, '-', 1)
#     elif (month_input == 2 and leap_year == 0):
#         if (day_input == 28):
#             print('Tommorow is: ', year_input , '-' '2', '-', 29)
#     else:
#         print('Tommorow is: ', year_input, '-', month_input, '-', day_input + 1)




# year = int(input('Please enter a year: '))
# month = int(input('Please enter a month: '))
# day = int(input('Please enter a day: '))

# day_input = day + 1

# leap_year = year % 4

# if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
#     if (day == 31):
#         print('Tommorow is: ', month + 1, '-', 1, '-', year)
#     else:
#        print('Tommorow is: ', month, '-', day + 1, '-', year)
# elif (month == 4 or month == 6 or month == 9 or month == 11 and day == 30):
#   print('Tommorow is: ', month + 1, '-', 1, '-', year)
# elif (month == 2 and day == 28 and leap_year == 0):
#   print('Tommorow is: ', month, '-', 29, '-', year)
# elif (month == 2 and day == 28 and leap_year != 0):
#   print('Tommorow is: ', month + 1, '-', 1, '-', year)
# elif (month == 2 and day == 29 and leap_year == 0):
#   print('Tommorow is: ', month + 1, '-', 1, '-', year)
# elif (month == 12 and day == 31):
#   print('Tommorow is: ', 1, '-', 1, '-', year + 1)

year = int(input('Please enter a year: '))
month = int(input('Please enter a month: '))
day = int(input('Please enter a day: '))

day_input = day + 1

leap_year = year % 4

if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
    if (day == 31):
        print('Tommorow is: ', month + 1, '-', 1, '-', year)
    else:
       print('Tommorow is: ', month, '-', day + 1, '-', year)
elif (month == 4 or month == 6 or month == 9 or month == 11 and day == 30):
  print('Tommorow is: ', month + 1, '-', 1, '-', year)
elif (month == 2 and day == 28 and leap_year == 0):
  print('Tommorow is: ', month, '-', 29, '-', year)
elif (month == 2 and day == 28 and leap_year != 0):
  print('Tommorow is: ', month + 1, '-', 1, '-', year)
elif (month == 2 and day == 29 and leap_year == 0):
  print('Tommorow is: ', month + 1, '-', 1, '-', year)
elif (month == 12 and day == 31):
  print('Tommorow is: ', 1, '-', 1, '-', year + 1)

