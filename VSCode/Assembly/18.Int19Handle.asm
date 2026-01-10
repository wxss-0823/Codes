assume cs:code
stack SEGMENT
             DB 128 DUP(0)
stack ENDS

data SEGMENT
            DW 0, 0
data ENDS

code SEGMENT
       start:   MOV   AX, stack
                MOV   SS, AX
                MOV   SP, 128

                MOV   AX, data
                MOV   DS, AX

                MOV   AX, 0
                MOV   ES, AX

                PUSH  ES:[9*4]
                POP   DS:[0]
                PUSH  ES:[9*4+2]
                POP   DS:[2]

                MOV   WORD PTR ES:[9*4], OFFSET int9
                MOV   ES:[9*4+2], CS

                MOV   AX, 0b800H
                MOV   ES, AX
                MOV   AH, 'a'
       s:       MOV   ES:[160*12+12*2], AH
                CALL  delay
                INC   AH
                CMP   AH, 'z'
                JNA   s

                MOV   AX, 0
                MOV   ES, AX

                PUSH  DS:[0]
                POP   ES:[9*4]
                PUSH  DS:[2]
                POP   ES:[9*4+2]

                MOV   AX, 4c00H
                INT   21H

       delay:   PUSH  AX
                PUSH  DX
                MOV   DX, 0008H
                MOV   AX, 0
       s1:      SUB   AX, 1
                SBB   DX, 1
                CMP   AX, 0
                JNE   s1
                CMP   DX, 0
                JNE   s1
                POP   DX
                POP   AX
                RET

       int9:    PUSH  AX
                PUSH  BX
                PUSH  ES

                IN    AL, 60H

                PUSHF

                PUSHF
                POP   BX
                AND   BH, 11111100B
                PUSH  BX
                POPF
                CALL  DWORD PTR DS:[0]

                CMP   AL, 1
                JNE   int9ret

                MOV   AX, 0b800H
                MOV   ES, AX
                INC   BYTE PTR ES:[160*12+12*2+1]

       int9ret: POP   ES
                POP   BX
                POP   AX
                IRET

code ENDS
end start