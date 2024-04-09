public class Test {
    public static void main(String[] args) {
        show(new Cat());    // 以 Cat 对象调用 show 方法
        show(new Dog());    // 以 Dog 对象调用 show 方法

        Animal a = new Cat();   // 向上转型
        a.eat();                // 调用的是 Cat 的方法
        Cat c = (Cat) a;        // 向下转型
        c.work();
        // 不能使用 a.work(); 因为 Animal 类下不存在 work() 抽象函数
    }

    public static void show(Animal a) {
        a.eat();
        if (a instanceof Cat) {
            Cat c = (Cat) a;
            c.work();
        } else if (a instanceof Dog) {
            Dog b = (Dog) a;
            b.work();
        }
    }
}


abstract class Animal {
    abstract void eat();
}

class Cat extends Animal {
    public void eat() {
        System.out.println("吃鱼");
    }
    public void work() {
        System.out.println("抓老鼠");
    }
}

class Dog extends Animal {
    public void eat() {
        System.out.println("吃骨头");
    }
    public void work() {
        System.out.println("看家");
    }
}
