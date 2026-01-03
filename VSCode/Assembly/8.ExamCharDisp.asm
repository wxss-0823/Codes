assume cs:codesg, ds:datasg, ss: stacksg
datasg segment
              db 'welcome to masm!'       ; length = 16 byte
              db 00000010B                ; background: black, font: green
              db 00100100B                ; background: green, font: red
              db 01110001B                ; background: white, font: blue
              dw 0
datasg ends

stacksg segment
               dw 50 dup (0)
stacksg ends

codesg segment
       start: mov  ax, datasg
              mov  ds, ax
              mov  ax, stacksg
              mov  ss, ax
              mov  sp, 100

              mov  bx, 0
              mov  cx, 3

       s:     push cx
              mov  bx, 0
              mov  cx, 16

       s0:    mov  di, 15
              pop  ds:[19]
              mov  si, ds:[19]          ; 倒序入栈，方便出栈
              sub  di, bx
              mov  dl, ds:[di]
              mov  dh, ds:[si+15]
              push dx
              push ds:[19]              ; 存在 stack overflow 的风险，最后一个数据存入后，再次压入 cx 会导致 stack 溢出
              inc  bx
              loop s0

              pop  cx
              loop s

              mov  ax, 0B800H
              mov  ds, ax
              mov  bx, 05D8H
              mov  cx, 3

       s1:    mov  si, cx
              mov  cx, 16

       s2:    pop  ds:[bx]
              add  bx, 2
              loop s2

              add  bx, 128
              mov  cx, si
              loop s1

              mov  ax, 4c00H
              int  21H

codesg ends
end start