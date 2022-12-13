import os


def main():
    parent = os.path.dirname(__file__)
    with open("README.md", "w") as output:
        output.write("# Images:\n")
        for i in os.listdir(parent):
            if os.path.isfile(i) and i != "README.md" and i != "script.py":
                output.write(f"![image]({i})\n")


if __name__ == '__main__':
    main()
