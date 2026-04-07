/**
 * Simple binary tree demonstration with recursive traversals (preorder,
 * inorder, postorder). The implementation preserves the traversal logic
 * used by the original example; the changes here are purely stylistic and
 * API additions for readability.
 */

// Node creation
class Node {
    int key;
    Node left, right;

    /**
     * Create a new tree node containing {@code item}.
     */
    public Node(int item) {
        key = item;
        left = right = null;
    }
}

class BinaryTree {
    Node root;

    /**
     * Construct a binary tree with a single root node containing {@code key}.
     */
    BinaryTree(int key) {
        root = new Node(key);
    }

    /**
     * Construct an empty binary tree.
     */
    BinaryTree() {
        root = null;
    }

    // Traverse Inorder (left, root, right)
    public void traverseInOrder(Node node) {
        if (node != null) {
            traverseInOrder(node.left);
            System.out.print(" " + node.key);
            traverseInOrder(node.right);
        }
    }

    // Convenience wrapper: traverse the whole tree inorder
    public void traverseInOrder() {
        traverseInOrder(root);
    }

    // Traverse Postorder (left, right, root)
    public void traversePostOrder(Node node) {
        if (node != null) {
            traversePostOrder(node.left);
            traversePostOrder(node.right);
            System.out.print(" " + node.key);
        }
    }

    // Convenience wrapper: traverse the whole tree postorder
    public void traversePostOrder() {
        traversePostOrder(root);
    }

    // Traverse Preorder (root, left, right)
    public void traversePreOrder(Node node) {
        if (node != null) {
            System.out.print(" " + node.key);
            traversePreOrder(node.left);
            traversePreOrder(node.right);
        }
    }

    // Convenience wrapper: traverse the whole tree preorder
    public void traversePreOrder() {
        traversePreOrder(root);
    }

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();

        tree.root = new Node(1);
        tree.root.left = new Node(2);
        tree.root.right = new Node(3);
        tree.root.left.left = new Node(4);

        System.out.print("Pre order Traversal: ");
        tree.traversePreOrder();
        System.out.print("\nIn order Traversal: ");
        tree.traverseInOrder();
        System.out.print("\nPost order Traversal: ");
        tree.traversePostOrder();
    }
}