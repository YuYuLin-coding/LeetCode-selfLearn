from Easy.No66_plus_one import Solution


def test_plus_one():
    a = Solution()
    result = a.plusOne([1,2,3])
    assert result == [1,2,4]
    result = a.plusOne([4,3,2,1])
    assert result == [4,3,2,2]
    result = a.plusOne([9])
    assert result == [1,0]