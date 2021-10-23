from my_module import square


def test_quare_fun(input_value):
    sub = square(input_value)

    assert sub == 16
