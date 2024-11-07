package mfg

import (
	"fmt"
	"math"
)

func GoFunction() {
	a := 1.0
	getSqrt := func(num float64) float64 {
		return math.Sqrt(num + a)
	}

	getTime := func(operation func(float64) float64, num1, num2 float64) float64 {
		result := (operation(num1) * num2)
		return result
	}

	fmt.Println(getSqrt(9.1))
	fmt.Println(getTime(getSqrt, 8, 2))
}
