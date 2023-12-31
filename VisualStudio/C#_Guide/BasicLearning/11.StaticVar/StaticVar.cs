using System;

namespace StaticVarApplication
{
    class StaticVar
    {
        public static int num;
        public void count()
        {
            num++;
        }

        public static int getNum()
        {
            return num;
        }
    }

    class StaticTester
    {
        static void Main()
        {
            StaticVar s = new StaticVar();
            s.count();
            s.count();
            s.count();
            // 用类名访问静态函数
            Console.WriteLine("变量 num: {0}", StaticVar.getNum());

            Console.ReadKey();
        }
    }
}