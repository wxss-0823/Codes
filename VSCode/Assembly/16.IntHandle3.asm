assume cs:code
data SEGMENT
            DB 'Welcome to masm!', '$'
data ENDS

code SEGMENT
       start: MOV AH, 2           ; 置光标子程序
              MOV BH, 0           ; 第 0 页
              MOV DH, 8           ; dh 中放行号
              MOV DL, 12          ; dl 中放列号
              INT 10H

              MOV AX, data
              MOV DS, AX
              MOV DX, 0
              MOV AH, 9
              INT 21H

              MOV AX, 4c00H
              INT 21H
code ENDS
end start