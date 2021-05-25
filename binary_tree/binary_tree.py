import itertools
import logging
import random
import re
from collections import deque
from dataclasses import dataclass
from typing import Optional


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)

    node_right = get_tree(max_depth - 1, level=level + 1)

    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


reg = re.compile(r"[\d]+")


def _get_list_of_nodes(path_to_log_file):
    nodes = []
    with open(path_to_log_file, "r") as log_file:
        val = re.findall(reg, log_file.readline())[0]
        left = None
        right = None
        for line in log_file:
            if "DEBUG" in line:
                if val != re.findall(reg, line)[0]:
                    nodes.append((val, left, right))
                    val = re.findall(reg, line)[0]
                    left = None
                    right = None
                if "left" in line:
                    left = re.findall(reg, line)[1]
                elif "right" in line:
                    right = re.findall(reg, line)[1]
        else:
            nodes.append((val, left, right))
    return nodes


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    nodes = _get_list_of_nodes(path_to_log_file)
    tree = BinaryTreeNode(val=nodes[0][0])
    queue = deque([tree])
    for n in nodes:
        node = queue.popleft()
        if n[1] is not None:
            node.left = BinaryTreeNode(val=n[1]) if n[1] is not None else None
            queue.append(node.left)
        if n[2] is not None:
            node.right = BinaryTreeNode(val=n[2]) if n[2] is not None else None
            queue.append(node.right)
    return tree


if __name__ == "__main__":
    logger = logging.getLogger("tree_walk")
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log.txt",
    )

    root = get_tree(7)

    walk(root)

    # root = restore_tree("walk_log.txt")
    # print(root)
