assume cs:code
code SEGMENT
  start: MOV AL, 4
         OUT 70H, AL
         IN  AL, 71H

         MOV AH, AL
         MOV CL, 4
         SHR AH, CL
         AND AL, 00001111b

         ADD AH, 30H
         ADD AL, 30H

         MOV BX, 0b800H
         MOV ES, BX
         MOV BX, 160*12+20*2
         MOV BYTE PTR ES:[BX], AH
         MOV BYTE PTR ES:[BX+2], AL

         MOV AX, 4c00H
         INT 21H

code ENDS
end start