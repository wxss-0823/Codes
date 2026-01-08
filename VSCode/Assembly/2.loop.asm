assume cs:code

code segment
          MOV  AX, 0020h
          MOV  DS, AX
          MOV  BX, 0
          MOV  CX, 64

     s:   MOV  DS:[BX], BX
          INC  BX
          LOOP s

          MOV  AX, 4c00h
          INT  21h

code ends

end