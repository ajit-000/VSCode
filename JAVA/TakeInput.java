import java.util.*;

public class TakeInput {
    public static void main(String args[]) {
        try (Scanner sc = new Scanner(System.in)) {
            int a=sc.nextInt(),b=sc.nextInt();

            System.out.println(a+b);
        }

    }
}
