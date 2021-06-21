
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
    
    # insert value fuction serve the purpose of inserting a new list or array into a linked list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    # get_length function count the number of elements in a linked list and return count in int
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    # remove by index fuction remove element in linked list at the given index
    def remove_by_index(self, index):
        if index<0 or index>=self.get_length():
            raise Exception('Index is out of bounds')

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
    
    # remove_by_data fuction remove element in linked list at the given value
    def remove_by_data(self, value):
        try:
            itr = self.head
            while itr:
                if itr.next.data == value:
                    itr.next = itr.next.next
                    break
                itr = itr.next
        except:
            raise Exception('data not found')
    
    # insert fuctions take a index and a data then push it at he place of that index
    def insert_before(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception('Index is out of bounds')
        
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

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
                node = Node(data, itr.next)
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
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def insert_after(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception('Index is out of bounds')
        
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1
    
    def queue_pop(self):
        if self.head is None:
            return
        itr = self.head
        while itr:
            self.head = self.head.next
            break
            itr = itr.next
    
    def stack_pop(self):
        if self.head is None:
            return
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def remove_dub(self):
        if self.head is None:
            return
        itr = self.head
        while itr.next:
            if itr.data == itr.next.data:
                new = itr.next.next
                itr.next = None
                itr.next = new
            else:
                itr = itr.next
        return self.head
    
    def sort_list(self):
        temp=self.head
        while(temp!=None):
            i=temp.next
            while(i!=None):
                if(temp.data>i.data):
                    n=i.data
                    i.data=temp.data
                    temp.data=n
                i=i.next
            temp=temp.next

    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += '[' + str(itr.data) + ']--'
            itr = itr.next
        print(llstr)

    def print_reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

ll = LinkedList()

arr = ['time', 'money', 'tech', 'cat', 'dog', 'tie','last','last','cat']
print(arr)
ll.insert_values(arr)
# ll.insert_at_begining('lol')
# ll.insert_at_end('tiiii')
# ll.insert_before(4, 'bin')
# ll.insert_after(1, 'coun')
# ll.insert_value_after('tiiii', 'after')
# ll.remove_by_data('tie')
# ll.insert_value_before('money', 'before')
# ll.insert_value_before('tiiii', 'before')
# ll.remove_by_index(1)
ll.queue_pop()
ll.stack_pop()
ll.sort_list()
ll.remove_dub()
ll.print()
# ll.print_reverse()
# ll.print()
