import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.FutureTask;

public class CallableTest implements Callable<Integer> {
    public static void main(String[] args) {
        CallableTest c1 = new CallableTest();
        FutureTask<Integer> ft = new FutureTask<>(c1);

        // 循环内主线程打印与子线程打印是并行的，等待子线程完全结束，才能跳出循环
        for(int i = 0; i < 100; i++) {
            System.out.println(Thread.currentThread().getName() + " 的循环变量i的值" + i);
            if(i == 20) {
                new Thread(ft, "Thread-with-return").start();
            }
        }

        try {
            System.out.println("子线程的返回值：" + ft.get());
        } catch (InterruptedException | ExecutionException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public Integer call() throws Exception {
        int i = 0;
        for(; i < 100; i++) {
            System.out.println(Thread.currentThread().getName() + " " + i);
        }
        return i;
    }
}
