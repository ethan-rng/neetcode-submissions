class PrefixTree:
    def __init__(self, char=''):
        self.char = '' # holds a single char
        self.children = defaultdict(PrefixTree) # holds a list of children's prefix

    def insert(self, word: str) -> None:
        # Base Case
        if len(word) == 0:
            self.children["*"] = PrefixTree('*')
            return

        # Recursive Case
        if word[0] not in self.children.keys():
            self.children[word[0]]  = PrefixTree(word[0])
        
        self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0: return "*" in self.children.keys()

        currChar = word[0]
        if currChar not in self.children.keys():
            return False
        
        if not self.children[currChar].search(word[1:]):
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0: return True

        currChar = prefix[0]
        if currChar not in self.children.keys():
            return False
        
        return self.children[currChar].startsWith(prefix[1:])
        
        