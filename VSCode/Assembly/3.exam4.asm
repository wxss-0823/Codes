assume cs:code
code segment
          MOV  AX, CS
          MOV  DS, AX
          MOV  AX, 0020h
          MOV  ES, AX
          MOV  BX, 0
          MOV  CX, 17h

     s:   MOV  AL, [BX]
          MOV  ES:[BX], AL
          INC  BX
          LOOP s

          MOV  AX, 4c00h
          INT  21h
code ends
end