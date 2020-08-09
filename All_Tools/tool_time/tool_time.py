#!/usr/bin/python
#-*-coding: utf8-*-
__all__ =["get_fun_running_time", \
          ]
#####内置库########内置库#####内置库###内置库###内置库###内置库###内置库###
import time,sys,os
#####第三方库#####第三方库######第三方库######第三方库#####第三方库#####第三方库####

#####本项目的库，请标注自己名称#####本项目的库，请标注自己名称#####本项目的库，请标注自己名称



#########################装饰器################装饰器###############装饰器#############################
def _flag_fun(flag, fun, time):
    if flag == 0:
        return
    elif flag == 1:
        print("**** the running time of function({})is {} **** ".format(fun.__name__, time))
    else:
        return

def get_fun_running_time(flag:int):
    '''
    creater: SpiritBoy
    :param flag: 0: not print
                 1: not print
    :return: 元组（被调函数返回值，被调函数执行时间）
    time.process_time()会把time.sleep()不计入等时间
    所以用time.perf_counter()
    '''
    def wapper(fun):
        def wapper_deeper(*args, **kw):

            start = time.perf_counter()
            r = fun(*args, **kw)
            end = time.perf_counter()

            _flag_fun(flag, fun, end-start)
            return r,end-start
        return wapper_deeper
    return wapper

#########方法###############方法#################方法###############方法####################





#########类###############类#################类###############类#############################

if __name__ == "__main__":
    '''
    @get_fun_running_time(0)
    def _run():
        print("high spirit boy")
        time.sleep(2)
        print("high spirit boy")
    r = _run()
    print(r[1])
    '''
    for i in range(3):
        print(i)
    print("\n\n\n")
    for i in range(3):
        print(i,end = "")
    pass