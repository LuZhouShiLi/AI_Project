import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char  # 字符
        self.freq = freq  # 频率
        self.left = None  # 左子节点
        self.right = None  # 右子节点

    def __lt__(self, other):
        return self.freq < other.freq  # 定义节点之间的小于比较，根据频率进行比较

def huffman_encoding(data):
    if not data:
        return "", {}, {}  # 处理空数据的情况，返回空的编码结果、空的字符编码和频率

    # 统计字符频率
    freq_map = defaultdict(int)  # 用于存储字符频率的字典
    for char in data:
        freq_map[char] += 1  # 统计每个字符的出现频率

    # 创建Huffman树
    heap = []  # 最小堆，用于构建Huffman树
    for char, freq in freq_map.items():
        node = HuffmanNode(char, freq)  # 创建Huffman节点
        heapq.heappush(heap, node)  # 将节点加入最小堆

    if len(heap) == 1:
        # 处理只有一个字符的情况
        node = heapq.heappop(heap)  # 弹出唯一的节点
        root = HuffmanNode(None, node.freq)  # 创建虚拟根节点
        root.left = node  # 将节点作为根节点的左子节点
    else:
        while len(heap) > 1:
            left_node = heapq.heappop(heap)  # 弹出频率最低的节点作为左子节点
            right_node = heapq.heappop(heap)  # 弹出频率次低的节点作为右子节点
            merged_node = HuffmanNode(None, left_node.freq + right_node.freq)  # 创建合并节点，频率为左右子节点频率之和
            merged_node.left = left_node  # 将左子节点赋值给合并节点的左子节点
            merged_node.right = right_node  # 将右子节点赋值给合并节点的右子节点
            heapq.heappush(heap, merged_node)  # 将合并节点加入最小堆

        root = heapq.heappop(heap)  # 最后剩下的节点即为根节点

    # 生成编码映射
    code_map = {}  # 存储字符和对应编码的字典
    generate_code_map(root, "", code_map)  # 生成字符的编码映射

    # 生成编码结果
    encoded_data = "".join(code_map[char] for char in data)  # 根据编码映射将数据进行编码

    # 返回编码结果、字符编码和频率
    return encoded_data, code_map, freq_map

def generate_code_map(node, current_code, code_map):
    if node is None:
        return
    if node.char:
        code_map[node.char] = current_code  # 如果当前节点是叶子节点，将字符和对应编码添加到编码映射中
        return
    generate_code_map(node.left, current_code + "0", code_map)  # 递归遍历左子树，并在当前编码末尾添加'0'
    generate_code_map(node.right, current_code + "1", code_map)  # 递归遍历右子树，并在当前编码末尾添加'1'
