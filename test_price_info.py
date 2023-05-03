import price_info


def test_total_cost():
    result = price_info.total_cost_shopping()

    assert result == 46.75
def test_fruit_cost():
    result = price_info.cost_of_fruits('orange',15)

    assert result == 21