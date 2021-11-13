array = [ 10, -3, -19, 7, -18, 4, 15, -5 ]
swap_index = -1

for index in range ( 0, len(array) ) :
    if array[ index ] < 0 :
        swap_index += 1
        temp = array[ swap_index ]
        array[ swap_index ] = array[ index ]
        array[ index ] = temp
        
if ( swap_index < (len(array))/2 ) : swap_index += 1

for index in range (0, int(len(array)/2)+1, 2) :
    
    if ( swap_index + index >= len(array) or swap_index - index < 0 ) : break

    temp = array[ swap_index + index ]
    array[ swap_index + index ] = array[ swap_index - index - 1 ]
    array[ swap_index - index - 1 ] = temp
    
print (array)
