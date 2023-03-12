import java.util.*;

public class ConditionalState {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            String opr = sc.nextLine();
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();
            switch (opr) {
                case "+":
                    System.out.println(num1 + num2);
                    break;
                case "-":
                    System.out.println(num1 - num2);
                    break;
                case "*":
                    System.out.println(num1 * num2);
                    break;
                case "/":
                    System.out.println(num1 / num2);
                    break;
                case "%":
                    System.out.println(num1 % num2);
                    break;
                default:
                    System.out.println("Invalid Operation");
            }
        }
    }
}
