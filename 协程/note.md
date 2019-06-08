# 协程
  - 资料
    - (https://blog.csdn.net/andybegin/article/details/77884645)
    - (http://python.jobbole.com/86481/)
    - (http://python.jobbole.com/87310/)
    - (https://segmentfault.com/a/1190000009781688)
 #  迭代器
  - iterable
    - 直接作用于for循环的叫可迭代对象,Iterable
    - 不但可以作用于for循环,还可以被next调用的,叫Itrator
    - list是典型的可迭代对象，但不是迭代器
    - 可以用isinstance判断
      from collections import Iterable
      l = [1,2,3,4]
      isinstance(l, Iterable)
      
      from collections import Iterator
      isinstance((x for x in range(10)), Iterator)
      
    - iterable和Iterator的关系,可以通过iter函数运算
       isinstance(iter('abc'), Iterator)
 
 # 生成器
  - 