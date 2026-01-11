assume cs:code 
code SEGMENT
  start: MOV  AH, 0
         INT  16H

         MOV  AH, 1
         CMP  AL, 'R'
         JE   red
         CMP  AL, 'G'
         JE   blue
         CMP  AL, 'B'
         JE   blue
         JMP  SHORT sret

  red:   SHL  AH, 1

  green: SHL  AH, 1

  blue:  MOV  BX, 0b800H
         MOV  ES, BX
         MOV  BX, 1
         MOV  CX, 2000
  s:     AND  BYTE PTR ES:[BX], 11111000B
         OR   ES:[BX], AH
         ADD  BX, 2
         LOOP s

  sret:  MOV  AX, 4c00H
         INT  21H

code ENDS
end start