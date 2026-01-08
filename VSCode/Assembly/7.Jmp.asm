assume cs:codesg
codesg segment

              MOV AX, 4c00H
              INT 21H

       start: MOV AX, 0
       s:     NOP
              NOP

              MOV DI, OFFSET s
              MOV SI, OFFSET s2       ; 在复制标号 S2 的指令至 S 处时，由于相对位移的关系，将不是跳转至 S1，而是跳转至程序开始 CS:[0]
              MOV AX, CS:[SI]
              MOV CS:[DI], AX

       s0:    JMP SHORT s

       s1:    MOV AX, 0
              INT 21H
              MOV AX, 0

       s2:    JMP SHORT s1
              NOP

codesg ends
end start
