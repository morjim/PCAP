class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        return self.queue
    
    def dequeue(self):
        if len(self.queue)>0:
            valor= self.queue.pop(0)
            return valor
        else:
            return "Queue is empty"
        
    def __str__(self):
        return str(self.queue)
        
pila = Queue()
pila.enqueue(1)
pila.enqueue(2)
pila.enqueue(3)
print(pila.__str__()) # [1, 2, 3]

print(pila.dequeue()) # [2, 3]
print(pila.dequeue())

