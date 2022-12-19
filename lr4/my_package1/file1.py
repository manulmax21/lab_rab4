
def get_func(tag):
    tag1 = "<" + tag + ">"
    tag2 = "</" + tag + ">"
    print("<ol>")
    def func(string):
        nonlocal tag1
        nonlocal tag2
        for i in range(len(string)):
            print(tag1 + " " + string[i] + " " + tag2)
        print("</ol>")
    return func

