import Tutorial

def test_add():
    assert Tutorial.add(7,3)== 10
    assert Tutorial.add(7)== 9
    assert Tutorial.add(5)== 7

def test_product():
    assert Tutorial.product(7)== 21
    assert Tutorial.product(7,7) == 49

def test_num():
    assert Tutorial.num(4,0)==4
    assert Tutorial.num(8,9)==8

def test_den():
    assert Tutorial.den(8,9)==9
    assert Tutorial.den(4,0)==0

def test_add_strings():
    phrase=Tutorial.add('Hello','Bridget')
    assert type(phrase) is str
    assert phrase=='HelloBridget'

def test_product_string():
    result=Tutorial.product('Hello',2)
    assert type(result) is str
    assert result== 'HelloHello'