class Stack:
    """a stack create as a class"""
    #constructor
    def __init__(self,max_size):
        # set attributes starting values

        self._items = 0
        self._max_size = max_size
        self._stack_pointer = 0
        self._stack_list = []

    def is_empty(self):
        #find out it there are any items in the list
        is_empty = True
        if self._items == 0:
            is_empty = False
            print("the list is not empty")
        else:
            print("the list is empty")

    def push(self):
        #pushes an item onto the list
        if self._items => self._max_size:
            print("the list is full you cannot push any more items onto this list")
        else:
            data = input(int("please enter the value you wish to be added to the stack"))
            self._stack_list.append(data)
            self._items += 1
        return 
        

    def pop(self):
        #pops item from the top of the list

    def peek(self):
        # shows the item on the top of the list

    def size(self):
        #states how many items are in the list

    
