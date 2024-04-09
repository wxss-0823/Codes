class SuperClass {
    private int n;
    // 不含参数的构造函数
    SuperClass() {
        System.out.println("SuperClass()");
    }
    // 含参数的构造函数
    SuperClass(int n) {
        System.out.println("SuperClass(" + n + ")");
        this.n = n;
    }
}

// 子类 1，继承子 SuperClass
class SubClass extends SuperClass {
    private int n;

    // 不含参数的构造函数
    SubClass() {
        // 缺省，首先自动调用父类的无参数构造函数
        System.out.println("SubClass()");
    }
    // 含参数的构造函数
    SubClass(int n) {
        super(300); // 指定调用父类的含参数构造函数
        System.out.println("SubClass(" + n + ")");
    }
}

// 子类 1，继承子 SuperClass
class SubClass1 extends SuperClass {
    private int n;

    // 不含参数的构造函数
    SubClass1() {
        super(300); // 指定调用父类的含参数构造函数
        System.out.println("SubClass()");
    }
    // 含参数的构造函数
    SubClass1(int n) {
        // 缺省，首先自动调用父类的无参数构造函数
        System.out.println("SubClass(" + n + ")");
    }
}

public class TestSuperSub {
    public static void main(String[] args) {
        System.out.println("-----SubClass 类继承-----");
        SubClass sc1 = new SubClass();
        SubClass sc2 = new SubClass(2);
        System.out.println("-----SubClass 类继承-----");
        SubClass1 sc3 = new SubClass1();
        SubClass1 sc4 = new SubClass1(4);
    }
}
