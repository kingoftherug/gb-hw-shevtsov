def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))


def out_white(text):
    print("\033[37m {}".format(text))


def out_default(text):
    print("\033[0m {}".format(text))


if __name__ == '__main__':
    out_red("Вывод красным цветом")
    out_yellow("Текст жёлтого цвета")
    out_blue("Синий текст")
