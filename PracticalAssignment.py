class node:
    def __init__(self,pid,name,pr):
        self.pid=pid
        self.name=name
        self.priority=pr
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=self.rear=None

    # Add Process
    def enqueue(self,new_node):
        if self.front==None:
            self.front=self.rear=new_node
            return

        if self.front.priority>new_node.priority:
            new_node.next=self.front
            self.front=new_node
            return

        else:
            temp=self.front
            while temp:
                if new_node.priority<temp.priority:
                    break
                else:
                    prev=temp
                    temp=temp.next

            prev.next=new_node
            new_node.next=temp

            if temp==None:
                self.rear=new_node

    # Execute Process
    def dequeue(self):
        if self.front:
            temp=self.front
            print("Executed Process:",temp.pid,temp.name)
            self.front=self.front.next

            if self.front==None:
                self.rear=None
        else:
            print("No process to execute")

    # View Next Process
    def display_next(self):
        if self.front:
            print("Next Process:",self.front.pid,
                  self.front.name,self.front.priority)
        else:
            print("No pending processes")

    # Display All Processes
    def display_all(self):
        temp=self.front
        if temp==None:
            print("Queue is empty")
            return

        while temp:
            print(temp.pid,temp.name,temp.priority)
            temp=temp.next

    # Count Processes
    def count(self):
        temp=self.front
        c=0
        while temp:
            c=c+1
            temp=temp.next

        print("Total pending processes:",c)


# Create Priority Queue
pq=PriorityQueue()

pq.enqueue(node(101,"System",1))
pq.enqueue(node(102,"Browser",2))
pq.enqueue(node(103,"Background",3))
pq.enqueue(node(104,"File",4))

print("All Processes:")
pq.display_all()

print("\nNext Process:")
pq.display_next()

print("\nExecuting Process:")
pq.dequeue()

print("\nAll Pending Processes:")
pq.display_all()

print("\nCounting Processes:")
pq.count()