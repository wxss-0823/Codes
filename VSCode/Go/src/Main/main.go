package main

import (
	"fmt"
	"mfg"
)

func main() {
	// mfg.GoFunction()
	// mfg.Sqrt(14.0)
	length, err := mfg.RunStringWriter("This is a interface example!")
	fmt.Println(length, err)
}
