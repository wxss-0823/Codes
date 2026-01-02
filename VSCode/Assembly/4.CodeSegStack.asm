assume cs:codesg
codesg segment
              dw   0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h
              dw   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
       ; 定义的 dw 数据将存储在 cs 段的开始，占用 30h 的地址空间，后面空间存储程序的机器码

       start: mov  ax, cs
              mov  ss, ax
              mov  sp, 30h
       ; 指向栈顶空间，当 push 时，根据 dw 类型，sp = sp-2，压入一个 dw 数据

              mov  bx, 0
              mov  cx, 8
       s:     push cs:[bx]
              add  bx, 2
              loop s

              mov  bx, 0
              mov  cx, 8
       s0:    pop  cs:[bx]
              add  bx, 2
              loop s0

              mov  ax, 4c00h
              int  21h

codesg ends
end start
  