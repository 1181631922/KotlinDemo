# 基本语法
kotlin的一些基本语法

### 1.函数的定义

```object BasicSyntax {
       @JvmStatic fun main(args: Array<String>) {
           println(BasicSyntax.sum(4, 5))
           BasicSyntax.printSum(5, 6)
       }

       fun sum(a: Int, b: Int): Int {
           return a + b
       }

       fun printSum(a: Int, b: Int) {
           println("$a and $b sum is ${a + b}")
       }
   }
```

:的用法可以是继承或者实现某个接口，还可以代表某个参数的类型，或者返回值，还有就是不用总写该死的分号了

### 2.定义变量

```@JvmStatic fun main(args: Array<String>) {
   //        println(BasicSyntax.sum(4, 5))
   //        BasicSyntax.printSum(5, 6)

           BasicSyntax.args()

       }

       fun args() {
           val a: Int = 1
           val b = 2
           var c: Int? = 0
           c = 3
           println("a=$a,b=$b,c=$c")
       }

```

我理解的是在kotlin中所有的都是对象，空的话是Unit

### 3.条件表达式

```@JvmStatic fun main(args: Array<String>) {
   //        println(BasicSyntax.sum(4, 5))
   //        BasicSyntax.printSum(5, 6)

   //        BasicSyntax.args()

           println(BasicSyntax.maxOf(4, 9))
       }

       fun maxOf(a: Int, b: Int): Int {
           if (a > b) {
               return a
           } else {
               return b
           }
       }
```
if的话相比之下还是一样的，但是switch区别比较大

### 4.使用可空变量以及控制检查

