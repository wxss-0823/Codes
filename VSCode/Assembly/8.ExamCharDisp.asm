assume cs:codesg, ds:datasg, ss: stacksg
datasg segment
              DB 'welcome to masm!'       ; length = 16 byte
              DB 00000010B                ; background: black, font: green
              DB 00100100B                ; background: green, font: red
              DB 01110001B                ; background: white, font: blue
              DW 0
datasg ends

stacksg segment
               DW 50 DUP (0)
stacksg ends

codesg segment
       start: MOV  AX, datasg
              MOV  DS, AX
              MOV  AX, stacksg
              MOV  SS, AX
              MOV  SP, 100

              MOV  BX, 0
              MOV  CX, 3

       s:     PUSH CX
              MOV  BX, 0
              MOV  CX, 16

       s0:    MOV  DI, 15
              POP  DS:[19]
              MOV  SI, DS:[19]          ; 倒序入栈，方便出栈
              SUB  DI, BX
              MOV  DL, DS:[DI]
              MOV  DH, DS:[SI+15]
              PUSH DX
              PUSH DS:[19]              ; 存在 stack overflow 的风险，最后一个数据存入后，再次压入 cx 会导致 stack 溢出
              INC  BX
              LOOP s0

              POP  CX
              LOOP s

              MOV  AX, 0B800H
              MOV  DS, AX
              MOV  BX, 05D8H
              ; mov  bx, 0
              MOV  CX, 3

       s1:    MOV  SI, CX
              MOV  CX, 16

       s2:    POP  DS:[BX]
              ADD  BX, 2
              LOOP s2

              ADD  BX, 128
              MOV  CX, SI
              LOOP s1

              MOV  AX, 4c00H
              INT  21H

codesg ends
end start