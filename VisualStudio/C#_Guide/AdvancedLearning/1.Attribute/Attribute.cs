using System;

[AttributeUsage(AttributeTargets.All)]
public class HelpAttribute : System.Attribute
{
    public readonly string Url;
    private string topic;

    public HelpAttribute(string url)    // url 是一个定位参数
    {
        this.Url = url;
    }

    public string Topic // Topic 是一个命名参数
    {
        get
        {
            return topic;
        }
        set
        {
            topic = value;
        }
    }
}

[HelpAttribute("Information on the class MyClass")]
class MyClass
{

}

namespace AttributeApplicaton
{
    class Program
    {
        static void Main(string[] args)
        {
            System.Reflection.MemberInfo info = typeof(MyClass);
            object[] attributes = info.GetCustomAttributes(true);
            for (int i = 0; i < attributes.Length; i++)
            {
                System.Console.WriteLine(attributes[i]);
            }
            Console.ReadKey();
        }
    }
}