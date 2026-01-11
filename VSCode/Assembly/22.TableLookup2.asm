assume cs:code
code SEGMENT
  start:     MOV  AH, 3
             MOV  AL, 0
             CALL setscreen

             MOV  AX, 4c00H
             INT  21H

  setscreen: JMP  SHORT set
  table      DW   sub1, sub2, sub3, sub4
  set:       PUSH BX

             CMP  AH, 3
             JA   sret
             MOV  BL, AH
             MOV  BH, 0
             ADD  BX, BX

             CALL WORD PTR table[BX]

  sret:      POP  BX
             RET

  sub1:      PUSH BX
             PUSH CX
             PUSH ES
             MOV  BX, 0b800H
             MOV  ES, BX

             MOV  BX, 0
             MOV  CX, 2000
  sub1s:     MOV  BYTE PTR ES:[BX], ' '
             ADD  BX, 2
             LOOP sub1s

             POP  ES
             POP  CX
             POP  BX
             RET

  sub2:      PUSH BX
             PUSH CX
             PUSH ES

             MOV  BX, 0b800H
             MOV  ES, BX
             MOV  BX, 1
             MOV  CX, 2000
  sub2s:     AND  BYTE PTR ES:[BX], 11111000B
             OR   ES:[BX], AL
             ADD  BX, 2
             LOOP sub2s

             POP  ES
             POP  CX
             POP  BX
             RET

  sub3:      PUSH BX
             PUSH CX
             PUSH ES
             MOV  CL, 4
             SHL  AL, CL
             MOV  BX, 0b800H
             MOV  ES, BX

             MOV  BX, 1
             MOV  CX, 2000
  sub3s:     AND  BYTE PTR ES:[BX], 10001111B
             OR   ES:[BX], AL
             ADD  BX, 2
             LOOP sub3s

             POP  ES
             POP  CX
             POP  BX
             RET

  sub4:      PUSH CX
             PUSH SI
             PUSH DI
             PUSH ES
             PUSH DS

             MOV  SI, 0b800H
             MOV  ES, SI
             MOV  DS, SI
             MOV  SI, 160
             MOV  DI, 0
             CLD
             MOV  CX, 24

  sub4s:     PUSH CX
             MOV  CX, 160
             REP  movsb
             POP  CX
             LOOP sub4s

             MOV  CX, 80
             MOV  SI, 0
  sub4s1:    MOV  BYTE PTR [160*24+SI], ' '
             ADD  SI, 2
             LOOP sub4s1

             POP  DS
             POP  ES
             POP  DI
             POP  SI
             POP  CX
             RET

code ENDS
end start