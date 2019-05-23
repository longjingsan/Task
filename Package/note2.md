#  1,模块
 - 一个模块就是一个包含pytho代码的文件， 后缀名成是.py就可以，模块就是个python文件
 - 为什么我们用模块
  - 程序太大，编写维护非常不方便，需要拆分
  - 模块可以增加代码重复利用的方式
  - 当做命名空间使用，避免命名冲突
 - 如何定义模块
  - 模块就是一个普通文件，所以任何代码可以直接书写，
  - 不过根据模块的规范，最好在模块中编写以下内容
    - 函数（单一功能，类似于Mixin），即要求高内聚，低耦合
    - 类（相似功能的组合，或者类似业务模块）
    - 测试代码，用着的时候可以修改，拓展之后还可以测试，方便别人用
  - 语法
       - import module.name
       - module_name.function
       - module_name.class_name
    - 
 - 如何使用模块
    - 可以直接导入模块
        - 假如模块名称直接以数字开头，需要借助importlib帮助
            import  importlib
             相当于导入了一个叫做01的模块并把导入模块赋值给了as，所以以后用as就行了
            as = importlib.import_module("01") 
             因为01不让用
    - 案例p01,p02
    - import 模块名 as 别名
       - 导入的同时给模块起一个别名
       - 其余用法跟第一种相同
       - 案例 p03       
    - 只导入模块中的某个类或者函数
       - from 模块名 import 函数名，类名
          - 按照上述方法可以选择性导入
          - 使用的时候可以直接使用导入的内容，不需要前缀
          - stu2 = Student(参数)
    - 导入模块中的所有东西
      - from 模块名 import *  ，相当于import 模块名。
      - 这样子前面就不用加前缀，但是用的时候可能会出现命名污染
      - stu2 = Student(参数)
    - if __name__==__main__的使用
      - 可以有效避免模块代码被导入的时候被动执行的问题
      - 建议所有代码都以该代码语句作为入口
      
      
      
  # 模块的搜索路径和存储
   - 什么是模块的搜索路径：
      - 加载模块的时候，系统会在哪些地方寻找此模块
   - 系统的默认的模块搜索路径
     - import sys
     - sys.path 该属性可以获取路径列表
     - 案例 p06.py
   - 添加搜索路径
     - sys.path.append(dir)，因为它是list类型
   - 模块的加载顺序
     - 搜索内存里面已经加载好的模块
     - 搜索python的内置莫模块
     - 搜索sys.path的路径
 
 # 包
 - 包：包是一种组织管理代码的方式，里面存放的模块
 - 用于将模块包含在一起的文件夹就是包
 - 自定义包的结构
      |---包
      |---|--- __init__.py  包的标志文件
      |---|--- 模块1
      |---|--- 模块2
      |---|--- 子包(子文件夹)
      |---|---|--- __init__.py  包的标志文件
      |---|---|--- 子包模块1
      |---|---|--- 子包模块2
   
  - 包的导入操作
   -  import 包名称
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用的方式：
             包名.函数名()
             包名.类名.函数名()
        - 此方式的访问内容是
          - 参看案例p07
          - 案例pkg01，p07.py
    - import 包名 as 别名
       - 用法跟作用方式，跟上述简单导入一致
       - 注意的是此种方法默认是对__init__.py中的内容
    
   -  import package.module
      - 导入包中的具体的一个模块
      - 使用方法
        -    package.module.func_name
        -    package.module.class.fun()
        -    package.module.class.var
              
      - 案例p08
   - import package.module as pm
   
 - from ...imprt..
   - from package import module1, module2, module3, .....
   - 此种导入方法不执行__init__的内容
      -  from pkg01 import p01
      -  p01.sayHello()
 - from package import *
     - 导入当前包 __init__.py文件中所有的函数和类
     - 使用方法
              func_name()
              class_name.func_name()
              class_name.var
     - 案例p09.py， 注意此种导入的具体内容
     
 - from package.module import *
       - 导入包中指定的模块的所有内容
       - 使用方法
            - func_name()
            - class_name.func_name()  
     
 - 在开发环境中经常会所以用其他模块，可以在当前包中直接导入其他模块中的内容
       - import 完整的包或者模块的路径 
 - __all__的用法：
     - 在使用from package import * 的时候，*可以导入放入内容
     - __init__.py中如果文件为空，或者没有__all__，那么只可以把__init__中的内容导入
     - __init__如果设置了__all__的值，那么则按照__all__指定的子包或者模块进行加载，
       - 就不会载入__init__中的内容
     - __all__=['module1', 'module2', 'package1'.........]
     - 参看案例pkg02，p10
 # 命名空间
   -用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
   - 作用是防止命名冲突
     - setName（）
     - Student.setName()
     - Dog.setName()