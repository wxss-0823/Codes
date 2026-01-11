assume cs:code
stack SEGMENT
        DB 4000 DUP (0)
stack ENDS

code SEGMENT
  start:     MOV  AX, stack
             MOV  DS, AX
             MOV  SI, 0

             MOV  DL, 12
             MOV  DH, 12

             CALL getstr

             MOV  AX, 4c00H
             INT  21H

  getstr:    PUSH AX

  getstrs:   MOV  AH, 0
             INT  16H
             CMP  AL, 20H
             JB   nochar
             MOV  AH, 0
             CALL charstack
             MOV  AH, 2
             CALL charstack
             JMP  getstrs

  nochar:    CMP  AH, 0eH
             JE   backspace
             CMP  AH, 1cH
             JE   enter
             JMP  getstrs

  backspace: MOV  AH, 1
             CALL charstack
             MOV  AH, 2
             CALL charstack
             JMP  getstrs

  enter:     MOV  AL, 0                        ; NULL=0H
             MOV  AH, 0
             CALL charstack
             MOV  AH, 2
             CALL charstack
             POP  AX
             RET

  charstack: JMP  SHORT charstart

  table      DW   charpush, charpop, charshow
  top        DW   0

  charstart: PUSH BX
             PUSH DX
             PUSH DI
             PUSH ES

             CMP  AH, 2
             JA   sret
             MOV  BL, AH
             MOV  BH, 0
             ADD  BX, BX
             JMP  WORD PTR table[BX]

  charpush:  MOV  BX, top
             MOV  [SI][BX], AL
             INC  top
             JMP  sret

  charpop:   CMP  top, 0
             JE   sret
             DEC  top
             MOV  BX, top
             MOV  AL, [SI][BX]
             JMP  sret

  charshow:  MOV  BX, 0b800H
             MOV  ES, BX
             MOV  AL, 160
             MOV  AH, 0
             MUL  DH
             MOV  DI, AX
             ADD  DL, DL
             MOV  DH, 0
             ADD  DI, DX

             MOV  BX, 0

  charshows: CMP  BX, top
             JNE  noempty
             MOV  BYTE PTR ES:[DI], ' '
             JMP  sret

  noempty:   MOV  AL, [SI][BX]
             MOV  ES:[DI], AL
             MOV  BYTE PTR ES:[DI+2], ' '
             INC  BX
             ADD  DI, 2
             JMP  charshows

  sret:      POP  ES
             POP  DI
             POP  DX
             POP  BX
             RET

code ENDS
end start