# Baseball players starter file


def main():
    # Open an output file, players.txt(in append mode 'a')
    outfile = open("players.txt", "a")

    # Enter the player's number, name, and home runs for three additional players
    for count in range(3):
        number = int(input("Enter the player's number: "))
        name = input("Enter the player's name: ")
        hrs = int(input("How many homeruns did he hit?: "))   

        # Store each player's data in the output file
        outfile.write(f"{number: 2d} {name} {hrs: 2d}\n")


    # Close the output file
    outfile.close()

    # Reopen the file for input (printing)
    infile = open("players.txt", "r")
    
    # Print out the data for each player
    print(infile.read())

    # Close the input file  
    infile.close()

main()

