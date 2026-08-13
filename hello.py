"""
Hello World 示例程序
"""

def greet(name="World"):
    """向指定的人打招呼"""
    return f"Hello, {name}!"


def main():
    print(greet())
    print(greet("GitHub"))
    print(greet("starwalker-dev"))


if __name__ == "__main__":
    main()
