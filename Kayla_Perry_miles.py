#Exercise 2

'''
Parameters/Inputs:
numbers entered by the user using input() function - miles

Returns/Outputs:
the conversion of miles to kilometers

Example:
Input: 3; Output: 3*1.60934 = 4.82802

###Pseudocode:
1. Define the 'miles_to_kilometers()' function:
- Prompt the user to input a number of miles driven
- The code  will take miles and convert them into kilometers using 1.60934 as the conversion factor
2. Define the  'main()' function:
- initialize the miles variables for the number of miles driven
- call the miles_to_kilometers() function
3. After the input of all of the miles driven a  message will print with the total miles driven
"{miles} miles = {kilometers} kilometers"

'''

def main():
  miles = 0

  #Ask for number of miles driven
  miles = int(input("How many miles were driven? "))

  kilometers = miles_to_kilometers(miles)

  print(f'{miles} miles = {kilometers} kilometers')


def miles_to_kilometers(miles):

  #Convert miles to kilometers
  kilometers = miles*1.60934
  return kilometers
main()
