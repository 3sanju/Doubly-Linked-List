class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n
    def insert_at_last(self,data):
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,data,None)
            #n.prev=temp
            temp.next=n
        else:
            n=Node(None,data,None)
            self.start=n
    def search(self,data):
        temp=self.start
        while temp is not None:
            if(temp.item==data):
                return temp
            temp=temp.next
        return None 
    def insert_after(self,temp,data):
        if temp is not None:
           n=Node(temp,data,temp.next)
           if temp.next is not None:
              temp.next.prev=n
           temp.next=n
    def print_List(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None
    def delete_last(self):
        if self.start is None: #Checks if the node is empty
            pass
        elif self.start.next is None: #Checks if the list has single node
            self.start=None
        else:
            temp=self.start 
            while temp.next is not None: #Condition when node has n number of nodes
                temp=temp.next
            temp.prev.next=None #Assign Node to the next of the previous node of temp
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next
my_list=DLL()
my_list.insert_at_start(20)
my_list.insert_at_start(30)
my_list.insert_at_last(50)
my_list.insert_after(my_list.search(30),40)
my_list.print_List()






            


    

      
