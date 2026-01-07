assume cs:code
data segment
            DB '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983'
            DB '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992'
            DB '1993', '1994', '1995'

            DD 16, 22, 382, 1356, 2390, 8000, 16000, 24486, 50065, 97479, 140417, 197514
            DD 345980, 590827, 803530, 1183000, 1843000, 2759000, 3753000, 4649000, 5937000

            DW 3, 7, 9, 13, 28, 38, 130, 220, 476, 778, 1001, 1442, 2258, 2793, 4037, 5635, 8226
            DW 11542, 14430, 15257, 17800
data ends

table segment
             ; db 21 dup ('xxxx     xxxxxxx   xxxxx    xxx ')  ; 21*32byte
             DB 672 DUP(20H)
table ends

buff segment
            DB 7 DUP(0)
buff ends

code segment
       start:        MOV  AX, data               ; 段地址定位
                     MOV  DS, AX
                     MOV  AX, table
                     MOV  ES, AX

                     MOV  SI, 0                  ;寄存器初始化
                     MOV  BX, 0
                     MOV  CX, 21

       year:         MOV  AX, DS:[SI]            ; 每一个年份 4byte 存入 table
                     MOV  ES:[BX], AX
                     MOV  AX, DS:[SI+2]
                     MOV  ES:[BX+2], AX
                     ADD  SI, 4
                     ADD  BX, 32
                     LOOP year


                     MOV  CX, 21
                     MOV  BX, 054H

       income:       MOV  AX, DS:[BX]
                     MOV  DX, DS:[BX+2]

                     PUSH BX
                     MOV  BX, 9

                     CALL dtoc

                     POP  BX
                     ADD  BX, 4

                     LOOP income

                     MOV  CX, 21
                     MOV  BX, 0A8H

       num:          MOV  AX, DS:[BX]
                     MOV  DX, 0

                     PUSH BX
                     MOV  BX, 19

                     CALL dtoc

                     POP  BX
                     ADD  BX, 2

                     LOOP num


                     MOV  CX, 21
                     MOV  SI, 0
                     MOV  DI, 0
                     MOV  DX, 0

       avgIncome:    MOV  AX, DS:[SI+054H]       ; L16
                     MOV  DX, DS:[SI+056H]       ; H16

                     PUSH CX

                     MOV  CX, DS:[DI+0A8H]

                     CALL divdw                  ; dx=H16, ax=L16, cx=rem
                     POP  CX                     ; 一定要提前 pop，dtoc 需要 cx 作为参数

                     PUSH BX
                     MOV  BX, 28                 ; 初始化固定偏移量

                     CALL dtoc                   ; 将平均收入转化为字符

                     ADD  SI, 4
                     ADD  DI, 2
                     POP  BX

                     LOOP avgIncome

       print2screen: MOV  DH, 2                  ; 显示 table 中保存的字符
                     MOV  DL, 25
                     MOV  CL, 2
                     MOV  CH, 0
                     MOV  AX, table
                     MOV  DS, AX
                     CALL show_str

                     MOV  AX, 4c00H
                     INT  21H

       ;功能：将 double word 型数据转变为表示十进制数的字符串
       ;参数：(dx)=H16，(ax)=L16，(cx)=当前行数，(bx)=固定偏移量
       ;返回：无
       dtoc:         PUSH AX
                     PUSH DS
                     PUSH SI
                     PUSH DX
                     PUSH CX
                     PUSH ES
                     PUSH DI
                     PUSH BX

                     MOV  SI, 21                 ; cx 存放当前循环次数，计算当前循环次数对应的 table 偏置
                     SUB  SI, CX
                     MOV  CX, SI

       dtoc_offset:  ADD  BX, 32
                     LOOP dtoc_offset

                     MOV  CX, buff
                     MOV  ES, CX
                     MOV  SI, 0

       dtoc_core:    MOV  CX, 10
                     CALL divdw                  ; 结果：dx=H16, ax=L16, cx=rem
                     ADD  CX, 30H
                     MOV  ES:[SI], CX            ; 计算最后一位的 ASCII 码，并放入 buff
                     INC  SI
                     MOV  CX, AX
                     OR   CX, DX                 ; 判断商的每一位是否为 0
                     JCXZ dtoc_tmp
                     JMP  SHORT dtoc_core

       dtoc_tmp:     MOV  CX, SI                 ; cx=si+1，初始化循环参数
                     DEC  SI
                     MOV  DI, 0

       dtoc_write:   MOV  AX, table              ; 商为 0 时，反向读取 ASCII 码，并放入 table
                     MOV  DS, AX
                     MOV  AL, ES:[SI]
                     MOV  DS:[BX+DI], AL         ; 缺少一个表示行数的变量
                     INC  DI
                     DEC  SI
                     LOOP dtoc_write

       dtoc_out:     POP  BX
                     POP  DI
                     POP  ES                     ; 退出子程序
                     POP  CX
                     POP  DX
                     POP  SI
                     POP  DS
                     POP  AX
                     RET

       ;功能：进行不会产生溢出的除法运算，被除数为 dword 型，除数为 word 型，结果为 dword 型
       ;参数：(ax)=dword 型数据的低 16 位，(dx)=dword 型数据的高 16 位，(cx)=除数
       ;返回：(dx)=结果的高 16 位，(ax)=结果的低 16 位，(cx)=余数
       divdw:        PUSH AX                     ; 参数寄存器保存
                     PUSH DX
                     PUSH CX

                     MOV  BP, SP
                     MOV  AX, [BP+2]             ; 取出 H16
                     MOV  DX, 0                  ; 高位置 0
                     DIV  CX                     ; 除数为 16 位，被除数位 dx-ax，结果 ax 为商，dx 为余数

                     MOV  [BP+2], AX             ; 写回 H16

                     MOV  AX, [BP+4]
                     DIV  CX
                     MOV  [BP+4], AX             ; 写回 L16
                     MOV  [BP], DX               ; 写回 rem
       divdw_out:    POP  CX
                     POP  DX
                     POP  AX
                     RET

       ;功能：在指定的位置，用指定的颜色，显示一个用 0 结束的字符串
       ;参数：(dh)=行号(取值范围 0~24)，(dl)=列号(取值范围 0~79)，(cl)=颜色，ds:si 指向字符串的首地址
       ;返回：void
       show_str:     PUSH DX                     ; 参数寄存器保存
                     PUSH CX

                     PUSH SI                     ; 子程序使用到的寄存器保存
                     PUSH AX
                     PUSH BX

                     MOV  AL, 00A0H              ; 计算字符串显示起始位置
                     MOV  AH, 0
                     MUL  DH                     ; 计算行偏置，每行 A0 个字符
                     MOV  BX, AX
                     MOV  AL, 2                  ; 计算列偏置，每列字符=列数*2
                     MOV  AH, 0
                     MUL  DL
                     ADD  BX, AX                 ; 计算结果：显存不允许从奇数地址存入数据
                     MOV  SI, 0
                     MOV  DX, CX
                     MOV  CX, 21
                     PUSH CX
                     MOV  CX, 16
                     JMP  SHORT disp

       row_offset:   PUSH CX
                     ADD  BX, 0060H

                     MOV  CX, 16

       disp:         PUSH DS                     ; 字符串 ds 段地址保存
                     PUSH DS:[SI]                ; push 两个字节的字符入栈

                     MOV  AX, 0B800H             ; 显存 ds 段地址
                     MOV  DS, AX
                     POP  AX                     ; pop 两个字节的字符出栈

                     MOV  DS:[BX], AL            ; 第一个字符放入显存
                     MOV  DS:[BX].1, DL          ; 颜色配置放入显存
                     MOV  DS:[BX].2, AH          ; 第二个字符放入显存
                     MOV  DS:[BX].3, DL          ; 颜色配置放入显存

                     ADD  SI, 2
                     ADD  BX, 4
                     POP  DS                     ; 取出字符串 ds 段地址

                     LOOP disp                   ; 列循环

                     POP  CX
                     LOOP row_offset             ; 行循环


       ok:
                     POP  BX
                     POP  AX
                     POP  SI

                     POP  CX
                     POP  DX

                     RET

       ;功能：将 buff 中的值初始化为 20H
       ;参数：无
       ;返回：无
       clear_buff:   PUSH AX
                     PUSH ES
                     PUSH SI
                     PUSH CX

                     MOV  AX, buff
                     MOV  ES, AX

                     MOV  SI, 0
                     MOV  CX, 7

       clear:        MOV  ES:[SI], 20H
                     INC  SI
                     LOOP clear

                     POP  CX
                     POP  SI
                     POP  ES
                     POP  AX

                     RET

code ends
end start