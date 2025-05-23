
// Deletion operation on a B+ Tree in C++

#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

#define MIN_DEGREE 3 // Minimum degree (defines the range for number of keys)

class BPlusTreeNode
{
public:
    bool leaf;
    std::vector<int> keys;
    std::vector<BPlusTreeNode *> children;
    BPlusTreeNode *parent;
    int numKeys;

    BPlusTreeNode(bool _leaf) : leaf(_leaf), numKeys(0), parent(nullptr) {}

    void insertNonFull(int key);
    void splitChild(int index, BPlusTreeNode *y);
    void remove(int key);
    void removeFromLeaf(int idx);
    void removeFromNonLeaf(int idx);
    int getPred(int idx);
    int getSucc(int idx);
    void borrowFromPrev(int idx);
    void borrowFromNext(int idx);
    void merge(int idx);

    friend class BPlusTree;
};

class BPlusTree
{
    BPlusTreeNode *root;

public:
    BPlusTree() { root = new BPlusTreeNode(true); }

    void insert(int key);
    void remove(int key);
    void traverse() { traverse(root); }

private:
    void traverse(BPlusTreeNode *node);
    BPlusTreeNode *search(BPlusTreeNode *node, int key);
};

void BPlusTreeNode::insertNonFull(int key)
{
    int i = numKeys - 1;

    if (leaf)
    {
        keys.push_back(0); // Add a dummy value to expand the keys vector
        while (i >= 0 && key < keys[i])
        {
            keys[i + 1] = keys[i];
            i--;
        }
        keys[i + 1] = key;
        numKeys++;
    }
    else
    {
        while (i >= 0 && key < keys[i])
        {
            i--;
        }
        i++;

        if (children[i]->numKeys == 2 * MIN_DEGREE - 1)
        {
            splitChild(i, children[i]);
            if (key > keys[i])
            {
                i++;
            }
        }
        children[i]->insertNonFull(key);
    }
}

void BPlusTreeNode::splitChild(int index, BPlusTreeNode *y)
{
    BPlusTreeNode *z = new BPlusTreeNode(y->leaf);
    z->numKeys = MIN_DEGREE - 1;

    for (int j = 0; j < MIN_DEGREE - 1; j++)
    {
        z->keys.push_back(y->keys[j + MIN_DEGREE]);
    }

    if (!y->leaf)
    {
        for (int j = 0; j < MIN_DEGREE; j++)
        {
            z->children.push_back(y->children[j + MIN_DEGREE]);
        }
    }

    y->numKeys = MIN_DEGREE - 1;

    children.insert(children.begin() + index + 1, z);
    keys.insert(keys.begin() + index, y->keys[MIN_DEGREE - 1]);
    numKeys++;
}

void BPlusTreeNode::remove(int key)
{
    int idx = std::lower_bound(keys.begin(), keys.end(), key) - keys.begin();

    if (idx < numKeys && keys[idx] == key)
    {
        if (leaf)
        {
            removeFromLeaf(idx);
        }
        else
        {
            removeFromNonLeaf(idx);
        }
    }
    else
    {
        if (leaf)
        {
            std::cout << "The key " << key << " is not present in the tree.\n";
            return;
        }

        bool flag = ((idx == numKeys) ? true : false);

        if (children[idx]->numKeys < MIN_DEGREE)
        {
            borrowFromPrev(idx);
            children[idx]->remove(key);
        }
        else
        {
            children[idx]->remove(key);
        }
    }
}

void BPlusTreeNode::removeFromLeaf(int idx)
{
    for (int i = idx + 1; i < numKeys; i++)
    {
        keys[i - 1] = keys[i];
    }
    keys.pop_back();
    numKeys--;
}

void BPlusTreeNode::removeFromNonLeaf(int idx)
{
    int key = keys[idx];

    if (children[idx]->numKeys >= MIN_DEGREE)
    {
        int pred = getPred(idx);
        keys[idx] = pred;
        children[idx]->remove(pred);
    }
    else if (children[idx + 1]->numKeys >= MIN_DEGREE)
    {
        int succ = getSucc(idx);
        keys[idx] = succ;
        children[idx + 1]->remove(succ);
    }
    else
    {
        merge(idx);
        children[idx]->remove(key);
    }
}

