using System;

namespace PolymorphismApplicaiton
{
    class Shape
    {
        protected int width, height;
        public Shape(int a = 0, int b = 0)
        {
            width = a;
            height = b;
        }

        public virtual int area()
        {
            Console.WriteLine("父类的面积：");
            return 0;
        }
    }

    class Rectangle : Shape
    {
        // 从基类中调用构造函数用 base 关键字
        public Rectangle(int a = 0, int b = 0): base(a, b) 
        {

        }

        public override int area()
        {
            Console.WriteLine("Rectangle类的面积：");
            return (width * height);  
        }

    }

    class Triangle : Shape
    {
        public Triangle(int a = 0, int b =0): base(a, b)
        {

        }

        public override int area()
        {
            Console.WriteLine("Triangle类的面积：");
            return (width * height / 2);
        }
    }

    class Caller
    {
        public void CallArea(Shape sh)
        {
            int a;
            a = sh.area();
            Console.WriteLine("面积：{0}", a);
        }
    }

    class Teater
    {
        static void Main(string[] args)
        {
            Caller c = new Caller();
            Rectangle r = new Rectangle(10, 7); 
            Triangle t = new Triangle(10, 5);
            c.CallArea(r);
            c.CallArea(t);
            Console.ReadKey();
        }
    }
}