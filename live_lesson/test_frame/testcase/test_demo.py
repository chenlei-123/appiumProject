def b(fun_12345):  # b装饰了a，所以fun 就是a

    def run_45678(*args, **kwargs):
        print("before a")
        fun_12345(*args, **kwargs)
        print("after a")

    return run_45678


@b
def a():
    print("a")


def test_demo():
    a()
