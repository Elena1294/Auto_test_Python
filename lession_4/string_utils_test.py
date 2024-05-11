from string_utils import StringUtils
import pytest

@pytest.mark.parametrize('input, result', [("добрый день","Добрый день"), ("hello, word","Hello, word"),("иван","Иван"),("мхат","Мхат"),("море волнунется раз","Море волнунется раз")])
def test_capitilize_positive(input, result):
    string_utils = StringUtils ()
    res = string_utils.capitilize(input)
    assert res == result

@pytest.mark.parametrize('input, result', [("123","123"), ("!@#$%^&*","!@#$%^&*"),("9658 Восемь","9658 восемь"),("GFFGHH","Gffghh"),("КАПС","Капс")])
def test_capitilize_negative(input, result):
    string_utils = StringUtils ()
    res = string_utils.capitilize(input)
    assert res == result

@pytest.mark.parametrize('input, result', [(" добрый день","добрый день"), ("  hello, word","hello, word"), (" море волнунется раз ","море волнунется раз ")])
def test_trim_positive(input, result):
    string_utils = StringUtils ()
    res = string_utils.trim(input)
    assert res == result

@pytest.mark.parametrize('input, result', [("123","123"), ("!@#$%^&*","!@#$%^&*"),("9658 Восемь","9658 Восемь"),("GFFGHH","GFFGHH"),("КАПС","КАПС"), ("   ",""), ("иван ","иван "),("мхат  ","мхат  "), ("","")])
def test_trim_negative(input, result):
    string_utils = StringUtils ()
    res = string_utils.trim(input)
    assert res == result

@pytest.mark.parametrize('input, result', [("добрый,день",["добрый","день"]),("добрый : день",["добрый","день"]),("добрый.день",["добрый","день"]),("добрый!день",["добрый","день"]) ])
def test_to_list_positive(input, result):
    string_utils = StringUtils ()
    res = string_utils.to_list(input)
    assert res == result

@pytest.mark.parametrize('input, result', [("123",["123"]),("fffff",["fffff"]), ("текст без разделителей",["текст без разделителей"])])
def test_to_list_negative(input, result):
    string_utils = StringUtils ()
    res = string_utils.to_list(input)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [("добрый день","д",True), ("hello, word","l",True),("12345","345",True),("мхат","мхат", True),("море волнунется раз"," раз", True)])
def test_contains_positive(input1,input2,result):
    string_utils = StringUtils ()
    res = string_utils.contains(input1,input2)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [("Lghf","123", False), ("!@#$%^&*",")()", False),("9658 Восемь","12", False),("GFFGHH","Gffghh", False),("КАПС","Капс", False)])
def test_contains_negative(input1,input2,result):
    string_utils = StringUtils ()
    res = string_utils.contains(input1,input2)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [("добрый день","день","добрый "), ("hello, word",",", "hello word"),("иван "," ","иван"),("мхат","мх", "ат"),("море волнунется раз"," волнунется ", "морераз")])
def test_delete_symbol_positive(input1,input2,result):
    string_utils = StringUtils ()
    res = string_utils.delete_symbol(input1,input2)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [("  "," ",""), ("!@#$%^&*"," ", "!@#$%^&*")])
def test_delete_symbol_negative(input1,input2,result):
    string_utils = StringUtils ()
    res = string_utils.delete_symbol(input1,input2)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [("добрый день","д",True),("УСТАЛЫЙ ПУТНИК","К",True), ("hello, word","l",False),("12345","345", False),("мхат","мхат",False),("море волнунется раз"," раз", False)])
def test_starts_with(input1,input2,result):
    string_utils = StringUtils ()
    res = string_utils.starts_with(input1,input2)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [("поздний вечер","р", True), ("странный день","д", False), ("hello, word","l",False),("12345","345", False),("мхат","мхат", True),("море волнунется раз"," раз", True)])
def test_end_with(input1,input2,result):
    string_utils = StringUtils ()
    res = string_utils.end_with(input1,input2)
    assert res == result

@pytest.mark.parametrize('input, result', [("",True), ("странный день", False), ("hello, word", False),("12345", False),(" ", False)])
def test_is_empty(input,result):
    string_utils = StringUtils ()
    res = string_utils.is_empty(input)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [(["добрый","день"],",", "добрый,день"), (["123","123","список"],":", "123:123:список")])
def test_list_to_string_positive(input1, input2, result):
    string_utils = StringUtils ()
    res = string_utils.list_to_string(input1, input2)
    assert res == result

@pytest.mark.parametrize('input1, input2, result', [([],"","")])
def test_list_to_string_negative(input1, input2, result):
    string_utils = StringUtils ()
    res = string_utils.list_to_string(input1, input2)
    assert res == result