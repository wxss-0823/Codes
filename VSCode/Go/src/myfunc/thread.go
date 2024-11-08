package mfg

import "fmt"

func Fibonacci(c, quit chan int) {
	x, y := 0, 1
	for {
		select {
		case c <- x:
			x, y = y, x+y
		case <-quit:
			fmt.Println("quit")
			return
		}
	}

}

func RunFibonacci(number int) {
	c := make(chan int, number)
	quit := make(chan int)

	go func() {
		for i := 0; i < cap(c); i++ {
			fmt.Printf("%d: %d\n", i+1, <-c)
		}
		quit <- 0
	}()

	Fibonacci(c, quit)
}
