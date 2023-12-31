// 主线程实例
//using System;
//using System.Threading;

//namespace MultithreadingApplication
//{
//    class MainThreadingProgram
//    {
//        static void Main(string[] args)
//        {
//            Thread th = Thread.CurrentThread;
//            th.Name = "MainThread";
//            Console.WriteLine("This is {0}", th.Name);
//            Console.ReadKey();
//        }
//    }
//}

using System;
using System.Threading;

namespace MultithreadingApplication
{
    class ThreadCreationProgram
    {
        public static void CallToChildThread()
        {
            try
            {
                Console.WriteLine("Child Thread Starts");
                // 计数到 10
                for (int count = 0; count <= 10; count++)
                {
                    Thread.Sleep(500);
                    Console.WriteLine(count);
                }
                Console.WriteLine("Child Thread Completed");
            }
            catch (ThreadAbortException e)
            {
                Console.WriteLine("Thrad Abort Exception: {0}", e);
            }
            finally
            {
                Console.WriteLine("Couldn't catch the Thread Exception");
            }
        }
        static void Main()
        {
            ThreadStart childref = new ThreadStart(CallToChildThread);
            CancellationTokenSource source = new CancellationTokenSource();
            Console.WriteLine("In Main: Creating the Child thread");
            Thread childThread = new Thread(childref);
            childThread.Start();
            
            // 停止主线程一段时间
            Thread.Sleep(2000);

            // childThread.Abort();  方法过时

            // 使用 CancelleationTokenSource
            // Cancel()手动取消任务，点击一下取消
            source.Cancel();
            Console.ReadKey();
        }
    }
}