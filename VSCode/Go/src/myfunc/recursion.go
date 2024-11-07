package mfg

import "fmt"

func SqrtRecursive(x, guess, preguess, epsilon float64) float64 {
	diff := guess*guess - x
	if diff < epsilon && -diff < epsilon {
		return guess
	}

	newguess := (guess + x/guess) / 2
	if newguess == guess {
		return newguess
	}

	return SqrtRecursive(x, newguess, guess, epsilon)
}

func Sqrt(x float64) {
	result := SqrtRecursive(x, 1.0, 0.0, 1e-9)
	fmt.Printf("The final guess value is %f.", result)
}
