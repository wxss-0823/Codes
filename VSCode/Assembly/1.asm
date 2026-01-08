assume cs:codescg

codescg segment
          MOV AX, 0123h
          MOV BX, 0456h
          ADD AX, AX
          MOV AX, 4c00h
          INT 21h

codescg ends

end