using System;
namespace StringApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            // 字符串，字符串连接
            string fname, lname;
            fname = "Wang";
            lname = "Xishengshun";

            string fullname = fname + lname;
            Console.WriteLine("Full name: {0}", fullname);

            // 通过使用string构造函数
            char[] letters = { 'H', 'e', 'l', 'l', 'o' };
            string greetings = new string(letters);
            Console.WriteLine("Greetings: {0}", greetings);

            // 方法返回字符串
            string[] sarray = { "Hello", "From", "Tutorials" };
            string message = string.Join(" ", sarray);
            Console.WriteLine("Message: {0}", message);

            // 用于转化值的格式化方法
            DateTime waiting = new DateTime(2023, 12, 27, 9, 17, 1);
            string chat = string.Format("Message sent at {0:t} on {0:D}", waiting);
            Console.WriteLine("Message: {0}", chat);
            Console.ReadKey();
        }
    }
}