;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 双变量寻址方式
; assume cs:codesg
; codesg segment
;   start: mov ax, 2000H
;          mov ds, ax
;          mov bx, 1000H
;          mov si, 0
;          mov ax, [bx+2+si]
;          inc si
;          mov cx, [bx+2+si]
;          inc si
;          mov di, si
;          mov bx, [bx+2+di]
; codesg ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; 每个单词的头一个字母改为大写
; assume cs:codesg, ds:datasg
; datasg segment
;          db '1. file         '
;          db '2. edit         '
;          db '3. search       '
;          db '4. view         '
;          db '5. options      '
;          db '6. help         '
; datasg ends

; codesg segment
;   start: mov  ax, datasg
;          mov  ds, ax
;          mov  bx, 0

;          mov  cx, 6
;   s:     mov  al, [bx+3]
;          and  al, 11011111b
;          mov  [bx+3], al
;          add  bx, 16
;          loop s
; codesg ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; 每个单词改为大写字母，使用 stack 暂存数据
; assume cs:codesg, ds:datasg, ss:stacksg
; datasg segment
;          db 'ibm             '
;          db 'dec             '
;          db 'dos             '
;          db 'vax             '
; datasg ends

; stacksg segment
;           dw 0, 0, 0, 0, 0, 0, 0, 0
; stacksg ends

; codesg segment
;   start: mov  ax, stacksg
;          mov  ss, ax
;          mov  sp, 16
;          mov  ax, datasg
;          mov  ds, ax

;          mov  bx, 0
;          mov  cx, 4
;   s0:    push cx
;          mov  si, 0
;          mov  cx, 3
;   s:     mov  al, [bx+si]
;          and  al, 11011111b
;          mov  [bx+si], al
;          inc  si
;          loop s

;          add  bx, 16
;          pop  cx
;          loop s0

;          mov  ax, 4c00H
;          int  21H
; codesg ends

; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; ; div 示例
; assume cs:codesg
; codesg segment
;   start: mov dx, 1
;          mov ax, 86A1H

;          mov bx, 100
;          div bx
         
;          mov ax, 4c00H
;          int 21H
; codesg ends
; end start
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
