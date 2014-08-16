#coding:utf-8
import sys

def pe(cmd):
    print cmd
    eval(cmd)

def func0(a0, a1, a2):
    print a0, a1, a2

def func1(a0='default0', a1='default1', a2='default2'):
    print a0, a1, a2

def func2(a0=[]):
    '''
    默认参数只会初始化一次，后续就使用第一次初始化的那个值
    '''
    a0.append(1)
    print a0

pe('func0(0, 1, 2)')
pe('func0(a0=0, a1=1, a2=2)')
pe('func0(a1=1, a2=2, a0=0)')

pe('func1()')
pe('func1(a0=0, a1=1, a2=2)')
pe('func1(a1=1, a2=2, a0=0)')

pe('func2()')
pe('func2([2])')
pe('func2()')
