public class FinalizationDemo {
    public static void main(String[] args) {
        Cake cake1 = new Cake(1);
        Cake cake2 = new Cake(2);
        Cake cake3 = new Cake(3);

        cake1 = cake2 = cake3 = null;

        // 调用系统垃圾回收器
        System.gc();
    }
}

class Cake extends Object {
    private int id;
    public Cake(int id){
        this.id = id;
        System.out.println("Cake Object " + id + " is created.");
    }

    // throws 关键字表示，函数可能存在异常，需要进行异常处理
    protected void finalize() throws Throwable {
        super.finalize();
        System.out.println("Cake Object " + id + " is disposed.");
    }
}