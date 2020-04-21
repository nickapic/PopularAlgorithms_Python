
# Binary Search
# Efficieny = O(log n)
# Basically breaks the list into halves again and again to find where the element is


def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        elif item < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None


smalllist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("###########  Results  ############ ")
print("Binary Search here : ")

print(binary_search(smalllist, 4))


# Linked list Implementation Non Automated way but you can automate it preety easily
# Time Complexity for Insertion is Constant O(1) and for deletion and search its O(n)
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        resultlist = []  # Done just because the code looks the output looks unorganized otherwise
        while (temp):
            resultlist.append(temp.data),
            temp = temp.next
        print(resultlist)


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third
print("Linked List here : ")
llist.printList()


# Helper function for our Selection Sort Algortihm
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# Selection Sort here Time Complexity is O(n^2) so its very slow wouldnt recommend using it try quick sort algorithms
# Its n^2 because it does two for loops one its helper function which is Find Smallest so thats O(n) and then this function which takes O(n) so the time complexity comes out to be n * n so O(n^2)


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


print("Selection Sort here : ")
print(selectionSort([5, 3, 6, 2, 10]))
