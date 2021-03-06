# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :  With上下文管理器的用法
   Author :       pengsheng
   date：          2019-04-20
-------------------------------------------------
"""
class MyResource:
    # def __enter__(self):
    #     print('open connect')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     # 在with内部处理异常
    #     if exc_tb:
    #         print('process exception close connect')
    #     else:
    #         print('process success')
    #
    #     return True  # 当返回为True的时候,表示在上下文语句内部处理了异常,外部不会抛出异常了

    def query(self):
        print('query data')
#
# try:
#     with MyResource() as resource:
#         1 / 0
#         resource.query()
# except Exception as ex:
#     print(str(ex))

from contextlib import contextmanager

@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource() # 生成器,类似return; 会中断函数,等外界的函数调用之后,继续执行下面的代码
    print('connect resource collection')

with make_myresource() as r:
    r.query()
    # connect to resource
    # query data
    # connect resource collection