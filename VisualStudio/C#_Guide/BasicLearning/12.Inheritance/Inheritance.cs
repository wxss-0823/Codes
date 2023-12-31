using System;

namespace InheritanceApplication
{
    class Shape
    {
        protected int width;
        protected int height;
        public void setWidth(int w)
        {
            width = w;
        }

        public void setHeight(int h)
        {
            height = h;
        }
    }

    // 基类 PaintCost
    public interface PaintCost
    {
        int getCost(int area);
    }

    // 派生类
    class Rectangle : Shape, PaintCost
    {
        public int getArea()
        {
            return (width * height);
        }

        public int getCost(int area)
        {
            return area * 70;
        }
    }

    class RectangleTester
    {
        static void Main(string[] args)
        {
            Rectangle Rect = new Rectangle();
            int area;
            Rect.setWidth(5);
            Rect.setHeight(7);
            area = Rect.getArea();

            // 打印对象的面积
            Console.WriteLine("总面积：{0}", area);
            Console.WriteLine("油漆总成本：{0}", Rect.getCost(area));
            Console.ReadKey();
        }
    }
}