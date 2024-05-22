enum Color {
    Red, Green, Blue;
}

public class EnumInSwitch {
    public static void main(String[] args) {
        Color myVar = Color.Blue;
        switch(myVar) {
            case Red:
                System.out.println("红色");
                break;
            case Blue:
                System.out.println("蓝色");
                break;
            case Green:
                System.out.println("绿色");
                break;
        }
    }
}
