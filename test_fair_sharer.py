from fair_sharer import fair_sharer

def test_fair_sharer():
    # Test case 1
    result = fair_sharer([0, 1000, 800, 0], 1)
    assert result == [100, 800, 900, 0], f"Expected [100, 800, 900, 0], but got {result}"

    # Test case 2
    result = fair_sharer([0, 1000, 800, 0], 2)
    assert result == [100, 890, 720, 90], f"Expected [100, 890, 720, 90], but got {result}"
