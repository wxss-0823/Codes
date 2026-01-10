assume cs:code
data SEGMENT
            DB 10 DUP (0)
data ENDS

code SEGMENT
       start:     MOV  AX, 12666
                  MOV  BX, data
                  MOV  DS, BX
                  MOV  SI, 0

                  CALL dtoc

                  MOV  AX, 4c00H
                  INT  21H

       ;功能：将 word 型数据转变为表示十进制数的字符串，字符串以 0 为结尾符
       ;参数：(ax)=word 型数据，ds:si 指向字符串首地址
       ;返回：无
       dtoc:      PUSH AX
                  PUSH DS
                  PUSH SI
                  PUSH DX
                  PUSH CX

       dtoc_core: MOV  CX, 10
                  MOV  DX, 0
                  DIV  CX
                  ADD  DX, 30H
                  MOV  DS:[SI], DL
                  INC  SI
                  MOV  CX, AX
                  JCXZ dtoc_out
                  JMP  SHORT dtoc_core

       dtoc_out:  POP  CX
                  POP  DX
                  POP  SI
                  POP  DS
                  POP  AX
                  RET
code ENDS
end start