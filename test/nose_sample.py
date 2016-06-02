# -*- coding: utf-8 -*-

__author__ = 'chenjiatan@zhangyue.com'

from nose.tools import assert_raises, raises, set_trace, nottest


class Calc(object):

    """Docstring for Calc.
    """

    def division(self, dividend, divisor):
        """除法
        """
        if divisor == 0:
            raise ZeroDivisionError()
        return dividend / divisor


class TestSample(object):
    """
    Test samplte
    """

    #__test__ = False

    def setup(self):
        """setup"""
        print('setup 方法执行于本类中每条用例之前加载')
        self.calc = Calc()

    def teardown(self):
        """teardown
        """
        print('teardown 方法执行于本类中每条用例之后清理')
        self.calc = None

    #@nottest
    def test_division_result(self):
        """测试除法
        """
        assert self.calc.division(24, 3) == 4

    @raises(ZeroDivisionError)
    def test_division_0(self):
        """测试被除数为0
        """
        raise self.calc.division(24, 0)

    def test_division_0_2(self):
        """测试被除数为0
        """
        set_trace()
        assert_raises(ZeroDivisionError, self.calc.division, 24, 0)

    @classmethod
    def setup_class(cls):
        """setup_class"""
        print('setup_class 类方法执行于本类中任何用例开始之前,且仅执行一次')
