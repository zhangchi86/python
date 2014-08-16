#coding:utf-8
import sys, traceback

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

def func3(*args):
    '''传入的任意多个参数都将放置在一个元组中
    '''
    print args

def func4(**args):
    '''传入的任意多个参数都将放置在一个dict中
    '''
    print args

def func5(a0, a1, a2, a3='defaulta3', a4='defaulta4', *args, **kwargs):
    '''调用的时候non-keyword arg要放在keyword arg之前
    '''
    print 'a0={a0},a1={a1},a2={a2},a3={a3},a4={a4},args={args},kwargs={kwargs}'.format(
            a0=a0,a1=a1,a2=a2,a3=a3,a4=a4,args=args,kwargs=kwargs)

pe('func0(0, 1, 2)')
pe('func0(a0=0, a1=1, a2=2)')
pe('func0(a1=1, a2=2, a0=0)')

pe('func1()')
pe('func1(a0=0, a1=1, a2=2)')
pe('func1(a1=1, a2=2, a0=0)')

pe('func2()')
pe('func2([2])')
pe('func2()')

pe('func3(1,2)')
pe('func3(1)')

pe('func4(a1=1,a2=2)')

try:
    pe('func5(b0=20,b1=21,0,1,2,b2=22,3,4,10,11,12)')
except:
    traceback.print_exc()
try:
    pe('func5(0,1,2,3,4,b0=20,b1=21,10,11,12)')
except:
    traceback.print_exc()
try:
    pe('func5(0,1,2,b0=20,b1=21,a3=3,a4=4)')
except:
    traceback.print_exc()
try:
    pe('func5(0,1,2,3,4,10,11,12,b0=20,b1=21)')
except:
    traceback.print_exc()
