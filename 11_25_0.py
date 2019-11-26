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

    # def maxArea(self, height: List[int]) -> int:
    #     begin, end, output = 0, len(height)-1, 0
    #     while begin < end:
    #         h = height[begin] if height[begin] < height[end] else height[end]
    #         temp = h * (end - begin)
    #         output = max(output, temp)
    #         if height[begin] < height[end]:
    #             begin += 1
    #         else:
    #             end -= 1
                
    #     return output

input_array = [1,8,6,2,5,4,8,3,7]
print(maxArea(input_array))