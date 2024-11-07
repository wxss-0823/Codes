package mfg

import "fmt"

type Writer interface {
	Write(string) (int, error)
}

type StringWriter struct {
	str string
}

// 必须指定为指针结构体，结果才会影响属性
func (sw *StringWriter) Write(data string) (int, error) {
	sw.str = data
	return len(data), nil
}

func RunStringWriter(txt string) (int, error) {
	var w Writer = new(StringWriter)
	sw := w.(*StringWriter)
	// sw.str = "Hello World!"
	length, er := sw.Write(txt)
	fmt.Println(sw.str)
	return length, er
}
