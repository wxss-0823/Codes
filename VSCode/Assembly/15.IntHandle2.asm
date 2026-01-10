assume cs:code 

code SEGMENT

       start: MOV  AX, CS
              MOV  DS, AX
              MOV  SI, OFFSET lp
              MOV  AX, 0
              MOV  ES, AX
              MOV  DI, 200H
              MOV  CX, OFFSET lpend - OFFSET lp
              CLD
              REP  movsb

              MOV  AX, 0
              MOV  ES, AX
              MOV  WORD PTR ES:[7cH*4], 200H
              MOV  WORD PTR ES:[7cH*4+2], 0

       main:  MOV  AX, 0b800H
              MOV  ES, AX
              MOV  DI, 160*12+10*2
              MOV  BX, OFFSET s - OFFSET se
              MOV  CX, 15
       s:     MOV  WORD PTR ES:[DI], 0221H
              ADD  DI, 2
              INT  7cH
       se:    NOP

              MOV  AX, 4c00H
              INT  21H


       lp:    PUSH BP
              MOV  BP, SP
              DEC  CX
              JCXZ lpret
              ADD  [BP+2], BX
       lpret: POP  BP
              IRET
       lpend: NOP

code ENDS

end start




