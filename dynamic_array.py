# Dynamic Array Simulation

class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity

    # Resize function
    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity

    # Append element
    def append(self, value):
        if self.size == self.capacity:
            self.resize(self.capacity * 2)

        self.array[self.size] = value
        self.size += 1

    # Pop element from end
    def pop(self):
        if self.size == 0:
            return "Array is empty"
        
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    # Display array
    def display(self):
        for i in range(self.size):
            print(self.array[i], end=" ")
        print()


# Driver code
arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

print("Array after append:")
arr.display()

print("Popped element:", arr.pop())

print("Array after pop:")
arr.display()