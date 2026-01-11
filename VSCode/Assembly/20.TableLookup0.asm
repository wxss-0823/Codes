assume cs:code
code SEGMENT
  start:    MOV  AL, 0acH
            CALL showbyte

            MOV  AX, 4c00H
            INT  21H

  ; 用 al 传送要显示的数据
  showbyte: JMP  SHORT show

  table     DB   '0123456789ABCDEF'

  show:     PUSH BX
            PUSH ES

            MOV  AH, AL
            SHR  AH, 1
            SHR  AH, 1
            SHR  AH, 1
            SHR  AH, 1
            AND  AL, 00001111B

            MOV  BL, AH
            MOV  BH, 0
            MOV  AH, table[BX]

            MOV  BX, 0b800H
            MOV  ES, BX
            MOV  ES:[160*12+12*2], AH
            MOV  ES:[160*12+12*2+1], 2

            MOV  BL, AL
            MOV  BH, 0
            MOV  AL, table[BX]

            MOV  BX, 0b800H
            MOV  ES, BX
            MOV  ES:[160*12+12*2+2], AL
            MOV  ES:[160*12+12*2+3], 2

            POP  ES
            POP  BX

            RET

code ENDS
end start


