assume cs:code
data segment
          DB '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983'
          DB '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992'
          DB '1993', '1994', '1995'
          ;以上是表示 21 年的 21 个字符串
          DD 16, 22, 382, 1356, 2390, 8000, 16000, 24486, 50065, 97479, 140417, 197514
          DD 345980, 590827, 803530, 1183000, 1843000, 2759000, 3753000, 4649000, 5937000
          ;以上是表示 21 年公司总收入的 21 个 dword 型数据
          DW 3, 7, 9, 13, 28, 38, 130, 220, 476, 778, 1001, 1442, 2258, 2793, 4037, 5635, 8226
          DW 11542, 14430, 15257, 17800
;以上是表示 21 年公司雇员人数的 21 个 word 型数据
data ends

table segment
           DB 21 DUP ('xxxx xxxx xx xx ')
table ends

code segment
     start: MOV  AX, data           ; 段地址定位
            MOV  DS, AX
            MOV  AX, table
            MOV  ES, AX

            MOV  SI, 0
            MOV  DI, 84
            MOV  BP, 168
            MOV  BX, 0
            MOV  CX, 21

     s:     PUSH CX                 ; 计算当前行数对应的内存 offset
            MOV  AX, 21
            SUB  AX, CX
            MOV  CX, AX
            MOV  AX, 16
            MUL  CL
            MOV  BX, AX             ; 计算结果存入 bx

            MOV  AX, DS:[SI]
            MOV  ES:[BX], AX
            ADD  SI, 2
            MOV  AX, DS:[SI]
            MOV  ES:[BX+2], AX
            ADD  SI, 2

            MOV  AX, DS:[DI]
            PUSH AX                 ; L16
            MOV  ES:[BX+5], AX
            ADD  DI, 2
            MOV  AX, DS:[DI]
            PUSH AX                 ; H16
            MOV  ES:[BX+7], AX
            ADD  DI, 2

            MOV  AX, DS:[BP]
            MOV  ES:[BX+10], AX
            ADD  BP, 2

            MOV  CX, AX
            POP  DX
            POP  AX
            DIV  CX
            MOV  ES:[BX+13], AX

            POP  CX
            LOOP s

            MOV  AX, 4c00H
            INT  21H
code ends
end start