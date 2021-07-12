#           ""
#         c   d
#     a           o
# t(true)   m       g(true)
#   s(true)     p(true)   s(true)

# root: {c: {a : {t: {s: {}}, m : {p: {}}}}, d: {o: {g : {s: {}}}} 

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.isWord = False

    def __str__(self) -> str:
        children = ""
        for k, v in self.children.items():
            children = "{}{}[{}]".format(children, k, str(v))
        return children

class Trie:
    def __init__(self) -> None:
        #initialize the trie data structure
        self.root = Node()

    def __str__(self) -> str:
        return str(self.root)

    def insert(self, word):
        #O(N) if N chars in word
        #Insert a word into the trie
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = Node()
            curNode = curNode.children[c]
        curNode.isWord = True

    def search(self, word):
        #O(N) if N chars in word
        #Search for a word in the trie
        curNode = self.root
        for c in word:
            if c in curNode.children:
                curNode = curNode.children[c]
            else:
                return False
        return curNode.isWord

    def startsWith(self, prefix):
        #O(N) if N chars in word
        #Search for words with the given prefix in the trie
        curNode = self.root
        for c in prefix:
            if c in curNode.children:
                curNode = curNode.children[c]
            else:
                return False
        return True


if __name__ == "__main__":
    trie = Trie()
    print(trie.insert("cat"))
    print(trie.search("cat"))
    print(trie.insert("cats"))
    print(trie.search("cats"))
    print(trie.insert("camp"))
    print(trie.insert("dog"))
    print(trie.insert("dogs"))
    print(trie.search("dogma"))
    print(trie.startsWith("ca"))
    print(trie.startsWith("do"))
    print(trie)
