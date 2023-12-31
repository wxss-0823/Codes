using System;
namespace TypeConversionApplication
{
    class ExplicitConversion
    {
        static void Main(string[] args)
        {
            double d = 5673.74;
            int i;

            // 强制转换double为int
            i = (int)d;
            Console.WriteLine(i);

            // 将不同值的类型转换为字符串类型
            int a = 75;
            float b = 53.005f;
            double c = 2345.7652;
            bool e = true;
            Console.WriteLine(a.ToString());
            Console.WriteLine(b.ToString());
            Console.WriteLine(c.ToString());
            Console.WriteLine(e.ToString());
            Console.ReadKey();
        }
    }
}
