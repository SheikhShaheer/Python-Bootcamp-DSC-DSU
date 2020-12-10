def create_student_list( entries = 5 ) :
    i = 0
    student_data = {}

    print( '**roll_num**  |  **name**  |  **age**  | **marks**(out of 100)' )
    
    while i != entries :

        student_data[i] = {}
        
        student_data[i]["rollNo"], student_data[i]["name"], student_data[i]["age"], student_data[i]["marks"] = input().split()

        i=i+1
        print()

    return student_data

def print_list( student_list, entries ) :

    marks = []

    for i in range( len( student_list ) ) :
        marks.append( student_list[i]["marks"] )

    lowest = highest_lowest_marks( marks, 'lowest' )
    highest = highest_lowest_marks( marks, 'highest' )
    average = average_marks( marks )
    
    print( '|-----------------------------------|' )
    print( '|   Lowest     Highest     Average  |' )
    print( '|-----------------------------------|' )

    print( '|', end='' )
    print( end='\t' )
    print( lowest, end='\t' )
    print( highest, end='\t\t')
    print( average, end='')
    print( '|', end='\n' )

    print( '|-----------------------------------|' )


def highest_lowest_marks( marks, marks_format ) :
    

    if ( 'lowest' == marks_format.lower() ) :
        return min( marks )

    elif ( 'highest' == marks_format.lower() ) :
        return max( marks )

def average_marks( marks ) :
    
    total = 0

    for i in range( len( marks ) ) :
        total = total + int( marks[i] )

    average = total / len( marks )

    return average

if __name__ == "__main__":

    # taking entriy count... 
    entries = int( input('Enter the number of entries : ') )
    student_list = {}
    
    # making list...
    student_list = create_student_list( entries )

    # Printing the list...
    print_list( student_list, entries )