class BankQueue:
    def __init__(self):
        self.__queue = []
    
    @property
    def queue(self):
        return self.__queue

    def push(self, operation):
        self.__queue.append(operation)
        return self.__queue

    def pop(self):
        if len(self.__queue)>0:
            self.__queue.pop(0)
            return self.__queue
        else:
             return "queue already empty"

    def clear(self):
        self.__queue.clear()
        return self.__queue
