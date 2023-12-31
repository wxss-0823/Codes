using System;

namespace DelegareApplication
{
    class PrintString
    {
        static FileStream fs;
        static StreamWriter sw;
        // 委托声明
        public delegate void printString(string s);

        // 该方法打印到控制台
        public static void WriteToScreen(string s)
        {
            Console.WriteLine("This string is: {0}", s);
        }
        // 该方法打印到文件
        public static void WriteToFile(string s)
        {
            fs = new FileStream(".\\message.txt", FileMode.Append, FileAccess.Write);
            sw = new StreamWriter(fs);
            sw.WriteLine(s);
            sw.Flush();
            sw.Close();
            fs.Close();
        }

        // 该方法把委托作为参数，并使用它调用方法
        public static void sendString(printString ps)
        {
            ps("Hello World!");
        }

        static void Main(string[] args)
        {
            printString ps;
            printString ps1 = new printString(WriteToScreen);
            printString ps2 = new printString(WriteToFile);
            ps = ps1 + ps2;
            sendString(ps);
            Console.ReadKey();
        }
    }
}