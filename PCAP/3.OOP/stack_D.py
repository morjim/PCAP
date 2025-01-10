class Stack:
    def __init__(self):
        self.size=0
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)
        self.size +=1
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        self.size -=1
        return val
    
    def __str__(self):
        print(f"Pila= { self.__stack_list}")
            
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0
    def get_sum(self):
        return self.__sum
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
stack_object= AddingStack()

for i in range(5):
    stack_object.push(i)

stack_object.__str__()
print(stack_object.get_sum())