sealed trait Tree2[+A]
case object EmptyTree extends Tree2[Nothing]
case class Node[A](value: A , left: Tree2[A], right: Tree2[A]) extends Tree2[A]]


package datastructures

//import MyListFunctions._



object notes {
		
		def maximum(x: String, y: String): String =
			if (x >= y) x
				else y            //> maximum: (x: String, y: String)String

	//tree:
	
	 def length[A](tree: Tree[A]): Int =
      tree match {
      case Leaf(x) => 1
      case Branch(left, right) => length(left) + 1 + length(right)
      
    }                                             //> length: [A](tree: datastructures.Tree[A])Int
    
  def maxDepth[A](tree: Tree[A]): Int =
  		tree match {
  			case Leaf(x) => 1
  			case Branch(left, right) =>
  				var ldepth: Int = maxDepth(left)
  				var rdepth: Int = maxDepth(right)
  				if (ldepth > rdepth) ldepth + 1
  					else
  						rdepth + 1
  		}                                 //> maxDepth: [A](tree: datastructures.Tree[A])Int
  		
  
  def treeMax(tree: Tree[String]): String = {
  	var maxi = ""
  	tree match {
  		case Leaf(x) =>
  			maxi = maximum(x, maxi)
  			maxi
  		case Branch(left, right) =>
  		var lmax = treeMax(left)
  		var rmax = treeMax(right)
  		if (lmax > rmax) lmax
  			else rmax
  	}
  }                                               //> treeMax: (tree: datastructures.Tree[String])String
  
 
	// end of a tree
	
	//tree2 functions:
	
	def tree2Map[A, B](tree: Tree2[A])(f: A => B): Tree2[B] =
		tree match {
			case EmptyTree => EmptyTree
			case Node(x, left, right) => Node(f(x), tree2Map(left)(f), tree2Map(right)(f))
		}                               
	
	def length2[A](tree: Tree2[A]): Int =
	 tree match {
	 	case EmptyTree => 0
	 	case Node(x, left, right) => length2(left) + 1 + length2(right)
	 }                                    
	 
	 def maxDepth2[A](tree: Tree2[A]): Int =
	   tree match {
	   	case EmptyTree => 0
	   	case Node(x, left, right) =>
	   		var lmax = maxDepth2(left)
	   		var rmax = maxDepth2(right)
	   		if (lmax > rmax) lmax + 1
	   		 else rmax + 1
	   }                                      
	  
	  def loadTree[A](tree: Tree2[A]): A =
	  	tree match {
	  		case EmptyTree => throw new Exception("value of empty tree")
	  		case Node(x, left, right) => x
	  	}                            
	  
	  def leftBranch[T](tree: Tree2[T]): Tree2[T] =
	   tree match {
	   	case EmptyTree => throw new Exception("left branch of empty tree")
	   	case Node(x, left, right) => left
	   	}                                
	   
	   def rightBranch[T](tree: Tree2[T]): Tree2[T] =
	   tree match {
	   	case EmptyTree => throw new Exception("left branch of empty tree")
	   	case Node(x, left, right) => right
	   	}                              
	  
	  def isTreeEmpty[T](tree: Tree2[T]): Boolean =
	  	tree match {
	  		case EmptyTree => true
	  		case Node(x, left, right) => false
	  	}                               
	 
	 
	 def addToTree(elem: Int, tree: Tree2[Int]): Tree2[Int] = {
	 	
	 		if (isTreeEmpty(tree)) Node(elem, EmptyTree, EmptyTree)
	 		else if (elem == loadTree(tree)) tree
	 		else if (elem < loadTree(tree)) Node(loadTree(tree), addToTree(elem, leftBranch(tree)), rightBranch(tree))
	 		else Node(loadTree(tree), leftBranch(tree), addToTree(elem, rightBranch(tree)))
	 	
	 	}                                
	 	
