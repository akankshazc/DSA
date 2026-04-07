/**
 * Check whether a binary tree is a complete binary tree.
 *
 * A complete binary tree is a binary tree in which all the levels are
 * completely filled except possibly the last level and the last level has
 * all keys as left as possible. This class preserves the original algorithm
 * and example while improving readability and adding small wrapper methods.
 */
// Node creation
class Node {
  int data;
  Node left, right;

  Node(int item) {
    data = item;
    left = right = null;
  }
}

class BinaryTree {
  Node root;

  /**
   * Count the number of nodes in the subtree rooted at {@code node}.
   */
  public int countNumNodes(Node root) {
    if (root == null)
      return 0;
    return 1 + countNumNodes(root.left) + countNumNodes(root.right);
  }

  /**
   * Recursive helper to check whether a tree is complete. {@code index}
   * represents the index of the current node in an array representation of
   * the tree and {@code numberNodes} is the total number of nodes.
   */
  public boolean checkComplete(Node root, int index, int numberNodes) {
    if (root == null)
      return true; // empty trees are complete
    if (index >= numberNodes)
      return false;
    return checkComplete(root.left, 2 * index + 1, numberNodes)
        && checkComplete(root.right, 2 * index + 2, numberNodes);
  }

  /**
   * Convenience wrapper: check whether the entire tree is complete.
   */
  public boolean isComplete() {
    int nodeCount = countNumNodes(root);
    return checkComplete(root, 0, nodeCount);
  }

  public static void main(String args[]) {
    BinaryTree tree = new BinaryTree();

    tree.root = new Node(1);
    tree.root.left = new Node(2);
    tree.root.right = new Node(3);
    tree.root.left.right = new Node(5);
    tree.root.left.left = new Node(4);
    tree.root.right.left = new Node(6);

    if (tree.isComplete())
      System.out.println("The tree is a complete binary tree");
    else
      System.out.println("The tree is not a complete binary tree");
  }
}