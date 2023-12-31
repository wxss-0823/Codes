using System;
using System.Reflection;

namespace DeBugInfoApplication
{
    // 一个自定义特性 DeBugInfo 被赋给类及其成员
    [AttributeUsage(AttributeTargets.Class |
        AttributeTargets.Constructor |
        AttributeTargets.Field |
        AttributeTargets.Method |
        AttributeTargets.Property,
        AllowMultiple = true)]
    public class DeBugInfo : System.Attribute
    {
        private int bugNo;          // position
        private string developer;   // position
        private string lastReview;  // position
        public string message;      // named

        // 定义特性的构造函数
        public DeBugInfo(int bg, string dev, string d)
        {
            this.bugNo = bg;
            this.developer = dev;
            this.lastReview = d;
        }

        public int BugNo    // position
        {
            get
            {
                return bugNo;
            }
            set
            {
                bugNo = value;
            }
        }

        public string Developer // position
        {
            get
            {
                return developer;
            }
            set
            {
                developer = value;
            }
        }

        public string LastReview    // position
        {
            get
            {
                return lastReview;
            }
            set
            {
                lastReview = value;
            }

        }

        public string Message
        {
            get
            {
                return message;
            }
            set 
            { 
                message = value; 
            }
        }
    }

    [DeBugInfo(45, "Zara Ali", "12/8/2012", Message = "Return type mismatch")]
    [DeBugInfo(49, "Nuha Ali", "10/10/2012", Message = "Unused variable")]
    class Rectangle
    {
        // 成员变量
        protected double length;
        protected double width;

        public Rectangle(double l, double w)
        {
            length = l;
            width = w;
        }

        [DeBugInfo(55, "Zara Ali", "19/10/2012", Message = "Return type mismatch")]
        public double GetArea()
        {
            return length * width;
        }

        [DeBugInfo(56, "Zara Ali", "19/10/2012")]
        public void Display()
        {
            Console.WriteLine("Length: {0}", length);
            Console.WriteLine("Width: {0}", width);
            Console.WriteLine("Area: {0}", GetArea());
        }// end class Rectangle
    }

    class ExcuteRectangle
    {
        static void Main(string[] args)
        {
            Rectangle r = new Rectangle(4.5, 7.5);
            r.Display();
            Type type = typeof(Rectangle);
            // 遍历 Rectangle 类的特性
            foreach (Object attributes in type.GetCustomAttributes(false))
            {
                DeBugInfo db1 = (DeBugInfo)attributes;
                if (db1 != null)
                {
                    Console.WriteLine("Bug no: {0}", db1.BugNo);
                    Console.WriteLine("Developer: {0}", db1.Developer);
                    Console.WriteLine("Last Reviewd: {0}", db1.LastReview);
                    Console.WriteLine("Remarks: {0}", db1.Message);
                }
            }

            // 遍历 Rectangle 类的方法特性
            foreach (MethodInfo m in type.GetMethods(BindingFlags.DeclaredOnly | 
                BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public))
                // GetMathods 后为空，会默认调用 GetType(), GetHashCode(), ToString()等方法
            {
                Console.WriteLine("{0}", m);
                foreach (Attribute a in m.GetCustomAttributes(true))
                {
                    DeBugInfo dbi = (DeBugInfo)a;
                    if (dbi != null)
                    {
                        Console.WriteLine("Bug no: {0}, for Method: {1}", dbi.BugNo, m);
                        Console.WriteLine("Developer: {0}", dbi.Developer);
                        Console.WriteLine("Last Reviewed: {0}", dbi.LastReview);
                        Console.WriteLine("Remarks: {0}", dbi.Message);
                    }
                }
            }
            Console.ReadLine();
        }
    }
}