	//end of tree2 functions
	def myTail[A](x: MyList[A]): MyList[A] = x match {
		case  Nil => Nil
		case  Cons(y, ys) => ys
			}                         //> myTail: [A](x: datastructures.MyList[A])datastructures.MyList[A]
	
	def myHead[A](x: MyList[A]): A = x match {
		case Nil => throw new Exception("head of empty list")
		case Cons(y, ys) => y
	}                                         //> myHead: [A](x: datastructures.MyList[A])A
	
	def setHead[T](x: MyList[T], elem: T): MyList[T] = x match {
		case Nil => Nil
		case Cons(y, ys) => Cons(elem, ys)
		}                                 //> setHead: [T](x: datastructures.MyList[T], elem: T)datastructures.MyList[T]
	
	def myDrop[A](x: MyList[A], n:Int): MyList[A] = {
		if (n == 0) x
			else
			myDrop(myTail(x), n - 1)
	}                                         //> myDrop: [A](x: datastructures.MyList[A], n: Int)datastructures.MyList[A]
	
	def myDropWhile[T](x: MyList[T], f: T => Boolean): MyList[T] = {
			if (!(f(myHead(x)))) x
			else
				myDropWhile(myTail(x), f)
		}                                 //> myDropWhile: [T](x: datastructures.MyList[T], f: T => Boolean)datastructure
                                                  //| s.MyList[T]
  def dropWhile[A](x: MyList[A])(f: A => Boolean): MyList[A] =
  	x match {
  	case Cons(h, t) if  f(h) => dropWhile(t)(f)
  	case _ => x
  	}                                         //> dropWhile: [A](x: datastructures.MyList[A])(f: A => Boolean)datastructures.
                                                  //| MyList[A]
  
  def dropWhile2[A](x: List[A])(f: A => Boolean): List[A] =
  	x match {
  	case h :: t if  f(h) => dropWhile2(t)(f)
  	case _ => x
  	}                                         //> dropWhile2: [A](x: List[A])(f: A => Boolean)List[A]
  
  def myFoldlRight[A, B](x: MyList[A], z: B)(f: (A, B) => B): B =
  x match {
  	case Nil => z
  	case Cons(y, ys) => f(y, myFoldlRight(ys, z)(f))
  }                                               //> myFoldlRight: [A, B](x: datastructures.MyList[A], z: B)(f: (A, B) => B)B
  
  def myFoldLeft[T, U](as: MyList[T], acc: U)(f: (T, U) => U): U =

  		 as match {
  		 	case Nil => acc
  		 	case Cons(y, ys) => myFoldLeft(ys, f(y, acc))(f)
  
  }                                               //> myFoldLeft: [T, U](as: datastructures.MyList[T], acc: U)(f: (T, U) => U)U
  
  def foldRight[T, U](as: MyList[T], acc: U)(f: (T, U) => U): U =
  	myFoldLeft(as, acc)(f)                    //> foldRight: [T, U](as: datastructures.MyList[T], acc: U)(f: (T, U) => U)U
  
  def myMap[A,B](as: MyList[A])(f: A => B): MyList[B] =
  as match {
  	case Nil => Nil
  	case Cons(x, xs) => Cons(f(x), myMap(xs)(f))
  }                                               //> myMap: [A, B](as: datastructures.MyList[A])(f: A => B)datastructures.MyList
                                                  //| [B]
  def square(xs: MyList[Int]): MyList[Int] =
  	myMap(xs)(x => x * x)                     //> square: (xs: datastructures.MyList[Int])datastructures.MyList[Int]
  	
  def myFlatMap[A, B](as: List[A])(f: A => List[B]): List[B] =
  	as match {
  		case List() => List()
  		case x :: xs => f(x) ++ myFlatMap(xs)(f)
  	}                                         //> myFlatMap: [A, B](as: List[A])(f: A => List[B])List[B]
  
