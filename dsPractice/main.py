class BinaryHeap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peek_node(root_node):
    if not root_node:
        return
    else:
        return root_node.customList[1]


def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heapSize


def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        if root_node.customList:
            for i in range(1, root_node.heapSize + 1):
                print(root_node.customList[i])
        return


def heapify_insert(rootNode, index, heap_type):
    parent_index = int(index / 2)
    if index <= 1:
        return
    if heap_type == 'Min':
        if rootNode.customList[index] < rootNode.customList[parent_index]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parent_index]
            rootNode.customList[parent_index] = temp
        heapify_insert(rootNode, parent_index, heap_type)

    if heap_type == 'Max':
        if rootNode.customList[index] > rootNode.customList[parent_index]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parent_index]
            rootNode.customList[parent_index] = temp
        heapify_insert(rootNode, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
    if root_node.heapSize + 1 == root_node.maxSize:
        return "Heap is full"
    else:
        root_node.customList[root_node.heapSize + 1] = node_value
        root_node.heapSize += 1
        heapify_insert(root_node, root_node.heapSize, heap_type)
        return "the value is inserted"


new_tree = BinaryHeap(5)
insert_node(new_tree, 5, 'Min')
insert_node(new_tree, 4, 'Min')
insert_node(new_tree, 3, 'Min')
insert_node(new_tree, 8, 'Min')
insert_node(new_tree, 1, 'Max')

# print(peek_node(new_tree))
# print(size_of_heap(new_tree))
level_order_traversal(new_tree)





