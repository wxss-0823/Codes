assume cs:code
data segment
            DB 'welcome to masm!', 0
data ends

code segment
       start:    MOV  DH, 8
                 MOV  DL, 3
                 MOV  CL, 2
                 MOV  AX, data
                 MOV  DS, AX
                 MOV  SI, 0
                 CALL show_str

                 MOV  AX, 4c00H
                 INT  21H


       ;功能：在指定的位置，用指定的颜色，显示一个用 0 结束的字符串
       ;参数：(dh)=行号(取值范围 0~24)，(dl)=列号(取值范围 0~79)，(cl)=颜色，ds:si 指向字符串的首地址
       ;返回：void
       show_str: PUSH DX                  ; 参数寄存器保存
                 PUSH CX

                 PUSH SI                  ; 子程序使用到的寄存器保存
                 PUSH AX
                 PUSH BX


                 MOV  AL, 00A0H           ; 计算字符串显示起始位置
                 MOV  AH, 0
                 MUL  DH                  ; 计算行偏置，每行 A0 个字符
                 MOV  BX, AX
                 MOV  AL, 2               ; 计算列偏置，每列字符=列数*2
                 MOV  AH, 0
                 MUL  DL
                 ADD  BX, AX              ; 计算结果：显存不允许从奇数地址存入数据
                 MOV  SI, 0

       disp:     PUSH DS                  ; 字符串 ds 段地址保存
                 PUSH DS:[SI]             ; push 两个字节的字符入栈

                 MOV  AX, 0B800H          ; 显存 ds 段地址
                 MOV  DS, AX
                 POP  AX                  ; pop 两个字节的字符出栈

                 MOV  DS:[BX], AL         ; 第一个字符放入显存
                 MOV  DS:[BX].1, CL       ; 颜色配置放入显存
                 MOV  DS:[BX].2, AH       ; 第二个字符放入显存
                 MOV  DS:[BX].3, CL       ; 颜色配置放入显存

                 ADD  SI, 2
                 ADD  BX, 4
                 POP  DS                  ; 取出字符串 ds 段地址

                 PUSH CX
                 MOV  CX, [SI]            ; 判断字符串结尾
                 JCXZ ok
                 POP  CX
                 JMP  SHORT disp

       ok:       POP  CX
                 POP  BX
                 POP  AX
                 POP  SI

                 POP  CX
                 POP  DX

                 RET

code ends
end start