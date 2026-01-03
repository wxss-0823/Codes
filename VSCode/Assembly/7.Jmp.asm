assume cs:codesg
codesg segment

         mov ax, 4c00H
         int 21H

  start: mov ax, 0
  s:     nop
         nop

         mov di, offset s
         mov si, offset s2  ; 在复制标号 S2 的指令至 S 处时，由于相对位移的关系，将不是跳转至 S1，而是跳转至程序开始 CS:[0]
         mov ax, cs:[si]
         mov cs:[di], ax

  s0:    jmp short s

  s1:    mov ax, 0
         int 21H
         mov ax, 0

  s2:    jmp short s1
         nop

codesg ends
end start
