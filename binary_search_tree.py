
class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):
        if data == self.data:
            # if the given data is already in the tree then return exists
            return 'already exists in the tree..'
        
        if data < self.data:
            # if the data is less than root then add it to the left side of the tree
            if self.left:
                #if left node is not a leaf
                self.left.add_child(data)
            else:
                #if left node is a leaf node 
                self.left = BinarySearchTreeNode(data)
        else:
            # if the data is greater than root then add it to the right side of the tree
            if self.right:
                #if right node is not a leaf
                self.right.add_child(data)
            else:
                #if right node is a leaf node 
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        # life, root, right 
        elements = []

        # left node here recursion is used to go to the lest most data
        if self.left:
            elements += self.left.in_order_traversal()
        
        # visit the branch or base node
        elements.append(self.data)

        #rignt node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        # root, left, right 
        elements = []
        
        elements.append(self.data)

        if self.left:
            elements += self.left.in_order_traversal()

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        # life, right, root 
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
        
        if self.right:
            elements += self.right.in_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_max()

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # if the node is a leaf just return it 
            if self.left is None and self.right is None:
                return None

            # if the node has one leaf
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # if the node has two branch
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self

    def find_parent(self, data):
        if data == self.left.data:
            return self.data

        if data == self.right.data:
            return self.data
        
        if data != self.data:
            return "given value doesn't exist"
        
        if data < self.data:
            if self.left:
                self.left.close_val(data)
            else:
                pass
        else:
            if self.right:
                self.right.close_val(data)
            else:
                pass
        
    

def build_tree_helper(element):
    root = BinarySearchTreeNode(element[0])

    for i in range(1, len(element)):
        root.add_child(element[i])
    
    return root


def closest_value(root, target):
    a = root.data
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a,b), key=lambda x: abs(target-x))


def is_BST(ele):
    if ele is None:
        return False
    elements = ele.in_order_traversal()

    flag = 0
    i = 1
    while i < len(elements):
        if(elements[i] == elements[i - 1]):
            flag = 0
            break
        if(elements[i] < elements[i - 1]):
            flag = 1
        i += 1
    
    if (not flag) :
        return True
    else :
        return False


num = [12,4,1,20,9,18,34]
numt = build_tree_helper(num)
numt.delete(20)
valu = closest_value(numt, 30)
print('In order search :',numt.in_order_traversal())
print('Post order search :',numt.post_order_traversal())
print('Per Order search :',numt.pre_order_traversal())
print('Closest value to 30 :',valu)
print('is this tree is a BST :',is_BST(numt))


