#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: violinsolo
# Created on 2019/3/8


import time


# ======
# test seconds process time (wall time or CPU time) meets
# ======
def test_time_meets(seconds):
    def deco(func):
        def _deco(*args, **kwargs):
            start = time.clock()
            func(*args, **kwargs)
            end = time.clock()
            if end - start > seconds:
                print('bad!')
            else:
                print('good!')

        return _deco

    return deco


# ======
# print fn running seconds process time (wall time or CPU time)
# ======
def test_time_costs():
    def deco(func):
        # print(func.__name__)
        def _deco(*args, **kwargs):
            start = time.clock()
            func(*args, **kwargs)
            end = time.clock()

            print(f'fn:"{func.__name__}" costs {end - start} seconds')

        return _deco

    return deco



if __name__ == '__main__':

    # ========
    # test time set
    @test_time_meets(1)
    def myfunc(*args, **kwargs):
        for i in range(100000000):
            pass

    myfunc()


    # ========
    # test time costs
    @test_time_costs()
    def myfunc2(*args, **kwargs):
        for i in range(100000):
            pass

    myfunc2()