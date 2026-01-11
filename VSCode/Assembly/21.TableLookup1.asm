assume cs:code
code SEGMENT
  start:   MOV  AX, 120
           CALL showsin

           MOV  AX, 4c00H
           INT  21H

  showsin: JMP  SHORT show
  table    DW   ag0, ag30, ag60, ag90, ag120, ag150, ag180
  ag0      DB   '0', 0
  ag30     DB   '0.5', 0
  ag60     DB   '0.866', 0
  ag90     DB   '1', 0
  ag120    DB   '0.866', 0
  ag150    DB   '0.5', 0
  ag180    DB   '0', 0
  show:    PUSH BX
           PUSH ES
           PUSH SI
           MOV  BX, 0b800H
           MOV  ES, BX

           MOV  AH, 0
           MOV  BL, 30
           DIV  BL
           MOV  BL, AL
           MOV  BH, 0
           ADD  BX, BX
           MOV  BX, table[BX]

           MOV  SI, 160*12+12*2
  shows:   MOV  AH, CS:[BX]
           CMP  AH, 0
           JE   showret
           MOV  ES:[SI], AH
           MOV  ES:[SI+1], 2
           INC  BX
           ADD  SI, 2
           JMP  SHORT shows

  showret: POP  SI
           POP  ES
           POP  BX
           RET

code ENDS
end start