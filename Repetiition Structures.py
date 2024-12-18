 #Exercise 1: Compute Averages
#The following code will take the input of a series of numbers and compute the average of those numbers.
# -1 will be the stop value.

#Setting the variables
number = 1.0 #Initialize for while loop
num_of_numbers = 0
total = 0


#Contintue averaging numbers while number is positive.
while number > 0:
    number = float(input("Enter positive numbers\n(enter a negative number to stop the code and reveal their average): "))

    #Check that number is positive
    #num_of_numbers is collecting the number of inputs while the total adds up all of the inputs
    if number > 0:
        num_of_numbers += 1
        total += number
        

#Display average
print(f"Average: {total/num_of_numbers:.2f}")


#Exercise 2: Salary
#The following code will determine how much money a person  would earn over a period of time.
#They will start with one penny and double each day. The input will ask for the number of days
#and display a table that shows the salary for each day and total pay at the end of the period.


#Setting the variables
salary = 0.01
days = 1

while days > 0:
    #Get our ending limit
    print(f"Let's determine your salary after a number of days\nif your salary starts at $0.01 and doubles each day.")
    days = int(input("How many days do you want to enter? "))

    #print the table
    print()
    print("Days\tSalary")
    print('-'*20)
    
    #print the days and the corresponding salaries
    for day in range (1, days +1):
        salary = 0.01*(2**(day-1))
        print(f'{day}\t${salary}')

        
#Exercise 3 : GoBulls
#The following code will print the numbers 1 to 50. For any multiples of 3, it will print "Go" in  place
#the number. For multiples of 5, it will bring "Bulls". For numbers that are multiples of both 3 and 5,
#it will print "GoBulls". If the number is not divisible by 3 or 5, it will print the number.

#input is range 1 - 50
#for multiples of 3 print  "Go"
#for multiples of 5 print "Bulls"
#for multiples of both 3 and 5, print "GoBulls"
#if not divisible by 3 or 5, print the number
#loop 1-50 to check  for  multiples of 3, multiples  of 5 and multiples of 3 and 5.


#Loop  through numbers 1 to 50

for number in range(1,51):

    #check if multiple of 3 and 5
    if number%3 == 0 and number%5 == 0:
        print("GoBulls")

    #check if multiple of only 3
    elif number%3 == 0:
        print("Go")

    #check if multiple of only 5
    elif number%5 == 0:
        print("Bulls")

    #if not multiples of 3 or 5 then print number
    else:
        print(number)

