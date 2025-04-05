// Checking if a binary tree is a perfect binary tree in C++

#include <iostream>
using namespace std;

struct Node
{
    int key;
    struct Node *left, *right;
};

// calculate the depth considering both left and right subtrees
int depth(Node *node)
{
    if (node == NULL)
    {
        return 0;
    }
    int leftDepth = depth(node->left);
    int rightDepth = depth(node->right);
    return max(leftDepth, rightDepth) + 1;
}

// check if the tree is a perfect binary tree
bool isPerfectR(struct Node *root, int d, int level = 0)
{
    if (root == NULL)
        return true;

    if (root->left == NULL && root->right == NULL)
        return (d == level + 1);

    if (root->left == NULL || root->right == NULL)
        return false;

    return isPerfectR(root->left, d, level + 1) &&
           isPerfectR(root->right, d, level + 1);
}

bool isPerfect(Node *root)
{
    int d = depth(root);
    return isPerfectR(root, d);
}

// create a new node
struct Node *newNode(int k)
{
    struct Node *node = new Node;
    node->key = k;
    node->right = node->left = NULL;
    return node;
}

int main()
{
    struct Node *root = NULL;
    root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);

    if (isPerfect(root))
        cout << "The tree is a perfect binary tree\n";
    else
        cout << "The tree is not a perfect binary tree\n";

    return 0;
}