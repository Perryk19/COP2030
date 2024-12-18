#Exercise 1

#Setting the ticket costs
'''
Parameters/Inputs:
numbers entered by the user using input() function - num_a, num_b & num_c

Returns/Outputs:
the ticket income depending on number of tickets from each class

Example:
Input: 3, 2, 1; Output: (3*30)+(2*25)+(1*20)= 90+50+20= 160

###Pseudocode:
1. Define the 'total_ticket_income()' function:
- Prompt the user the user to input a number for each class of ticket
- The code  will take total the class ticket prices multiplied by the number of tickets 
2. Define the  'main()' function:
- set price for the ticket class variables
- initialize the num_a, num_b, num_c variables for the number of tickets
3. After the input of all of the tickets sold were collected a  message will print with the total tickets solda
"The total income from ticket sales is ${ticket_income"

'''

def main():

  num_a = 0
  num_b = 0
  num_c = 0


  #Ask for how many tickets for each class were sold

  num_a = int(input("How many Class A tickets were sold? "))
  num_b = int(input("How many Class B tickets were sold? "))
  num_c = int(input("How many Class C tickets were sold? "))

  #Call the total ticket income
  ticket_income = total_ticket_income(num_a, num_b, num_c)


  print(f'The total income from ticket sales is ${ticket_income}')

def total_ticket_income(num_a, num_b, num_c):
  class_a = 30
  class_b  = 25
  class_c = 20

  #Calculate the total income
  ticket_income  = (num_a*class_a)+(num_b*class_b)+(num_c*class_c)

  return ticket_income

main()





