# print('Welcome to Northen Frock Bank ATM')
# restart=('Y')
# chances = 3
# balance = 67.14
# while chances >= 0:
#     pin = int(input('Please Enter You 4 Digit Pin: '))
#     if pin == (1234):
#         print('You entered you pin Correctly\n')
#         while restart not in ('n','NO','no','N'):
#             print('Please Press 1 For Your Balance\n')
#             print('Please Press 2 To Make a Withdrawl\n')
#             print('Please Press 3 To Pay in\n')
#             print('Please Press 4 To Return Card\n')
#             option = int(input('What Would you like to choose?'))
#             if option == 1:
#                 print('Your Balance is Â£',balance,'\n')
#                 restart = input('Would You you like to go back? ')
#                 if restart in ('n','NO','no','N'):
#                     print('Thank You')
#                     break
#             elif option == 2:
#                 option2 = ('y')
#                 withdrawl = float(input('How Much Would you like to withdraw? /nÂ£10/Â£20/Â£40/Â£60/Â£80/Â£100 for other enter 1: '))
#                 if withdrawl in [10, 20, 40, 60, 80, 100]:
#                     balance = balance - withdrawl
#                     print ('\nYour Balance is now Â£',balance)
#                     restart = input('Would You you like to go back? ')
#                     if restart in ('n','NO','no','N'):
#                         print('Thank You')
#                         break
#                 elif withdrawl != [10, 20, 40, 60, 80, 100]:
#                     print('Invalid Amount, Please Re-try\n')
#                     restart = ('y')
#                 elif withdrawl == 1:
#                     withdrawl = float(input('Please Enter Desired amount:'))    

#             elif option == 3:
#                 Pay_in = float(input('How Much Would You Like To Pay In? '))
#                 balance = balance + Pay_in
#                 print ('\nYour Balance is now Â£',balance)
#                 restart = input('Would You you like to go back? ')
#                 if restart in ('n','NO','no','N'):
#                     print('Thank You')
#                     break
#             elif option == 4:
#                 print('Please wait whilst your card is Returned...\n')
#                 print('Thank you for you service')
#                 break
#             else:
#                 print('Please Enter a correct number. \n')
#                 restart = ('y')
#     elif pin != ('1234'):
#         print('Incorrect Password')
#         chances = chances - 1
#         if chances == 0:
#             print('\nNo more tries')
#             break

# year=int(input("enter an year:"))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("%d is a leap year"%(year))
#        else:
#            print("%d is not a leap year"%(year))
#    else:
#        print("%d is a leap year"%(year))
# else:
#    print("%d is not a leap year"%(year))



# test_list1 = [1, 3, 4, 6, 8] 
# test_list2 = [4, 5, 6, 2, 10]  
# print ("Original list 1 : " + str(test_list1)) 
# print(type(test_list1))
# print ("Original list 2 : " + str(test_list2))
# res_list = [] 
# for i in range(0, len(test_list1)): 
#     res_list.append(test_list1[i] + test_list2[i]) 
# print ("Resultant list is : " + str(res_list)) 