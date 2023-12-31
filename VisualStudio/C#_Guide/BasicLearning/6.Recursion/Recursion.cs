using System;

namespace CalculatorApplication
{
    class NumberMainpulator
    {
        public int factorial(int num)
        {
            /* 局部变量定义 */
            int result;

            if (num == 1)
            {
                return 1;
            }
            else
            {
                result = factorial(num - 1) * num;
                return result;
            }
        }

        public void GetValue(out int x, out int y)
        {
            Console.WriteLine("请输入第一个值：");
            x = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("请输入第二个值：");
            y = Convert.ToInt32(Console.ReadLine());
        }

        static void Main(string[] args) 
        { 
            NumberMainpulator n = new NumberMainpulator();
            // 调用factorial方法
            Console.WriteLine("6的阶乘是：{0}", n.factorial(6));

            /* 局部变量定义 */
            int a, b;

            /* 调用函数来获取值 */
            n.GetValue(out a, out b);

            Console.WriteLine("在方法调用之后，a的值： {0}", a);
            Console.WriteLine("在方法调用之后，b的值： {0}", b);
            Console.ReadLine();
        }
    }
}