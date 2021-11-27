#nested loops = the "inner loop" will finish all of it 's iterations before finishing one iteration of the "outer loop"

rows = int(input('How many rows?: '))
columns = int(input('How many columns?: '))
symbols = input('Enter a symbol to use: ')


for i in range(rows):
    for j in range(columns):
        print(symbols, end="") #end="" prevents the cursor from going to the nex line
    print()