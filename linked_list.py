# basic node will look like this so this is basic node structure

class node:

    def __init__(self,data=None):
        self.data=data
        self.next=None

# using this basic node structure to make linkedlist

class llist:

    def __init__(self):
        self.head=node()
# function to append a node at the end of linked list
    def appen(self,data):
        new_node=node(data)

        temp=self.head
        if self.head==None:
            self.head=new_node



        while self.head.next:
            self.head=self.head.next

        self.head.next=new_node
        self.head=temp
# function to display the linked list
    def display(self):
        arr=[]

        while self.head.next:

            self.head=self.head.next
            arr.append(self.head.data)
        print(arr)

my_list=llist()
my_list.appen(1)
my_list.appen(2)
my_list.appen(3)
my_list.display()
