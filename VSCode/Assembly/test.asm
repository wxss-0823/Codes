assume cs:code
data segment
       dd 5937000
data ends

table segment
        db 21 dup ('xxxx     xxxxxxx   xxxxx    xxx ')  ; 21*32byte
table ends

buff segment
       db 14 dup(0)
       db 10 dup(0)
buff ends

code segment
  start:                            ;mov  ax, data
  ;  mov  ds, ax
  ;  mov  ax, ds:[0]
  ;  mov  dx, ds:[2]
  ;  call dtoc

             mov  dh, 2
             mov  dl, 25
             mov  cl, 2
             mov  ch, 0
             mov  ax, table
             mov  ds, ax
             call show_str

             mov  ax, 4c00H
             int  21H


  ;功能：将 double word 型数据转变为表示十进制数的字符串
  ;参数：(dx)=H16，(ax)=L16，ds:si 指向字符串首地址
  ;返回：无
  dtoc:      push ax
             push ds
             push si
             push dx
             push cx
             push es

             mov  cx, buff
             mov  es, cx
             mov  si, 0

  dtoc_core: mov  cx, 10
             call divdw             ; 结果：dx=H16, ax=L16, cx=rem
             add  cx, 30H
             mov  es:[si], cx       ; 计算最后一位的 ASCII 码，并放入 buff
             inc  si
             mov  cx, ax
             or   cx, dx            ; 判断商的每一位是否为 0
             jcxz dtoc_write
             jmp  short dtoc_core

  dtoc_write:mov  ax, table         ; 商为 0 时，反向读取 ASCII 码，并放入 table
             mov  ds, ax
             mov  al, es:[si]
             push si
             mov  cx, 6
             sub  cx, si
             mov  si, cx
             mov  ds:[si+9], al     ; 缺少一个表示行数的变量
             pop  si
             mov  cx, si
             dec  si
             jcxz dtoc_out
             jmp  short dtoc_write
  
  dtoc_out:  pop  es                ; 退出子程序
             pop  cx
             pop  dx
             pop  si
             pop  ds
             pop  ax
             ret


  ;功能：进行不会产生溢出的除法运算，被除数为 dword 型，除数为 word 型，结果为 dword 型
  ;参数：(ax)=dword 型数据的低 16 位，(bx)=dword 型数据的高 16 位，(cx)=除数
  ;返回：(dx)=结果的高 16 位，(ax)=结果的低 16 位，(cx)=余数
  divdw:     push ax                ; 参数寄存器保存
             push dx
             push cx

             mov  bp, sp
             mov  ax, [bp+2]        ; 取出 H16
             mov  dx, 0             ; 高位置 0
             div  cx                ; 除数为 16 位，被除数位 dx-ax，结果 ax 为商，dx 为余数

             mov  [bp+2], ax        ; 写回 H16

             mov  ax, [bp+4]
             div  cx
             mov  [bp+4], ax        ; 写回 L16
             mov  [bp], dx          ; 写回 rem
  divdw_out: pop  cx
             pop  dx
             pop  ax
             ret

  ;功能：在指定的位置，用指定的颜色，显示一个用 0 结束的字符串
  ;参数：(dh)=行号(取值范围 0~24)，(dl)=列号(取值范围 0~79)，(cl)=颜色，ds:si 指向字符串的首地址
  ;返回：void
  show_str:  push dx                ; 参数寄存器保存
             push cx

             push si                ; 子程序使用到的寄存器保存
             push ax
             push bx
  
             mov  al, 00A0H         ; 计算字符串显示起始位置
             mov  ah, 0
             mul  dh                ; 计算行偏置，每行 A0 个字符
             mov  bx, ax
             mov  al, 2             ; 计算列偏置，每列字符=列数*2
             mov  ah, 0
             mul  dl
             add  bx, ax            ; 计算结果：显存不允许从奇数地址存入数据
             mov  si, 0
             mov  dx, cx
             mov  cx, 21
             push cx
             mov  cx, 16
             jmp  short disp

  row_offset:push cx
             add  bx, 0060H

             mov  cx, 16

  disp:      push ds                ; 字符串 ds 段地址保存
             push ds:[si]           ; push 两个字节的字符入栈
           
             mov  ax, 0B800H        ; 显存 ds 段地址
             mov  ds, ax
             pop  ax                ; pop 两个字节的字符出栈

             mov  ds:[bx], al       ; 第一个字符放入显存
             mov  ds:[bx].1, dl     ; 颜色配置放入显存
             mov  ds:[bx].2, ah     ; 第二个字符放入显存
             mov  ds:[bx].3, dl     ; 颜色配置放入显存

             add  si, 2
             add  bx, 4
             pop  ds                ; 取出字符串 ds 段地址

             loop disp              ; 列循环

             pop  cx
             loop row_offset        ; 行循环


  ok:        
             pop  bx
             pop  ax
             pop  si

             pop  cx
             pop  dx

             ret
code ends
end start