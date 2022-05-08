import sys

class Queue:
    def __init__(self):
        self.queue=[]
        self.head=-1
        self.rear=-1
    def isEmpty(self):
        if (self.head==self.rear):
            return True
        else:
            return False
    def enqueue(self, data):
        self.queue.append(data)
        self.rear+=1
    def dequeue(self):
        if self.isEmpty():
            return -1
        else:
            self.head+=1
            dequeued=self.queue[self.head]
            return dequeued
    def size(self):
        return (self.rear-self.head)
    def front(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head+1]
    def back(self):
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.rear]
        

n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(sys.stdin.readline())
    
Q=Queue()
for _ in arr:
    tmp=_.split()
    if tmp[0]=='push':
        Q.enqueue(tmp[1])
    elif tmp[0]=='pop':
        print(Q.dequeue())
    elif tmp[0]=='size':
        print(Q.size())
    elif tmp[0]=='empty':
        if(Q.isEmpty()):
            print(1)
        else:
            print(0)
    elif tmp[0]=='front':
        print(Q.front())
    elif tmp[0]=='back':
        print(Q.back())
