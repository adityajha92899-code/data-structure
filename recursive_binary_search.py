# Recursive Binary Search

def binary_search(arr, left, right, target):

    if left <= right:
        mid = (left + right) // 2

        # element found
        if arr[mid] == target:
            return mid
        
        # search in left half
        elif arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)
        
        # search in right half
        else:
            return binary_search(arr, mid + 1, right, target)

    return -1


# Driver code
arr = [2, 4, 6, 8, 10, 12, 14]
target = 10

result = binary_search(arr, 0, len(arr)-1, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")