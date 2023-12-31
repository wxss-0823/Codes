using System;
namespace ArrayApplication
{
    class MyArray
    {
        static void Main(string[] args)
        {
            int[] n = new int[10];//是一个带有10个整数的数组
            int i, j;

            //初始化数组n中的元素
            for (i = 0; i <10; i++)
            {
                n[i] = i + 100;
            }

            //输出每个数组元素的值
            for (j = 0; j < 10; j++)
            {
                Console.WriteLine("Element[{0}] = {1}", j, n[j]);
            }
            Console.ReadKey();
        }
    }
}
