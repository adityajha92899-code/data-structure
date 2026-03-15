# Tower of Hanoi using Recursion

def tower_of_hanoi(n, source, auxiliary, destination):
    
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return
    
    # move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary)
    
    # move nth disk to destination
    print("Move disk", n, "from", source, "to", destination)
    
    # move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination)


# Driver Code
n = 3
tower_of_hanoi(n, 'A', 'B', 'C')