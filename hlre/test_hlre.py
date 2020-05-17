from hlre.hlre import get_highlighting_function
from argparse import Namespace

def test_hl_function():
    args = Namespace(all=False, highlight_style='u', group_highlight_style="b")
    hl = get_highlighting_function(args)

    assert hl(r'.', 'abc').value == '<u>a</u>bc'
    assert hl(r'.+', 'abc').value == '<u>abc</u>'
    assert hl(r'b', 'abc').value == 'a<u>b</u>c'
    assert hl(r'^b', 'abc').value == 'abc'
    assert hl(r'(.)', 'abc').value == '<u><b>a</b></u>bc'
    assert hl(r'(.)$', 'abc').value == 'ab<u><b>c</b></u>'

def test_hl_function_with_all_matches():
    args = Namespace(all=True, highlight_style='u', group_highlight_style="b")
    hl = get_highlighting_function(args)

    assert hl(r'.', 'abc').value == '<u>a</u><u>b</u><u>c</u>'
    assert hl(r'..', 'abc').value == '<u>ab</u>c'
    assert hl(r'(.)', 'abc').value == '<u><b>a</b></u><u><b>b</b></u><u><b>c</b></u>'
