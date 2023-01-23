class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, string):
        current = self.root
        for i in string:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("successfully inserted")
        return

    def serchString(self, string):
        currentNode = self.root
        for i in string:
            node = currentNode.children.get(i)
            if not node:
                return False
            currentNode = node
        if currentNode.endOfString:
            return True
        else:
            return False


def deleteString(root, string, index):
    ch = string[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, string, index + 1)
        return False

    if index == len(string) - 1:
        if len(currentNode.children) >= 1:
            root.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, string, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, string, index + 1)
    if canThisNodeBeDeleted:
        root.children.pop(ch)
        return True
    else:
        return False





newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Api")
print(deleteString(newTrie.root, "App", 0))
print(newTrie.serchString("App"))
print(newTrie.serchString("Api"))
print(deleteString(newTrie.root, "Api", 0))
print(newTrie.serchString("Api"))


