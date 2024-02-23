from mypackage import mymodule

def test_top_n():
    """ test that top_n works correctly """
    
    assert mymodule.top_n([8, 3, 7, 4, 2], 3) == [8, 7, 4], "incorrect"
    assert mymodule.top_n([5, 1, 2, 9, 6], 2) == [9, 6], "incorrect"
    assert mymodule.top_n([1, 2, 3, 4, 5], 1) == [5], "incorrect"