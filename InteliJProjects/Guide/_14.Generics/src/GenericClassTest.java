public class GenericClassTest {
    public static class Box<T> {
        private T t;

        public void add(T t) {
            this.t = t;
        }

        public T get() {
            return this.t;
        }
    }

    public static void main(String[] args) {
        Box<Integer> integerBox = new Box<>();
        integerBox.add(145);

        Box<String> stringBox = new Box<>();
        stringBox.add("wxss");

        System.out.println(integerBox.get());
        System.out.println(stringBox.get());


    }

}
