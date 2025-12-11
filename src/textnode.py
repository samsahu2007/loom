from enum import Enum


class TextType(Enum):
    PLAIN = "PLAIN"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    IMAGE = "IMAGE"


class TextNode:
    def __init__(self, txt: str, node_type: TextType, url: str | None = None) -> None:
        self.text: str = txt
        self.node_type: TextType = node_type
        self.url: str | None = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return NotImplemented

        return (
            self.text == other.text
            and self.node_type == other.node_type
            and self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.node_type.value}, {self.url})"
