class Node:
    def __init__(self, data:dict):
        '''
        variables:
            data: contains the data of each worker. Should look like this:

                {
                    SSNO: 123121234
                    NAME: "John Doe"
                    DAYS: 00
                    ENTITY: "company.inc"
                }
        '''
        self.__SSNO = data["SSNO"]
        self.__NAME = data["NAME"]
        self.__ENTITY = data["ENTITY"]
        self.__DAYS = 0
        self.__next = None


class WorkersQueue:
    def __init__(self, data):
        new_node = Node(data)
        self.__queue_head:Node = new_node
        self.__queue_last:Node = new_node
        self.__queue_total:int = 0 
        self.__list_head:Node = new_node
        self.__list_last:Node = new_node
        self.__list_total:int = 0


    def push(self, data):
        if (self.not_in_list(data)):
            self.add_list(data)
        self.__queue_last.__next = Node(data)
        self.__queue_last = self.__queue_last.__next
        self.__queue_total = self.__queue_total + 1
    
    def pop(self):
        ret = self.__queue_head
        self.__queue_head = self.__queue_head.__next
        self.__queue_total = self.__queue_total - 1
        return ret

    def add_list(self,data):
        self.__list_last.__next = Node(data)
        self.mergeSort(self.__list_head)
        pass
    
    def sort(self,left,right):
        result = None
        if left.data <= right.data: 
            result = left 
            result.next = self.sort(left.__next, right) 
        else: 
            result = right
            result.next = self.sort(left, right.__next) 
        return result 

    def mergeSort(self, node):
        middle = self.get_middle()
        next_to_middle = middle.__next
        middle.next = None
        left = self.mergeSort(self.__list_head) 
        right = self.mergeSort(next_to_middle) 
        sortedlist = self.sort(left, right)
        return sortedlist 
    
    def get_middle(self):
        current = self.__list_head
        i = 0
        while(i != self.__list_total//2):
            current = current.__next
            i = i+1
        return current

    def not_in_list(self,data):
        current = self.__list_head
        in_list = 0
        while(current.__next != None):
            if(data["SSNO"] == current.__SSNO):
                in_list = in_list +1
        if(in_list == 0):
            return True


