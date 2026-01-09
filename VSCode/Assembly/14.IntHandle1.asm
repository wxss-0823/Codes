assume cs:code
data segment
       DB 'conversation', 0
data ends

code segment
  start:      MOV  AX, CS
              MOV  DS, AX
              MOV  SI, OFFSET capital
              MOV  AX, 0
              MOV  ES, AX
              MOV  DI, 200H
              MOV  CX, OFFSET capitalend - OFFSET capital
              CLD
              REP  movsb

              MOV  AX, 0
              MOV  ES, AX
              MOV  word PTR ES:[7cH*4], 200H
              MOV  word PTR ES:[7cH*4+2], 0

  main:       MOV  AX, data
              MOV  DS, AX
              MOV  SI, 0
              INT  7cH

              MOV  AX, 4c00H
              INT  21H

  capital:    PUSH CX
              PUSH SI
  change:     MOV  CL, [SI]
              MOV  CH, 0
              JCXZ ok
              AND  byte PTR [SI], 11011111B
              INC  SI
              JMP  SHORT change
  ok:         POP  SI
              POP  CX
              IRET

  capitalend: NOP

code ends
end start
