assume cs:code 
code SEGMENT
  start: MOV AX, 0b800H
         MOV ES, AX
         MOV BX, 0

         MOV AL, 1
         MOV CH, 0
         MOV CL, 1
         MOV DL, 0
         MOV DH, 0
         MOV AH, 2
         INT 13H

         MOV CX, 1
         MOV SI, 0
         MOV BL, 10

         ADD AL, 30H
         MOV ES:[SI], AL

         ADD AH, 30H        ; 返回错误码 01H：非法命令，可能电脑无软盘吧
         MOV ES:[SI+2], AH

         MOV AX, 4c00H
         INT 21H

code ENDS
end start