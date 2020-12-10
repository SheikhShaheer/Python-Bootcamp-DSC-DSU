def print_pattern(name) :

    temp1 = 0
    temp2 = len(name)-1

    # Iterater the input and print diagnolly...
    for i in range(len(name)) : 
        for j in range(len(name)) : 
            if i==temp1 and j==temp2 : 
                print(name[i].upper(), end='')
                temp1=temp1+1
                temp2=temp2-1
            elif i==j :
                print(name[i].upper(), end='')
            else :
                print(end=' ')
        print()

if __name__ == "__main__":
    
    # take input...
    name = input("Write Something Man ! ") 

    # Print the pattern...
    print_pattern(name)
    
