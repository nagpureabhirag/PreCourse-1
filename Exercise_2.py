
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.head = None

        
    def push(self, data):
        '''
        Pushes element on top of stack
        ---------
        arguments:
        data: int - value to push
        ---------
        returns:
        None
        TC: O(1)
        SC: O(1)
        '''
        temp = Node(data)
        temp.next = self.head
        self.head = temp
        # self.display()

        
    def pop(self):
        '''
        Pop element from stack
        --------
        arguments:
        None
        ---------
        returns:
        value: int - value at top popped from stack
        TC: O(1)
        SC: O(1)
        '''
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        # self.display()
        return value

    
    # def display(self):
    #     temp = self.head
    #     s = []
    #     while temp:
    #         s.append(temp.data)
    #         temp = temp.next
    #     print(s)
        
a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
