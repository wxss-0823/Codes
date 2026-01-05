assume cs:code
data segment
       db 'welcome to masm!', 0
data ends

code segment
  start:   mov  dh, 8
           mov  dl, 3
           mov  cl, 2
           mov  ax, data
           mov  ds, ax
           mov  si, 0
           call show_str

           mov  ax, 4c00H
           int  21H


  ;功能：在指定的位置，用指定的颜色，显示一个用 0 结束的字符串
  ;参数：(dh)=行号(取值范围 0~24)，(dl)=列号(取值范围 0~79)，(cl)=颜色，ds:si 指向字符串的首地址
  ;返回：void
  show_str:push dx             ; 参数寄存器保存
           push cx

           push si             ; 子程序使用到的寄存器保存
           push ax
           push bx
                   
  
           mov  al, 00A0H      ; 计算字符串显示起始位置
           mov  ah, 0
           mul  dh             ; 计算行偏置，每行 A0 个字符
           mov  bx, ax
           mov  al, 2          ; 计算列偏置，每列字符=列数*2
           mov  ah, 0
           mul  dl
           add  bx, ax         ; 计算结果：显存不允许从奇数地址存入数据

  disp:    push ds             ; 字符串 ds 段地址保存
           push ds:[si]        ; push 两个字节的字符入栈
           
           mov  ax, 0B800H     ; 显存 ds 段地址
           mov  ds, ax
           pop  ax             ; pop 两个字节的字符出栈

           mov  ds:[bx], al    ; 第一个字符放入显存
           mov  ds:[bx].1, cl  ; 颜色配置放入显存
           mov  ds:[bx].2, ah  ; 第二个字符放入显存
           mov  ds:[bx].3, cl  ; 颜色配置放入显存

           inc  si
           add  bx, 2
           pop  ds             ; 取出字符串 ds 段地址

           push cx
           mov  cx, [si]       ; 判断字符串结尾
           jcxz ok
           pop  cx
           jmp  short disp

  ok:      pop  cx
           pop  bx
           pop  ax
           pop  si

           pop  cx
           pop  dx

           ret

code ends
end start