import pytest

from algorithms.multiply import multiply


def test_true():
    pytest.approx((multiply(2, 3), 6))
