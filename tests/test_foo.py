from foo import is_a_bigger


def teat_is_a_bigger():
    a = 2
    b = 1
    answer = is_a_bigger(a, b)
    assert answer
