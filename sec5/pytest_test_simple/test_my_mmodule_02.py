from my_module import square
import pytest


@pytest.mark.parametrize(
    'inputs', [2, 3, 4.5]
)
def test_square_return_type(inputs):
    sub = square(inputs)

    assert isinstance(sub, int)
