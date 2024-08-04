public class RunnableDemo implements Runnable {
    private Thread t;
    private String threadName;

    RunnableDemo(String name) {
        this.threadName  = name;
        System.out.println("Creating " + threadName);
    }

    public void run() {
        System.out.println("Running " + threadName);
        try {
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " + threadName + ", " + i);
                // 睡眠
                Thread.sleep(1000);
            }
        } catch(InterruptedException e) {
            System.out.println("Thread " + threadName + "interrupted");
        }
        System.out.println("Thread " + threadName +"exiting");
    }

    public void start() {
        if(t == null) {
            t = new Thread(this, threadName);
            t.start();
        }
    }
}

class ThreadTest1 {
    public static void main(String[] args) {
        RunnableDemo r1 = new RunnableDemo("thread-1");
        r1.start();

        RunnableDemo r2 = new RunnableDemo("thread-2");
        r2.start();
    }
}
