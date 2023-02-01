class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insertString(self, string):
        currentNode = self.root
        for i in string:
            ch = i
            node = currentNode.children.get(ch)
            if not node:
                node = TrieNode()
                currentNode.children.update({ch: node})
            currentNode = node
        currentNode.endOfString = True
        return


    def searchString(self, string):
        currentNode = self.root
        for i in string:
            ch = i
            node = currentNode.children.get(ch)
            if not node:
                return False
            currentNode = node
        if currentNode.endOfString:
            return True
        return False


new = Trie()
new.insertString("rasheed")
new.insertString("hoi")
print(new.searchString("rasheed"))

