assume cs:code

stack SEGMENT
        DB 128 DUP (0)
stack ENDS

code SEGMENT
  start:   MOV   AX, stack
           MOV   SS, AX
           MOV   SP, 128

           PUSH  CS
           POP   DS

           MOV   AX, 0
           MOV   ES, AX

           MOV   SI, OFFSET int9
           MOV   DI, 204H
           MOV   CX, OFFSET int9end - OFFSET int9
           CLD
           REP   movsb

           PUSH  ES:[9*4]
           POP   ES:[200H]
           PUSH  ES:[9*4+2]
           POP   ES:[202H]

           CLI
           MOV   WORD PTR ES:[9*4], 204H
           MOV   WORD PTR ES:[9*4+2], 0
           STI

           MOV   AX, 4c00H
           INT   21H

  int9:    PUSH  AX
           PUSH  BX
           PUSH  CX
           PUSH  ES

           IN    AL, 60H

           PUSHF
           CALL  DWORD PTR CS:[200H]

           CMP   AL, 3bH
           JNE   int9ret

           MOV   AX, 0b800H
           MOV   ES, AX
           MOV   BX, 1
           MOV   CX, 2000
  s:       INC   BYTE PTR ES:[BX]
           ADD   BX, 2
           LOOP  s

  int9ret: POP   ES
           POP   CX
           POP   BX
           POP   AX
           IRET

  int9end: NOP

code ENDS
end start