assume cs:code
data segment
            db '1975','1976','1977','1978','1979','1980','1981','1982','1983'
            db '1984','1985','1986','1987','1988','1989','1990','1991','1992'
            db '1993','1994','1995'

            dd 16,22,382,1356,2390,8000,16000,24486,50065,97479,140417,197514
            dd 345980,590827,803530,1183000,1843000,2759000,3753000,4649000,5937000
       
            dw 3,7,9,13,28,38,130,220,476,778,1001,1442,2258,2793,4037,5635,8226
            dw 11542,14430,15257,17800
data ends

table segment
       ; db 21 dup ('xxxx     xxxxxxx   xxxxx    xxx ')  ; 21*32byte
             db 672 dup(20H)
table ends

buff segment
            db 7 dup(0)
buff ends

code segment
       start:       mov  ax, data               ; 段地址定位
                    mov  ds, ax
                    mov  ax, table
                    mov  es, ax

                    mov  si, 0                  ;寄存器初始化
                    mov  bx, 0
                    mov  cx, 21
        
       year:        mov  ax, ds:[si]            ; 每一个年份 4byte 存入 table
                    mov  es:[bx], ax
                    mov  ax, ds:[si+2]
                    mov  es:[bx+2], ax
                    add  si, 4
                    add  bx, 32
                    loop year


                    mov  cx, 21
                    mov  bx, 054H

       income:      mov  ax, ds:[bx]
                    mov  dx, ds:[bx+2]

                    push bx
                    mov  bx, 9

                    call dtoc

                    pop  bx
                    add  bx, 4
  
                    loop income

                    mov  cx, 21
                    mov  bx, 0A8H

       num:         mov  ax, ds:[bx]
                    mov  dx, 0
     
                    push bx
                    mov  bx, 19

                    call dtoc

                    pop  bx
                    add  bx, 2
  
                    loop num


                    mov  cx, 21
                    mov  si, 0
                    mov  di, 0
                    mov  dx, 0

       avgIncome:   mov  ax, ds:[si+054H]       ; L16
                    mov  dx, ds:[si+056H]       ; H16

                    push cx

                    mov  cx, ds:[di+0A8H]

                    call divdw                  ; dx=H16, ax=L16, cx=rem
                    pop  cx                     ; 一定要提前 pop，dtoc 需要 cx 作为参数
               
                    push bx
                    mov  bx, 28                 ; 初始化固定偏移量
               
                    call dtoc                   ; 将平均收入转化为字符

                    add  si, 4
                    add  di, 2
                    pop  bx

                    loop avgIncome

       print2screen:mov  dh, 2                  ; 显示 table 中保存的字符
                    mov  dl, 25
                    mov  cl, 2
                    mov  ch, 0
                    mov  ax, table
                    mov  ds, ax
                    call show_str

                    mov  ax, 4c00H
                    int  21H

       ;功能：将 double word 型数据转变为表示十进制数的字符串
       ;参数：(dx)=H16，(ax)=L16，(cx)=当前行数，(bx)=固定偏移量
       ;返回：无
       dtoc:        push ax
                    push ds
                    push si
                    push dx
                    push cx
                    push es
                    push di
                    push bx

                    mov  si, 21                 ; cx 存放当前循环次数，计算当前循环次数对应的 table 偏置
                    sub  si, cx
                    mov  cx, si

       dtoc_offset: add  bx, 32
                    loop dtoc_offset

                    mov  cx, buff
                    mov  es, cx
                    mov  si, 0

       dtoc_core:   mov  cx, 10
                    call divdw                  ; 结果：dx=H16, ax=L16, cx=rem
                    add  cx, 30H
                    mov  es:[si], cx            ; 计算最后一位的 ASCII 码，并放入 buff
                    inc  si
                    mov  cx, ax
                    or   cx, dx                 ; 判断商的每一位是否为 0
                    jcxz dtoc_tmp
                    jmp  short dtoc_core

       dtoc_tmp:    mov  cx, si                 ; cx=si+1，初始化循环参数
                    dec  si
                    mov  di, 0

       dtoc_write:  mov  ax, table              ; 商为 0 时，反向读取 ASCII 码，并放入 table
                    mov  ds, ax
                    mov  al, es:[si]
                    mov  ds:[bx+di], al         ; 缺少一个表示行数的变量
                    inc  di
                    dec  si
                    loop dtoc_write
  
       dtoc_out:    pop  bx
                    pop  di
                    pop  es                     ; 退出子程序
                    pop  cx
                    pop  dx
                    pop  si
                    pop  ds
                    pop  ax
                    ret

       ;功能：进行不会产生溢出的除法运算，被除数为 dword 型，除数为 word 型，结果为 dword 型
       ;参数：(ax)=dword 型数据的低 16 位，(dx)=dword 型数据的高 16 位，(cx)=除数
       ;返回：(dx)=结果的高 16 位，(ax)=结果的低 16 位，(cx)=余数
       divdw:       push ax                     ; 参数寄存器保存
                    push dx
                    push cx

                    mov  bp, sp
                    mov  ax, [bp+2]             ; 取出 H16
                    mov  dx, 0                  ; 高位置 0
                    div  cx                     ; 除数为 16 位，被除数位 dx-ax，结果 ax 为商，dx 为余数

                    mov  [bp+2], ax             ; 写回 H16

                    mov  ax, [bp+4]
                    div  cx
                    mov  [bp+4], ax             ; 写回 L16
                    mov  [bp], dx               ; 写回 rem
       divdw_out:   pop  cx
                    pop  dx
                    pop  ax
                    ret
        
       ;功能：在指定的位置，用指定的颜色，显示一个用 0 结束的字符串
       ;参数：(dh)=行号(取值范围 0~24)，(dl)=列号(取值范围 0~79)，(cl)=颜色，ds:si 指向字符串的首地址
       ;返回：void
       show_str:    push dx                     ; 参数寄存器保存
                    push cx

                    push si                     ; 子程序使用到的寄存器保存
                    push ax
                    push bx
  
                    mov  al, 00A0H              ; 计算字符串显示起始位置
                    mov  ah, 0
                    mul  dh                     ; 计算行偏置，每行 A0 个字符
                    mov  bx, ax
                    mov  al, 2                  ; 计算列偏置，每列字符=列数*2
                    mov  ah, 0
                    mul  dl
                    add  bx, ax                 ; 计算结果：显存不允许从奇数地址存入数据
                    mov  si, 0
                    mov  dx, cx
                    mov  cx, 21
                    push cx
                    mov  cx, 16
                    jmp  short disp

       row_offset:  push cx
                    add  bx, 0060H

                    mov  cx, 16

       disp:        push ds                     ; 字符串 ds 段地址保存
                    push ds:[si]                ; push 两个字节的字符入栈
           
                    mov  ax, 0B800H             ; 显存 ds 段地址
                    mov  ds, ax
                    pop  ax                     ; pop 两个字节的字符出栈

                    mov  ds:[bx], al            ; 第一个字符放入显存
                    mov  ds:[bx].1, dl          ; 颜色配置放入显存
                    mov  ds:[bx].2, ah          ; 第二个字符放入显存
                    mov  ds:[bx].3, dl          ; 颜色配置放入显存

                    add  si, 2
                    add  bx, 4
                    pop  ds                     ; 取出字符串 ds 段地址

                    loop disp                   ; 列循环

                    pop  cx
                    loop row_offset             ; 行循环


       ok:          
                    pop  bx
                    pop  ax
                    pop  si

                    pop  cx
                    pop  dx

                    ret

       ;功能：将 buff 中的值初始化为 20H
       ;参数：无
       ;返回：无
       clear_buff:  push ax
                    push es
                    push si
                    push cx

                    mov  ax, buff
                    mov  es, ax

                    mov  si, 0
                    mov  cx, 7

       clear:       mov  es:[si], 20H
                    inc  si
                    loop clear
  
                    pop  cx
                    pop  si
                    pop  es
                    pop  ax

                    ret

code ends
end start