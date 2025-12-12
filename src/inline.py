from typing import List, Tuple
from textnode import TextType, TextNode
from re import findall


def split_nodes_delimiter(
    old_nodes: List[TextNode], delimiter: str, text_type: TextType
):
    new_nodes: List[TextNode] = []
    for old_node in old_nodes:
        if old_node.node_type != TextType.PLAIN:
            new_nodes.append(old_node)
            continue
        parts = old_node.text.split(delimiter, 2)
        if len(parts) == 2:
            # It means no closing delimiter
            raise ValueError(f"Could Not find closing delimiter for {old_node}")
        for idx, part in enumerate(parts):
            if not idx & 1:
                new_nodes.append(TextNode(part, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes


def extract_markdown_images(text: str) -> List[Tuple[str, str]]:
    matches =  findall(r"!\[([\w\s]+)\]\(([^\(\)]*)\)", text)
    return matches


def extract_markdown_links(text: str) -> List[Tuple[str, str]]:
    matches = findall(r"\[([\w\s]+)\]\(([^\(\)]*)\)", text)
    return matches