from price_info import total_cost_shopping, cost_of_fruits
def test_total_cost_shopping():
    expected_total_cost = 5 * 1.20 + 5 * 1.40 + 1 * 6.50 + 2 * 2.70 + 10 * 0.90 + 1 * 2.95 + 2 * 4.95
    assert total_cost_shopping() == expected_total_cost

def test_cost_of_fruits():
    assert cost_of_fruits('apple', 5) == 6.0
    assert cost_of_fruits('orange', 5) == 7.0
    assert cost_of_fruits('watermelon', 1) == 6.50
    assert cost_of_fruits('pineapple', 2) == 5.40
    assert cost_of_fruits('pear', 10) == 9.0
    assert cost_of_fruits('papaya', 2) == 5.9
    assert cost_of_fruits('pomegranate', 2) == 9.90
