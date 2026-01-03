assume cs:codesg, ss:stacksg
stacksg segment
          db 16 dup(0)
stacksg ends

codesg segment
         mov  ax, 4c00H
         int  21H
  start: mov  ax, stacksg
         mov  ss, ax
         mov  sp, 16
         mov  ax, 0
         push cs
         push ax
         mov  bx, 0
         retf
codesg ends
end start