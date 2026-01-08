assume cs:codesg
codesg segment
              DW   0123h, 0456h, 0789h, 0abch, 0defh, 0fedh, 0cbah, 0987h
              DW   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
       ; 定义的 dw 数据将存储在 cs 段的开始，占用 30h 的地址空间，后面空间存储程序的机器码

       start: MOV  AX, CS
              MOV  SS, AX
              MOV  SP, 30h
       ; 指向栈顶空间，当 push 时，根据 dw 类型，sp = sp-2，压入一个 dw 数据

              MOV  BX, 0
              MOV  CX, 8
       s:     PUSH CS:[BX]
              ADD  BX, 2
              LOOP s

              MOV  BX, 0
              MOV  CX, 8
       s0:    POP  CS:[BX]
              ADD  BX, 2
              LOOP s0

              MOV  AX, 4c00h
              INT  21h

codesg ends
end start
  