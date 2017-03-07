package chapter01

object Curry {
  
  def partial0[A, B, C](a: A, f: (A, B) => C): B => C = 
    (b: B) => f(a, b)
   
  def curry[A,B,C](f: (A, B) => C): A => (B => C) =
    (a: A) => (b: B) => f(a, b)
  
  //def uncurry[A, B, C](f: A => B => C):(A, B) => C =
    
 
  
  def compose[A,B,C](f: B => C, g: A => B): A => C = 
    (b: A ) => f(g(b))
  

  
  def  main(args: Array[String]): Unit = {
    println("hello curry")
    var a = 12
    var x = 1
    var y = 2
    println(partial0(a: Int, (a: Int, b: Int) => (a + b): Int)(2))
    println(compose((a: Int) => ((a + 10): Int), (b: Int) => ((b - 10): Int))(1))
    val f = (x: Double) => math.Pi / 2 - x
    val cos = f compose math.sin
    println(curry((x: Int, y: Int) => x + y)(2)(1))  
  }
    package datastructures

sealed trait List[+A] 
case object Nil extends List[Nothing]
case class Cons[+A](head: A, tail: List[A]) extends List[A]

object List {
  
}
}