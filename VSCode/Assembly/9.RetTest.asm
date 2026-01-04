;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; 远转移 retf
; assume cs:codesg, ss:stacksg
; stacksg segment
;                db 16 dup(0)
; stacksg ends

; codesg segment
;               mov  ax, 4c00H
;               int  21H
;        start: mov  ax, stacksg
;               mov  ss, ax
;               mov  sp, 16
;               mov  ax, 0
;               push cs
;               push ax
;               mov  bx, 0
;               retf
; codesg ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; call，ret 配合使用
; assume cs:codesg
; codesg segment
;        start: mov  ax, 1
;               mov  cx, 3

;               call s
;               mov  bx, ax

;               mov  ax, 4c00H
;               int  21H

;        s:     add  ax, ax
;               loop s
;               ret
; codesg ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; 子程序：利用寄存器传递参数
; assume cs:codesg
; datasg segment
;               dw 1, 2, 3, 4, 5, 6, 7, 8
;               dd 0, 0, 0, 0, 0, 0, 0, 0
; datasg ends

; codesg segment
;        start: mov  ax, datasg
;               mov  ds, ax
;               mov  si, 0
;               mov  di, 16

;               mov  cx, 8
;        s:     mov  bx, [si]
;               call cube
;               mov  [di], ax
;               mov  [di].2, dx
;               add  si, 2
;               add  di, 4
;               loop s

;               mov  ax, 4c00H
;               int  21H

;        cube:  mov  ax, bx
;               mul  bx
;               mul  bx
;               ret
; codesg ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; 子程序：批量数据传递
; assume cs:code
; data segment
;             db 'conversation'
; data ends

; code segment
;        start:  mov  ax, data
;                mov  ds, ax
;                mov  si, 0
;                mov  cx, 12
;                call capital
;                mov  ax, 4c00H
;                int  21H

;        capital:and  byte ptr [si], 11011111b
;                inc  si
;                loop capital
;                ret
; code ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 子程序：用 stack 保存使用到的 reg
assume cs:code
data segment
       db 'word', 0
       db 'unix', 0
       db 'wind', 0
       db 'good', 0
data ends

code segment
  start:  mov  ax, data
          mov  ds, ax
          mov  bx, 0

          mov  cx, 4
  s:      mov  si, bx
          call capital
          add  bx, 5
          loop s

          mov  ax, 4c00H
          int  21H

  capital:push cx
          push si
               
  change: mov  cl, [si]
          mov  ch, 0
          jcxz ok

          and  byte ptr [si], 11011111b
          inc  si
          jmp  short change

  ok:     pop  si
          pop  cx
          ret
code ends
end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;