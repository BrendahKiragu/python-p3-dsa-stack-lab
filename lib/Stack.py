class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0
    
    def full(self):
        return len(self.items) == self.limit

    def push(self, item):
        if not self.full():
            self.items.append(item)
        else:
            return None     

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
       if not self.isEmpty():
           return self.items[-1]
       else:
           return None 
    
    def size(self):
        return len(self.items)

    def search(self, target):
        for item in reversed(range(len(self.items))):
            if self.items[item] == target:
                return len(self.items)-1- item
        return -1    

        
