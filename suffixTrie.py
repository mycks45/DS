
class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

    
class Trie:
    def __init__(self):
        self.root = TrieNode()      
        

    def trie(self, str_val):
        for i in range(len(str_val)):
            self.populateSuffixTrie(i, str_val)
        

    def populateSuffixTrie(self, index, str_val):
        
        node = self.root
        i = index
        srt_len = len(str_val)
        while i < srt_len:
            letter = str_val[i]
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode()
                node.children[letter] = new_node
                node = new_node
            i += 1
            
        node.is_end = True


    def contains(self, search_str):
        node = self.root
        for i in search_str:
            if not i in node.children.keys():
                return False
            else:
                node = node.children[i]
        return node.is_end # return true if exist


word = Trie()
word.trie('mannan')
word.trie('anfus')
word.trie('man')
word.trie('harshad')


print(word.contains('harshad'))
print(word.contains('arshad'))
print(word.contains('rshad'))
print(word.contains('shad'))
print(word.contains('had'))
print(word.contains('ad'))
print(word.contains('d'))