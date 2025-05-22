
# 模式匹配
score = "B"

match score:
    case "A":
        print("is A")
    case "B":
        print("is B")
    case _:
        print("ans is ???.")