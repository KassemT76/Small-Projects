#Introduction/Menu
def menu():
    print("\nWelcome to the Binary Converter by Kassem Taha")
    print('What would you like to do: ')
    print('1. Continue')
    print('2. Exit')

def converter():
    #Input
    x = int(input("\nInsert number to be converted to binary: \n"))
    #Declaring Variables
    result = []
    y = 0
    z = 0

    #Converting Base 10 to Base 2 and assigning the binary values to "result" array
    while x >= 1:
        z = x % 2
        result.append(z)
        x = int(x/2)
        y = int(x/2)

    #Reversing the array so it is readable
    result.reverse()

    #Output
    print("Your number in binary is: ")
    print(*result)

#Loop after program is done
while True:
    menu()
    #Enter either 1 to continue or 2 to exit the program
    choice = int(input('\nEnter a number: '))
    if choice == 1:
         converter()
    elif choice == 2:
        break