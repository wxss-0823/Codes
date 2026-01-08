assume cs:code
data segment
            DD 5937000
            DW 10
            DW 0
data ends

code segment
       start:     MOV  AX, data
                  MOV  DS, AX
                  MOV  AX, DS:[0]
                  MOV  DX, DS:[2]
                  MOV  CX, DS:[4]
                  CALL divdw

                  MOV  AX, 4c00H
                  INT  21H

       ;功能：进行不会产生溢出的除法运算，被除数为 dword 型，除数为 word 型，结果为 dword 型
       ;参数：(ax)=dword 型数据的低 16 位，(bx)=dword 型数据的高 16 位，(cx)=除数
       ;返回：(dx)=结果的高 16 位，(ax)=结果的低 16 位，(cx)=余数
       divdw:     PUSH AX               ; 参数寄存器保存
                  PUSH DX
                  PUSH CX

                  MOV  BP, SP
                  MOV  AX, [BP+2]       ; 取出 H16
                  MOV  DX, 0            ; 高位置 0
                  DIV  CX               ; 除数为 16 位，被除数位 dx-ax，结果 ax 为商，dx 为余数

                  MOV  [BP+2], AX       ; 写回 H16

                  MOV  AX, [BP+4]
                  DIV  CX
                  MOV  [BP+4], AX       ; 写回 L16
                  MOV  [BP], DX         ; 写回 rem
       divdw_out: POP  CX
                  POP  DX
                  POP  AX
                  RET


code ends
end start