assume cs:code
data segment
       db 'abcd'
data ends

table segment
        db 4 dup(0)

table ends

code segment
  start:mov ax, data
        mov ds, ax
        mov ax, table
        mov es, ax
        mov al, ds:[0]
        mov es:[0], al

        mov ax, 4c00H
        int 21H
code ends
end start