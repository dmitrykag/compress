def compress(to_compress): # return 0-1 string
    freqs = {} # 1. посчитаем частоты символов

    # 2. построить дерево Хаффмана
    nodes = build_leaves(freqs)

    root = build_huffman_tree(nodes)

    # 3. найти по этому дереву коды символов
    codes = build_codes(root)

    # 4. заменить буквы в исходной строке кодами 
    return encode(to_compress, codes)

def encode(to_compress, codes):
    return ""

def build_codes(tree):
    return {}

class HuffmanNode:
    def __init__(self, letters, freq):
        self.letters = letters
        self.freq = freq
        self.left = None
        self.right = None

def build_leaves(freqs):
    res = []
    for s in freqs:
       res.append(HuffmanNode(s, freqs[s]))
    return res

def build_huffman_tree(nodes):
    while len(nodes) > 1:
        node1 = extract_min(nodes)
        node2 = extract_min(nodes)
        new_node = HuffmanNode(node1.letters + node2.letters, node1.freq + node2.freq)
        new_node.left, new_node.right = node1, node2
        nodes.append(new_node)
    return nodes[0]