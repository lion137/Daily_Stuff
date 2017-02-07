package main

import ("time"
"fmt"
"math"
)
type DisjointSet struct{
	head, tail *node
	count int }

type node struct {
	member string
	next *node
	set *DisjointSet
	
}

func (self DisjointSet) isEmpty() bool {
	return self.head == nil
}

func main() {
	var s1 DisjointSet
	
	
	fmt.Println(s1.isEmpty());
	
	}







type Employee struct {
	ID int
	name string
	address string
	DoB time.Time
	position string
	salary int
	}
/*
 
 var dilbert Employee
	dilbert.salary += 1000
	position := &dilbert.position
	*position = "Senior" */

func hypot(x, y float64) float64 {
	return math.Sqrt(x * x + y * y);
}

