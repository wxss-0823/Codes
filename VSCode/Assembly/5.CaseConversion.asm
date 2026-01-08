assume cs:codesg, ds:datasg
datasg segment
              DB 'BaSiC'
              DB 'iNfOrMaTiOn'
datasg ends
codesg segment
       start: MOV  AX, datasg
              MOV  DS, AX

              MOV  BX, 0
              MOV  CX, 5
       s:     MOV  AL, [BX]
              AND  AL, 11011111B
              MOV  [BX], AL
              INC  BX
              LOOP s

              MOV  BX, 5
              MOV  CX, 11
       s0:    MOV  AL, [BX]
              OR   AL, 00100000B
              MOV  [BX], AL
              INC  BX
              LOOP s0

              MOV  AX, 4c00h
              INT  21h
codesg ends
end start