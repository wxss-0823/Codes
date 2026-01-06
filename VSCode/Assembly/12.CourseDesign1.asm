assume cs:code
data segment
       db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
       db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
       db '1993','1994','1995'
  ;以上是表示 21 年的 21 个字符串
       dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
       dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5937000
  ;以上是表示 21 年公司总收入的 21 个 dword 型数据
       dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
       dw 11542,14430,15257,17800
  ;以上是表示 21 年公司雇员人数的 21 个 word 型数据
data ends

table segment
        db 21 dup ('xxxx     xxxxxxx   xxxxx    xxx ')  ; 21*32byte
table ends

buff segment
       db 16 dup(0)
buff ends

code segment
  start:mov  ax, data       ; 段地址定位
        mov  ds, ax
        mov  ax, table
        mov  es, ax

        mov  si, 0
        mov  di, 84
        mov  bp, 168
        mov  bx, 0
        mov  cx, 21
        
  main: push cx             ; 计算当前行数对应的内存 offset
        mov  ax, 21
        sub  ax, cx
        mov  cx, ax
        mov  ax, 32
        mul  cl
        mov  bx, ax         ; 计算结果存入 bx

        mov  ax, ds:[si]    ; 每一个年份 4byte 存入 table
        mov  es:[bx], ax
        add  si, 2
        mov  ax, ds:[si]
        mov  es:[bx+2], ax
        add  si, 2

        mov  ax, ds:[di]    ; 每一个收入 7byte 存入 table
        mov  dx, ds:[di+2]
        call dtoc


code ends
end start