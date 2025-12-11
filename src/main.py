from textnode import TextNode, TextType

print("Hello WOrld")


def main():
    node = TextNode("This is some anchor text", TextType.PLAIN, "https://www.boot.dev")
    print(node)


main()
