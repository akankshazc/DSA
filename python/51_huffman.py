"""
Huffman Coding in Python.
Generates Huffman codes for characters in a string based on their frequencies.
"""

from typing import Dict, Any


class NodeTree:
    """
    Node for Huffman tree.
    """

    def __init__(self, left: Any = None, right: Any = None) -> None:
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self) -> str:
        return f'{self.left}_{self.right}'


def huffman_code_tree(node: Any, left: bool = True, binString: str = '') -> Dict[str, str]:
    """
    Recursively builds Huffman codes for each character.

    Args:
        node (Any): Current node or character.
        left (bool): Direction flag.
        binString (str): Current binary string.

    Returns:
        Dict[str, str]: Mapping of character to Huffman code.
    """
    if isinstance(node, str):
        return {node: binString}
    l, r = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


if __name__ == "__main__":
    string = 'BCAADDDCCACACAC'
    freq = {}
    for c in string:
        freq[c] = freq.get(c, 0) + 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    nodes = freq
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    huffmanCode = huffman_code_tree(nodes[0][0])
    print(' Char | Huffman code ')
    print('----------------------')
    for (char, frequency) in freq:
        print(f' {char!r:4} |{huffmanCode[char]:12}')
