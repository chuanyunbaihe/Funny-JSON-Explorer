import argparse
import json
from Factory import TreeFactory, RectangleFactory
from Director import JsonDirector
from IconFamily import IconFamily


def main():
    parser = argparse.ArgumentParser(description='Funny JSON Explorer')
    parser.add_argument('-f', '--file', required=True, help='JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'], help='display style')
    parser.add_argument('-i', '--icon', required=False, choices=['star', 'pocker'], help='icon family')
    args = parser.parse_args()
    with open(args.file, 'r') as file:
        data = json.load(file)

    if args.style == 'tree':
        builder = TreeFactory()
    elif args.style == 'rectangle':
        builder = RectangleFactory()
    else:
        raise ValueError(f"Unknown style: {args.style}")

    icon = IconFamily(args.icon)  # 选择图标族

    # 构造并呈现JSON树
    director = JsonDirector()
    director.construct(builder)
    root = builder.result()
    root.show(icon, data)


if __name__ == '__main__':
    main()
