import pytest

from app.rpc.methods import add, divide, multiply, subtract


class TestAdd:
    def test_positive_numbers(self) -> None:
        assert add(1, 2) == 3

    def test_negative_numbers(self) -> None:
        assert add(-1, -2) == -3

    def test_floats(self) -> None:
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_positive_result(self) -> None:
        assert subtract(10, 3) == 7

    def test_negative_result(self) -> None:
        assert subtract(3, 10) == -7


class TestMultiply:
    def test_positive_numbers(self) -> None:
        assert multiply(4, 5) == 20

    def test_by_zero(self) -> None:
        assert multiply(5, 0) == 0


class TestDivide:
    def test_even_division(self) -> None:
        assert divide(10, 2) == 5

    def test_float_result(self) -> None:
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises(self) -> None:
        with pytest.raises(ValueError, match="Division by zero is not allowed."):
            divide(10, 0)
