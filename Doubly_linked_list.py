
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr
    
    # remove_by_data fuction remove element in linked list at the given value
    def remove_by_data(self, value):
        try:
            itr = self.head
            while itr:
                if itr.data == value:
                    itr.prev.next = itr.next
                    if itr.next:
                        itr.next.prev = itr.prev
                    break
                itr = itr.next
        except:
            raise Exception('data not found')
    
    #this function take a value(existing data) and date and insert date in before the the value 
    def insert_value_before(self, value, data):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.data == value:
                self.insert_at_begining(data)
                break
            elif itr.next.data == value:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
    
    #this function take a value(existing data) and date and insert date in after the the value 
    def insert_value_after(self, value, data):
        if self.head is None:
            return
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break
            itr = itr.next
    
    def pop_from_begining(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        while itr:
            self.head = self.head.next
            break
            itr = itr.next
    
    def pop_from_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        last_node = self.get_last_node()
        itr = last_node
        while itr:
            itr.prev.next = itr.next
            if itr.next:
                itr.next.prev = itr.prev
            break

            itr = itr.next

    
    def print_forward(self):
        if self.head is None:
            print('linked list is empty')
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += '[' + str(itr.data) + ']--'
            itr = itr.next
        print(llstr)
    
    def print_backward(self):
        if self.head is None:
            print('linked list is empty')
            return
        
        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += '[' + str(itr.data) + ']--'
            itr = itr.prev
        print(llstr)


arr = ['time', 'money', 'tech', 'cat', 'dog', 'tie', 'last', 'pen']
ll = DoublyLinkedList()
ll.insert_values(arr)
ll.insert_at_begining(1)
ll.insert_at_end(356)
# ll.remove_by_data('cat')
ll.insert_value_before('tech', 'before')
ll.insert_value_after('tech', 'after')
ll.pop_from_begining()
ll.pop_from_end()
ll.print_forward()

