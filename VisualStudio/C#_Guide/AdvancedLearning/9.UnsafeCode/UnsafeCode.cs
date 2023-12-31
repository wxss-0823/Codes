using System;

namespace UnsafeCodeApplication
{
    class TestPointer
    {
        public unsafe static void Main(string[] args)
        {
            int[] list = { 10, 100, 200 };
            fixed (int* ptr = list) 

            /* 显示指针中的数组地址 */
            for (int i = 0; i < 3; i++)
            {
                Console.WriteLine("Address of list[{0}] = {1}", i, (int)(ptr + i));
                Console.WriteLine("Value of list[{0}] = {1}", i, *(ptr + i));
            }
            Console.ReadKey();
        }
    }
}