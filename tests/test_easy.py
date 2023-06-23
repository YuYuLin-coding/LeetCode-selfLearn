import Easy.No66_plus_one
import Easy.No121_best_time_to_buy_and_sell_stock

def test_plus_one():
    a = Easy.No66_plus_one.Solution()
    result = a.plusOne([1, 2, 3])
    assert result == [1, 2, 4]
    result = a.plusOne([4, 3, 2, 1])
    assert result == [4, 3, 2, 2]
    result = a.plusOne([9])
    assert result == [1, 0]

def test_best_time_to_buy_and_sell_stock():
    b = Easy.No121_best_time_to_buy_and_sell_stock.Solution()
    result = b.maxProfit([7,1,5,3,6,4])
    assert result == 5
    result = b.maxProfit([7,6,4,3,1])
    assert result == 0