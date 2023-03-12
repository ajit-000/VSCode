import java.util.*;

public class Assignment {
    public static void main(String args[]) {
        boolean again = false;
        while (!again) {
            Scanner sc = new Scanner(System.in);
            Float topaid;
            System.out.print("-model\t");
            String model = sc.nextLine();
            System.out.print("-type\t");
            String type = sc.nextLine();
            System.out.print("-InsuranceType\t");
            String insuranceType = sc.nextLine();
            System.out.print("-price\t");
            int price = sc.nextInt();
            if (type.equals("Hatchback")) {
                Float per = 0.05f;
                if (insuranceType.equals("Basic")) {
                    topaid = per * price;
                } else {
                    topaid = (per * price) + (0.02f * price);
                }
                System.out.println("You have to pay " + topaid + " for " + insuranceType + " insurance");
            }
            System.out.println("Enter another detail y/n");
            char op = sc.next().charAt(0);
            if (op == 'n') {
                again = true;
            }
        }
    }
}
