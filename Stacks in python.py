    """

    # studying the stacks which is called a user defined data type .

    # well there are more like that - : Queues , Linked list , Graphs.

    # STACKS 

    # adding a new element onto the stack is called push .

    # removing an element form the statck is called pop .

    # it can be used to create undo-redo functionalities . 



    This works on the principle of LIFO . (LAST IN FIRST OUT)

    so here what happens , the element which has just lastly entered
    the stack will come out first .

    if i input 1 , 2 , 3 successively in the same way .
    then the first output will be 3 . 

    because the last one entering the stack will leave the stack first

    thats why stcaks are used for creating undo- redo functionalities.


        /\         /\
        \1\       /1/  
            \/↘     ↗\/ 
        |               |
        |_______________|
        |------2.-------|
        |_______________|
        |------3.-------|
        |_______________|



    ||          |||||||||    ||||||||     |||||||||||||
    ||             ||        ||           ||         ||
    ||             ||        |||||||      ||         ||
    ||             ||        ||           ||         ||
    ||||||||   ||||||||||    ||           |||||||||||||


    LAST           IN        FIRST              OUT







    # lets create stacks ...

    """

    class Stacks:
        no_of_stacks = 0 
        def __init__(self) :
            self.items = []
            Stacks.no_of_stacks+=1
        
        def is_empty(self):
            return bool(self.items == [])
        #   return True if len(self.items) == 0 else False
        # both applicable

        def push(self, item) :
            self.items.insert(0 , item)

        def pop(self):
            self.items.pop(0)
        
        def print_stack(self) :
            print(self.items)
        
        def stack_size(self) -> int:
            print(len(self.items))


    first = Stacks()
    first.push("one")
    first.push("two")
    first.push("three")
    first.push("four")
    print(first.is_empty())
    first.stack_size()
    first.print_stack()
    first.pop()
    first.push("five")
    first.print_stack()
    print(first.__dict__)

    print(Stacks.__dict__)