 	def myFilter[A](as: List[A])(f: A => Boolean): List[A] =
 		as match {
 			case List() => List()
 			case x :: xs => if (f(x)) myFilter(xs)(f) else x :: myFilter(xs)(f)
 		}                                 //> myFilter: [A](as: List[A])(f: A => Boolean)List[A]
  
  
  
  
   def myLength[A](xs: MyList[A]): Int =
     xs match {
      case Nil => 0
      case Cons(y, ys) => 1 + myLength(ys)
   }                                              //> myLength: [A](xs: datastructures.MyList[A])Int
	
  println("Welcome to the Scala worksheet")       //> Welcome to the Scala worksheet
  val l: MyList[Int] = Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, Nil)))))
                                                  //> l  : datastructures.MyList[Int] = Cons(1,Cons(2,Cons(3,Cons(4,Cons(5,Nil)))
                                                  //| ))
  val xs = List(1, 2, 3)                          //> xs  : List[Int] = List(1, 2, 3)
  setHead(l, 11)                                  //> res0: datastructures.MyList[Int] = Cons(11,Cons(2,Cons(3,Cons(4,Cons(5,Nil)
                                                  //| ))))
  dropWhile(l)(s => s < 4)                        //> res1: datastructures.MyList[Int] = Cons(4,Cons(5,Nil))
  myFoldlRight (l, 1) (_ * _)                     //> res2: Int = 120
  myFoldlRight(l, Nil: MyList[Int]) (Cons(_,_))   //> res3: datastructures.MyList[Int] = Cons(1,Cons(2,Cons(3,Cons(4,Cons(5,Nil))
                                                  //| )))
  myFoldLeft(l ,0) (_ + _)                        //> res4: Int = 15
  foldRight(l, 0) (_ + _)                         //> res5: Int = 15
  square(l)                                       //> res6: datastructures.MyList[Int] = Cons(1,Cons(4,Cons(9,Cons(16,Cons(25,Nil
                                                  //| )))))
  ((x: Int) => List(x, x))(1)                     //> res7: List[Int] = List(1, 1)
  
 List(1, 2) ++ List(3, 4)                         //> res8: List[Int] = List(1, 2, 3, 4)
 
 myFlatMap(List(1, 2, 3))(x => List(x, x, x))     //> res9: List[Int] = List(1, 1, 1, 2, 2, 2, 3, 3, 3)
 
 myFilter(List(1, 2, 3, 4))((x: Int) => x < 4)    //> res10: List[Int] = List(4)
 
 
 val tree = Branch(Leaf("DD"), Branch(Leaf(""), Branch(Leaf(" "), Leaf(""))))
                                                  //> tree  : datastructures.Branch[String] = Branch(Leaf(DD),Branch(Leaf(),Branc
                                                  //| h(Leaf( ),Leaf())))
 val tree1 = Branch(Leaf(1), Leaf(1))             //> tree1  : datastructures.Branch[Int] = Branch(Leaf(1),Leaf(1))
 
 length(tree)                                     //> res11: Int = 7
 length(tree1)                                    //> res12: Int = 3
 maxDepth(tree)                                   //> res13: Int = 4
 treeMax(tree)                                    //> res14: String = DD
 
 val tree20 = Node(10, Node(5, EmptyTree, EmptyTree), Node(15, EmptyTree, EmptyTree))
                                                  //> tree20  : datastructures.Node[Int] = Node(10,Node(5,EmptyTree,EmptyTree),No
                                                  //| de(15,EmptyTree,EmptyTree))
 
 tree2Map(tree20)((x: Int) => 3 * x)              //> res15: datastructures.Tree2[Int] = Node(30,Node(15,EmptyTree,EmptyTree),Nod
                                                  //| e(45,EmptyTree,EmptyTree))
 length2(tree20)                                  //> res16: Int = 3
 
 maxDepth2(tree20)                                //> res17: Int = 2
 addToTree(2, tree20)                             //> res18: datastructures.Tree2[Int] = Node(10,Node(5,Node(2,EmptyTree,EmptyTre
                                                  //| e),EmptyTree),Node(15,EmptyTree,EmptyTree))
 
  
  
  
  
  
  
}
