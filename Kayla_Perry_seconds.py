#Exercise 3

'''
Parameters/Inputs:
numbers entered by the user using input() function - hours & minutes

Returns/Outputs:
the conversion of hours and minutes to seconds

Example:
Input: 3, 2; Output: 3*60*60 + 2*60 = 10920 seconds

###Pseudocode:
1. Define the 'convert_to_seconds()' function:
- Prompt the user to input a number for hours and minutes worked
- The code  will take hours and minutes and convert them into seconds using hours*60*60 + minutes*60
2. Define the  'main()' function:
- initialize the hours and minutes variables for the number of duration worked in hours and minutes
- call the convert_to_seconds() function
3. After the input of the hours and minutes worked a  message will print with the total seconds worked
"{hours} hours and {minutes} minutes = {seconds} seconds"

'''

def main():
  hours = 0
  minutes = 0

  #Ask for number of miles driven
  hours = int(input("How many hours were worked? "))
  minutes = int(input("How many minutes were worked? "))

  seconds = convert_to_seconds(hours, minutes)

  print(f'{hours} hours and {minutes} minutes = {seconds} seconds')


def convert_to_seconds(hours, minutes):
  seconds = hours*60*60 + minutes*60
  return seconds

main()
