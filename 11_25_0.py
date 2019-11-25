def maxArea(height):
    if not height:
        return 0
    
    out = 0
    left = 0
    right = len(height) - 1
    
    while left != right:
        if height[left] < height[right]:
            out = max(height[left] * (right - left), out)
            left += 1
        else:
            out = max(height[right] * (right-left), out)
            right -= 1
        
    return out


input_array = [1,8,6,2,5,4,8,3,7]
print(maxArea(input_array))