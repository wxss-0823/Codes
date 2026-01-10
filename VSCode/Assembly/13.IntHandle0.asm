assume cs:code
code SEGMENT
       start: MOV  AX, CS
              MOV  DS, AX
              MOV  SI, OFFSET sqr
              MOV  AX, 0
              MOV  ES, AX
              MOV  DI, 200H
              MOV  CX, OFFSET sqrend - OFFSET sqr
              CLD
              REP  movsb

              MOV  AX, 0
              MOV  ES, AX
              MOV  WORD PTR ES:[7ch*4], 200H
              MOV  WORD PTR ES:[7ch*4+2], 0

              MOV  AX, 3456
              INT  7cH
              ADD  AX, AX
              ADC  DX, DX
              MOV  AX, 4c00H
              INT  21H

       sqr:   MUL  AX
              IRET
       sqrend:NOP

code ENDS
end start