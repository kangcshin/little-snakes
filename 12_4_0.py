def maxWater(height, n): 
  
    # To store the maximum water so far 
    maximum = 0; 
  
    # Both the pointers are pointing at the first 
    # and the last buildings respectively 
    i = 0
    j = n - 1
  
    # While the water can be stored between 
    # the currently chosen buildings 
    while (i < j): 
      
        # Update maximum water so far and increment i 
        if (height[i] < height[j]):      
            maximum = max(maximum, (j - i - 1) * height[i]); 
            i += 1; 
          
        # Update maximum water so far and decrement j 
        elif (height[j] < height[i]): 
            maximum = max(maximum, (j - i - 1) * height[j]); 
            j -= 1; 
          
        # Any of the pointers can be updated (or both) 
        else:      
            maximum = max(maximum, (j - i - 1) * height[i]); 
            i += 1; 
            j -= 1; 
          
    return maximum; 
  
# Driver code 
height = [2, 1, 3, 4, 6, 5] 
  
n = len(height) 
  
print (maxWater(height, n))