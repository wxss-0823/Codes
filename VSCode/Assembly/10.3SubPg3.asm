assume cs:code
data segment
       db 10 dup (0)
data ends

code segment
  start:    mov  ax, 12666
            mov  bx, data
            mov  ds, bx
            mov  si, 0

            call dtoc

            mov  ax, 4c00H
            int  21H

  ;功能：将 word 型数据转变为表示十进制数的字符串，字符串以 0 为结尾符
  ;参数：(ax)=word 型数据，ds:si 指向字符串首地址
  ;返回：无
  dtoc:     push ax
            push ds
            push si
            push dx
            push cx

  dtoc_core:mov  cx, 10
            mov  dx, 0
            div  cx
            add  dx, 30H
            mov  ds:[si], dl
            inc  si
            mov  cx, ax
            jcxz dtoc_out
            jmp  short dtoc_core

  dtoc_out: pop  cx
            pop  dx
            pop  si
            pop  ds
            pop  ax
code ends
end start