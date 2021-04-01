"""

queue are another kind of user defined data structures . 

in this kind of data structures the element which goes first comes out first ..

this kind of addding and removing the elements feature is called FIFO .

FIFO -: First In First Out .
"""
class Queue: 
    
    def __init__(self) :
        self.items = [] 

    def enqueue(self , item):
        self.items.insert(0 , item)

    def dequeue(self) :
        self.items.pop() 

    def is_empty( self) :
        bool(self.items == [])

    def print_queue(self ) :
        print(self.items)


queue = Queue()

queue.enqueue(10) 
queue.enqueue(15)
queue.enqueue(20)
queue.dequeue()
queue.print_queue()
