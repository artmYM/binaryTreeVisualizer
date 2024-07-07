import graphviz

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeVisualizer:
    def __init__(self):
        self.graph = graphviz.Digraph()

    def add_node(self, node):
        if node:
            self.graph.node(str(node.value))
            if node.left:
                self.graph.edge(str(node.value), str(node.left.value))
                self.add_node(node.left)
            if node.right:
                self.graph.edge(str(node.value), str(node.right.value))
                self.add_node(node.right)

    def visualize(self, root):
        self.add_node(root)
        return self.graph


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)


    visualizer = TreeVisualizer()
    graph = visualizer.visualize(root)
    graph.render('binary_tree', format='png', cleanup=True) 
    graph.view() 
