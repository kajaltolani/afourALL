#Python program to swap two variables (without using temporary variable) provided by the user.

var1=input('enter data for variable 1: ')
print('var1: ',var1)
var2=input('enter data for variable 2: ')
print('var2: ', var2)
swap_it = input('Do you want to swap the data? (Enter Y or N.)')    #assuming that user says Yes
print('Swapping data as follows: ')
var1,var2=var2,var1                       #syntax for swapping without using temp variable x,y=y,x
print('var1 after swapping: ',var1)
print('var2 after swapping: ',var2)
