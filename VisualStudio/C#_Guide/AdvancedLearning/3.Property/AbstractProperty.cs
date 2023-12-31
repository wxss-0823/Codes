using System;

namespace PropertyApplication
{
    public abstract class Person
    {
        public abstract string Name 
        { 
            get; 
            set;
        }

        public abstract int Age
        {
            get;
            set;
        }
    }

    class Student : Person
    {
        private string code = "N.A";
        private string name = "N.A";
        private int age = 0;

        // 声明类型为 string 的 Code 属性
        public string Code
        {
            get
            {
                return code;
            }
            set
            {
                code = value;
            }
        }

        // 声明类型为 string 的 Name 属性
        public override string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }

        // 声明类型为 int 的 age 属性
        public override int Age
        {
            get
            {
                return age;
            }
            set
            {
                age = value;
            }
        }

        public override string ToString()
        {
            return "Code =" + Code + ", Name = " + Name + ", Age = " + Age;
        }
    }

    class ExacuteDemo 
    {
        public static void Main()
        {
            // 创建一个新的 Student 对象
            Student s = new Student();

            // 设置 student 的 code、name 和 age
            s.Code = "001";
            s.Name = "Zara";
            s.Age = 9;
            Console.WriteLine("Student Info:- {0}", s);
            // 增加年龄
            s.Age += 1;
            Console.WriteLine("Student Info:- {0}", s);
            Console.ReadKey();
        }
    }

}