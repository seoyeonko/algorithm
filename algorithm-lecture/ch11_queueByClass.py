# 클래스로 큐 작성하기 
class MyQueue:
    def __init__(self):
        self.queue = []
        
    def get(self):
        return self.queue.pop(0) # FIFO - delete first element
    def put(self, newitem):
        self.queue.append(newitem)
    def empty(self):
        return len(self.queue)==0
    def qsize(self):
        return len(self.queue)


queue = MyQueue()
while True:
    cmd = input(">>> ").split()
    if cmd[0] == "quit": break
    
    if cmd[0] == "get":
        print(queue.get())
    elif cmd[0] == "put":
        queue.put(cmd[1])
    elif cmd[0] == "empty":
        print(queue.empty())
    elif cmd[0] == "qsize":
        print(queue.qsize())