from .context import assert_equal
from sympy import exp, sin, Symbol, E

x = Symbol('x', real=True, positive=True)
y = Symbol('y', real=True, positive=True)


def test_exp_letter():
    assert_equal("e", E)
    assert_equal("e", exp(1))


def test_exp_letter_numeric():
    assert_equal("e^{1}", exp(1, evaluate=False))
    assert_equal("e^{3}", exp(3, evaluate=False))


def test_exp_letter_symbol():
    assert_equal("e^{x}", exp(x, evaluate=False))


def test_exp_letter_symbol_expr():
    assert_equal("e^{x+y}", exp(x + y, evaluate=False))


def test_exp_letter_symbol_expr_group():
    assert_equal("e^{(x+y)}", exp(x + y, evaluate=False))


def test_exp_letter_expr():
    assert_equal("\\sin(x)*e^{x}", sin(x, evaluate=False) * exp(x, evaluate=False))


def test_exp_command():
    assert_equal("\\exponentialE", E)
    assert_equal("\\exponentialE", exp(1))


def test_exp_command_expression():
    assert_equal("\\exponentialE^{3}", exp(3, evaluate=False))


def test_exp_command_multiplied():
    '''
    \\exponentialE is NOT a function, so using the following notation equates to multiplication
    '''
    assert_equal("\\exponentialE (3)", E * 3)
    assert_equal("\\exponentialE \\left( 3\\right)", E * 3)
    assert_equal("\\exponentialE \\times 3", E * 3)


def test_exp_func():
    assert_equal("\\exp(3)", exp(3, evaluate=False))
    assert_equal("\\exp(1)", exp(1, evaluate=False))


def test_exp_func_no_delim():
    assert_equal("\\exp 3", exp(3, evaluate=False))
    assert_equal("\\exp 1", exp(1, evaluate=False))
