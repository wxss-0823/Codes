assume cs:code
data segment
       dd 5937000
       dw 10
       dw 0
data ends

code segment
  start:    mov  ax, data
            mov  ds, ax
            mov  ax, ds:[0]
            mov  dx, ds:[2]
            mov  cx, ds:[4]
            call divdw

            mov  ax, 4c00H
            int  21H

  ;功能：进行不会产生溢出的除法运算，被除数为 dword 型，除数为 word 型，结果为 dword 型
  ;参数：(ax)=dword 型数据的低 16 位，(bx)=dword 型数据的高 16 位，(cx)=除数
  ;返回：(dx)=结果的高 16 位，(ax)=结果的低 16 位，(cx)=余数
  divdw:    push ax          ; 参数寄存器保存
            push dx
            push cx

            mov  bp, sp
            mov  ax, [bp+2]  ; 取出 H16
            mov  dx, 0       ; 高位置 0
            div  cx          ; 除数为 16 位，被除数位 dx-ax，结果 ax 为商，dx 为余数

            mov  [bp+2], ax  ; 写回 H16

            mov  ax, [bp+4]
            div  cx
            mov  [bp+4], ax  ; 写回 L16
            mov  [bp], dx    ; 写回 rem
  divdw_out:pop  cx
            pop  dx
            pop  ax
            ret


code ends
end start