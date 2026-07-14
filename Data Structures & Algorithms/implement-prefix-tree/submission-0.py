class TrieNode:
    def __init__(self):
       self.collection= {}
       self.end = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.collection:
                curr.collection[c] = TrieNode()

            curr = curr.collection[c] 

        curr.end = True     

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.collection:
                return False

            curr = curr.collection[c] 

        if curr.end == True:
            return True
        else:
            return False      

    def startsWith(self, prefix: str) -> bool: 
        curr = self.root 
        
        
        for c in prefix: 
            if c not in curr.collection: 
                return False 
            curr = curr.collection[c] 
            
        return True         
        