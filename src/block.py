from enum import Enum
from re import fullmatch, search
from typing import List


class BlockType(Enum):
    PARAGRAPH = "PARAGRAPH"
    HEADING = "HEADING"
    CODE = "CODE"
    QUOTE = "QUOTE"
    UNORDERED_LIST = "UNORDERED_LIST"
    ORDERED_LIST = "ORDERED_LIST"


def markdown_to_blocks(markdown: str) -> List[str]:
    blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks


def is_ordered_list(block: str) -> bool:
    block = block.strip()
    if not block:
        return False
    expected = 1
    for line in block.splitlines():
        m = fullmatch(r"(\d+)\.\s+.+", line)
        if not m:
            return False
        num = int(m.group(1))
        if num != expected:
            return False
        expected += 1
    return True


def block_to_block_type(markdown) -> BlockType:
    if markdown == "":
        return BlockType.PARAGRAPH
    if search(r"^#{1,6}\s+(.*)$", markdown):
        return BlockType.HEADING
    elif search(r"`{3}([\s\S]*?)`{3}", markdown):
        return BlockType.CODE
    elif all(fullmatch(r">\s?(.+)", line) for line in markdown.splitlines()):
        return BlockType.QUOTE
    elif all(fullmatch(r"-\s*(.+)", line) for line in markdown.splitlines()):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(markdown):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
