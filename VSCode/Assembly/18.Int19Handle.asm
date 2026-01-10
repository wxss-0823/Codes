assume cs:code
code SEGMENT
  start: MOV AX, 0b800H
         MOV ES, AX
         MOV AH, 'a'
  s:     MOV ES:[160*12+12*2], AH
         INC AH
         CMP AH, 'z'
         JNA s

         MOV AX, 4c00H
         INT 21H

code ENDS
end start