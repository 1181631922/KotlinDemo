package com.fanyafeng.kotlindemo.javatest

/**
 * Author： fanyafeng
 * Data： 17/5/24 上午10:47
 * Email: fanyafeng@live.cn
 */
object BasicSyntax {
    @JvmStatic fun main(args: Array<String>) {
//        println(BasicSyntax.sum(4, 5))
//        BasicSyntax.printSum(5, 6)

//        BasicSyntax.args()

//        println(BasicSyntax.maxOf(4, 9))

        println(BasicSyntax.paraseInt("4"))
    }

    fun paraseInt(str: String): Int? {
        return str.toIntOrNull()
    }

    fun maxOf(a: Int, b: Int): Int {
        if (a > b) {
            return a
        } else {
            return b
        }
    }

    fun args() {
        val a: Int = 1
        val b = 2
        var c: Int? = 0
        c = 3
        println("a=$a,b=$b,c=$c")
    }


    fun sum(a: Int, b: Int): Int {
        return a + b
    }

    fun printSum(a: Int, b: Int) {
        println("$a and $b sum is ${a + b}")
    }
}
