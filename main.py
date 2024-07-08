import graphviz
import tkinter as tk
from tkinter import simpledialog, messagebox, font

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeVisualizer:
    def __init__(self):
        self.graph = graphviz.Digraph()

    def add_node(self, node, parent=None, edge_label=""):
        if node:
            self.graph.node(str(node.data))
            if parent:
                self.graph.edge(str(parent.data), str(node.data), label=edge_label, style="dashed")
            if node.left:
                self.add_node(node.left, node, edge_label="L")
            if node.right:
                self.add_node(node.right, node, edge_label="R")

    def visualize(self, root):
        self.graph.attr(rankdir='TB')
        self.add_node(root)
        return self.graph

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

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

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

class TreeApp:
    def __init__(self, root):
        self.root = root
        self.tree = None

        self.init_ui()

    def init_ui(self):
        self.root.title("Binary Search Tree Visualizer")
        self.root.geometry("400x700")

        self.main_font = font.Font(size=14)

        self.current_nodes_label = tk.Label(self.root, text="Current Nodes: []", font=self.main_font)
        self.current_nodes_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Node", command=self.add_node, font=self.main_font, width=20, height=2, bg="#4CAF50", fg="white")
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Node", command=self.delete_node, font=self.main_font, width=20, height=2, bg="#f44336", fg="white")
        self.delete_button.pack(pady=10)

        self.visualize_button = tk.Button(self.root, text="Visualize Tree", command=self.visualize_tree, font=self.main_font, width=20, height=2, bg="#008CBA", fg="white")
        self.visualize_button.pack(pady=10)

        self.inorder_label = tk.Label(self.root, text="In-order Traversal: []", font=self.main_font)
        self.inorder_label.pack(pady=10)

        self.preorder_label = tk.Label(self.root, text="Pre-order Traversal: []", font=self.main_font)
        self.preorder_label.pack(pady=10)

        self.postorder_label = tk.Label(self.root, text="Post-order Traversal: []", font=self.main_font)
        self.postorder_label.pack(pady=10)

    def update_labels(self):
        if self.tree:
            in_order = self.tree.in_order_traversal()
            pre_order = self.tree.pre_order_traversal()
            post_order = self.tree.post_order_traversal()
            self.current_nodes_label.config(text=f"Current Nodes: {in_order}")
            self.inorder_label.config(text=f"In-order Traversal: {in_order}")
            self.preorder_label.config(text=f"Pre-order Traversal: {pre_order}")
            self.postorder_label.config(text=f"Post-order Traversal: {post_order}")
        else:
            self.current_nodes_label.config(text="Current Nodes: []")
            self.inorder_label.config(text="In-order Traversal: []")
            self.preorder_label.config(text="Pre-order Traversal: []")
            self.postorder_label.config(text="Post-order Traversal: []")

    def add_node(self):
        value = simpledialog.askinteger("Input", "Enter the value to add:")
        if value is not None:
            if self.tree is None:
                self.tree = BinarySearchTreeNode(value)
                self.update_labels()
                messagebox.showinfo("Info", f"Node {value} added")
            else:
                if self.tree.search(value):
                    messagebox.showerror("Error", f"Node {value} already exists")
                else:
                    self.tree.add_child(value)
                    self.update_labels()
                    messagebox.showinfo("Info", f"Node {value} added")

    def delete_node(self):
        value = simpledialog.askinteger("Input", "Enter the value to delete:")
        if value is not None and self.tree:
            if not self.tree.search(value):
                messagebox.showerror("Error", f"Node {value} does not exist")
            else:
                self.tree = self.tree.delete(value)
                self.update_labels()
                messagebox.showinfo("Info", f"Node {value} deleted")

    def visualize_tree(self):
        if self.tree is None:
            messagebox.showwarning("Warning", "Tree is empty")
            return

        visualizer = TreeVisualizer()
        graph = visualizer.visualize(self.tree)
        graph.render('binary_tree', format='png', cleanup=True)
        graph.view()

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeApp(root)
    root.mainloop()
