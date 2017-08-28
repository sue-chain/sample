# -*- coding: utf-8 -*-
# pylint: disable=broad-except

"""try except return finally 执行顺序

无论except是否执行，finally都会执行,且最后执行
无论try except是否有return(有return时，程序暂存返回值)，finally都会执行, 且最后执行
except, finally中return,则会覆盖之前暂存的返回值, so，不要在finally中写return

"""

import logging

__authors__ = ['"sue.chain" <sue.chain@gmail.com>']

logging.getLogger("").setLevel("DEBUG")

def exec_try_finally():
    """顺序执行try finally

    """
    try:
        logging.info("execute try")
    except Exception as error:
        logging.error("execute except")
    finally:
        logging.info("execute finally")

def exec_try_except_finally():
    """顺序执行try finally

    """
    try:
        raise Exception("")
        logging.info("execute try")
    except Exception as error:
        logging.error("execute except")
    finally:
        logging.info("execute finally")

def exec_try_return_finally():
    """顺序执行

    """
    try:
        logging.info("execute try")
        return "return try"
    except Exception as error:
        logging.error("execute except")
    finally:
        logging.info("execute finally")

def exec_except_return_finally():
    """顺序执行

    """
    try:
        logging.info("execute try")
        raise Exception("test") 
    except Exception as error:
        logging.error("execute except")
        return "return except"
    finally:
        logging.info("execute finally")

def exec_finally_return_finally():
    """顺序执行

    """
    try:
        logging.info("execute try")
        raise Exception("test") 
    except Exception as error:
        logging.error("execute except")
        return "return except"
    finally:
        logging.info("execute finally")
        return "return finally"

if __name__ == '__main__':
    #exec_try_finally()
    #exec_try_except_finally()
    #print exec_try_return_finally()
    #print exec_except_return_finally()
    print exec_finally_return_finally()

