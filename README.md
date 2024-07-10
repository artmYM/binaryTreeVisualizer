## Binary Search Tree Visualizer
### Description
This script provides a graphical user interface (GUI) to visualize and interact with a Binary Search Tree (BST). Users can add or delete nodes, view the tree structure, and practice traversals. The exercise feature generates a random BST, which users must traverse and input the correct in-order, pre-order, and post-order traversals.

## Code
### Class Initialization
- TreeNode: Represents a node in the tree.
- TreeVisualizer: Handles the visualization of the tree using Graphviz.
- BinarySearchTreeNode: Implements the binary search tree functionality, including adding, searching, deleting nodes, and traversals.
- TreeApp: The main application class using tkinter for the GUI.
### Binary Search Tree Functionality
#### Node Management
- Adding Nodes: Users can add nodes to the tree. The script ensures no duplicate nodes are added.
- Deleting Nodes: Users can delete nodes from the tree. The script ensures non-existing nodes cannot be deleted.
- Searching Nodes: Searches the tree to check if a node exists.
#### Traversals
- In-order Traversal: Left, Root, Right
- Pre-order Traversal: Root, Left, Right
- Post-order Traversal: Left, Right, Root
### Graphical User Interface
#### User Interface Elements
- Labels: Display the current nodes and traversal results.
- Buttons: Allow users to add nodes, delete nodes, visualize the tree, and start an exercise.
- Exercise Window: A new window for traversal exercises with input fields for traversals and a submit button.
#### Tree Visualization
- Visualization: Uses Graphviz to generate a visual representation of the BST.
- Exercise Visualization: Shows the randomly generated tree for the exercise.
## Installation Requirements
Python:

- Ensure you have Python installed (preferably Python 3.6 or later).
Required Packages:

- graphviz: For visualizing the binary search tree.
- tkinter: For creating the graphical user interface.
- random: For generating random trees for exercises.
## Usage
- Running the Script: Execute the script to open the main application window.
- Adding Nodes: Click the "Add Node" button and enter the value of the node to add.
- Deleting Nodes: Click the "Delete Node" button and enter the value of the node to delete.
- Visualizing the Tree: Click the "Visualize Tree" button to generate and display the current tree structure.
- Exercise Mode: Click the "Exercise" button to open a new window, view a randomly generated tree, and input the correct traversals.
## Project's Future
I aim to revise this script to:

- Improve the robustness of the tree generation and visualization algorithms.
- Add more interactive features for educational purposes.
- Enhance the user interface for a better user experience.
