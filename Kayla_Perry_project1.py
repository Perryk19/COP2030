# Corner Store Program
# Purpose: This is a sales tracking program


#This code will calculate the sales totals by taking an input for the product ID and quantity, calculating the sales tax and subtotal,
#and adding them together.
#It will handle multiple transactions, and update the cash drawer after each transaction.

cash_drawer = 100.00
productID = 0
quantity = 0
price = 0.0
subtotal = 0.0
sales_tax = 0.0
total_sale = 0.0
tax_rate = 0.0
another_sale = "y"

print()
print("----------[ C o r n e r S t o r e ]----------")
print()

# Loop for each sale
while another_sale == "y":
    # Enter the first productID
    print()
    productID = int(input("Enter the first Product ID (-1 to end): "))
    # Loop for each product
    while productID != -1:
        # Enter the quantity
        quantity = int(input("Enter the quantity: "))
        
        # Look up price and whether it is taxable
        if productID == 101:
            price = 3.95
            tax_rate = 0
        elif productID == 102:
            price = 1.85
            tax_rate = 0.075
        elif productID == 103:
            price = 2.49
            tax_rate = 0.075
        elif productID == 104:
            price = 5.19
            tax_rate = 0.075
        elif productID == 105:
            price = 4.99
            tax_rate = 0
        else:
            print("Error! Item not found")
        
        
        # Add to subtotal and sales_tax
        subtotal += quantity * price
        sales_tax += quantity * price * tax_rate
        
        # Get next productID
        productID = int(input("Enter the next Product ID (-1 to end): "))
        
    # End of while loop

 
    # Add subtotal and sales_tax to total_sale
    total_sale = subtotal + sales_tax
    
    
    # Print out receipt
    print()
    print(f"Subtotal:     ${subtotal: 7.2f}")
    print(f"Sales Tax:    ${sales_tax: 7.2f}")
    print(f"Total:        ${total_sale: 7.2f}")
    # Add Total Sale to Cash Drawer
    cash_drawer += total_sale
    
    # Zero out subtotal and sales_tax
    subtotal = 0
    sales_tax = 0
    
    # Ask for another sale
    another_sale = input("Would you like another sale ('y' or 'n')? ")
# Print out cash drawer
print()
print(f"Total in cash drawer: ${cash_drawer: 7.2f}")