int BPlusTreeNode::getPred(int idx)
{
    BPlusTreeNode *cur = children[idx];
    while (!cur->leaf)
    {
        cur = cur->children[cur->numKeys];
    }
    return cur->keys[cur->numKeys - 1];
}

int BPlusTreeNode::getSucc(int idx)
{
    BPlusTreeNode *cur = children[idx + 1];
    while (!cur->leaf)
    {
        cur = cur->children[0];
    }
    return cur->keys[0];
}

void BPlusTreeNode::borrowFromPrev(int idx)
{
    BPlusTreeNode *child = children[idx];
    BPlusTreeNode *sibling = children[idx - 1];

    for (int i = child->numKeys - 1; i >= 0; i--)
    {
        child->keys[i + 1] = child->keys[i];
    }

    if (!child->leaf)
    {
        for (int i = child->numKeys; i >= 0; i--)
        {
            child->children[i + 1] = child->children[i];
        }
    }

    child->keys[0] = keys[idx - 1];

    if (!leaf)
    {
        child->children[0] = sibling->children[sibling->numKeys];
    }

    keys[idx - 1] = sibling->keys[sibling->numKeys - 1];

    child->numKeys += 1;
    sibling->numKeys -= 1;
}

void BPlusTreeNode::borrowFromNext(int idx)
{
    BPlusTreeNode *child = children[idx];
    BPlusTreeNode *sibling = children[idx + 1];

    child->keys[child->numKeys] = keys[idx];

    if (!(child->leaf))
    {
        child->children[child->numKeys + 1] = sibling->children[0];
    }

    keys[idx] = sibling->keys[0];

    for (int i = 1; i < sibling->numKeys; i++)
    {
        sibling->keys[i - 1] = sibling->keys[i];
    }

    if (!sibling->leaf)
    {
        for (int i = 1; i <= sibling->numKeys; i++)
        {
            sibling->children[i - 1] = sibling->children[i];
        }
    }

    child->numKeys += 1;
    sibling->numKeys -= 1;
}

void BPlusTreeNode::merge(int idx)
{
    BPlusTreeNode *child = children[idx];
    BPlusTreeNode *sibling = children[idx + 1];

    child->keys[MIN_DEGREE - 1] = keys[idx];

    for (int i = 0; i < sibling->numKeys; i++)
    {
        child->keys[i + MIN_DEGREE] = sibling->keys[i];
    }

    if (!child->leaf)
    {
        for (int i = 0; i <= sibling->numKeys; i++)
        {
            child->children[i + MIN_DEGREE] = sibling->children[i];
        }
    }

    for (int i = idx + 1; i < numKeys; i++)
    {
        keys[i - 1] = keys[i];
    }

    for (int i = idx + 2; i <= numKeys; i++)
    {
        children[i - 1] = children[i];
    }

    child->numKeys += sibling->numKeys + 1;
    numKeys--;
    delete sibling;
}

void BPlusTree::insert(int key)
{
    BPlusTreeNode *r = root;
    if (r->numKeys == 2 * MIN_DEGREE - 1)
    {
        BPlusTreeNode *s = new BPlusTreeNode(false);
        root = s;
        s->children.push_back(r);
        s->splitChild(0, r);
        s->insertNonFull(key);
    }
    else
    {
        r->insertNonFull(key);
    }
}

void BPlusTree::remove(int key)
{
    root->remove(key);
    if (root->numKeys == 0)
    {
        BPlusTreeNode *oldRoot = root;
        if (root->leaf)
        {
            root = nullptr;
        }
        else
        {
            root = root->children[0];
        }
        delete oldRoot;
    }
}

void BPlusTree::traverse(BPlusTreeNode *node)
{
    if (node)
    {
        int i;
        for (i = 0; i < node->numKeys; i++)
        {
            if (!node->leaf)
            {
                traverse(node->children[i]);
            }
            std::cout << node->keys[i] << "";
        }
        if (!node->leaf)
        {
            traverse(node->children[i]);
        }
    }
}

int main()
{
    BPlusTree tree;
    tree.insert(10);
    tree.insert(20);
    tree.insert(5);
    tree.insert(6);
    tree.insert(15);

    std::cout << "Tree after insertions: ";
    tree.traverse();
    std::cout << std::endl;

    tree.remove(10);
    std::cout << "Tree after deleting 10: ";
    tree.traverse();
    std::cout << std::endl;
    return 0;
}
