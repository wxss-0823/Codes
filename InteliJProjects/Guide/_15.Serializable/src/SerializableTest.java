import java.io.*;

public class SerializableTest {
    public static class MyClass implements Serializable{
        private final String className;

        MyClass (String name) {
            this.className = name;
        }

        String get() {
            return this.className;
        }
    }

    public static void main(String[] args) {
        MyClass math = new MyClass("Mathematica");
        String path = "./_15.Serializable/src/obj.ser";
        try {
            // 写入对象流
            FileOutputStream fileOut = new FileOutputStream(path);
            ObjectOutputStream objOut = new ObjectOutputStream(fileOut);
            objOut.writeObject(math);
            objOut.close();
            fileOut.close();

            // 读取对象流
            FileInputStream fileIn = new FileInputStream(path);
            ObjectInputStream objIn = new ObjectInputStream(fileIn);
            MyClass objEmpty =  (MyClass) objIn.readObject();
            objIn.close();
            fileIn.close();

            System.out.println("objEmpty.get() = " + objEmpty.get());
        } catch (IOException | ClassNotFoundException e) {
            System.out.printf(e.toString());
        }
    }
}
