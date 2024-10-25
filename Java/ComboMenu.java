import java.util.Scanner;

public class comboMenu {
    

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double grandTotal = 0;

        while (true) {
            double subtotal = 0;
            String sandwich = null;
            String fries = null;
            String drink = null;
            int ketchupPackets = 0;
            double sandwichPrice = 0.0;
            double fryPrice = 0.0;
            double drinkPrice = 0.0;
            boolean discount = false;

            // Sandwich
            System.out.println("Would you like a sandwich? (tofu: $5.75, chicken: $5.25, beef: $6.25)");
            String sandwichChoice = scanner.nextLine().toLowerCase();
            if (sandwichChoice.equals("tofu")) {
                subtotal += 5.75;
                sandwich = "tofu";
                sandwichPrice = 5.75;
            } 
            else if (sandwichChoice.equals("chicken")) {
                subtotal += 5.25;
                sandwich = "chicken";
                sandwichPrice = 5.25;
            } 
            else if (sandwichChoice.equals("beef")) {
                subtotal += 6.25;
                sandwich = "beef";
                sandwichPrice = 6.25;
            }

            // Fries
            System.out.println("Would you like fries? (small: $1, medium: $1.75, large: $2.25)");
            String friesChoice = scanner.nextLine().toLowerCase();
            if (friesChoice.equals("small")) {
                subtotal += 1.00;
                fries = "small";
                fryPrice = 1.00;
            } 
            else if (friesChoice.equals("medium")) {
                subtotal += 1.75;
                fries = "medium";
                fryPrice = 1.75;
            } 
            else if (friesChoice.equals("large")) {
                subtotal += 2.25;
                fries = "large";
                fryPrice = 2.25;
            }

            // Drink
            System.out.println("Would you like a drink? (small: $1, medium: $1.50, large: $2.00)");
            String drinkChoice = scanner.nextLine().toLowerCase();
            if (drinkChoice.equals("small")) {
                subtotal += 1.00;
                drink = "small";
                drinkPrice = 1.00;
            } 
            else if (drinkChoice.equals("medium")) {
                subtotal += 1.50;
                drink = "medium";
                drinkPrice = 1.50;
            } 
            else if (drinkChoice.equals("large")) {
                subtotal += 2.00;
                drink = "large";
                drinkPrice = 2.00;
                System.out.println("Would you like to upgrade to a child size for $0.38 more? (yes/no)");
                if (scanner.nextLine().equalsIgnoreCase("yes")) {
                    subtotal += 0.38;
                }
            }

            // Ketchup
            if (sandwich != null || fries != null || drink != null) {
                ketchupPackets = (int)getPositiveDouble(scanner, "How many ketchup packets would you like? ($0.25 each) ");
                subtotal += ketchupPackets * 0.25;
            }

            // Discount
            if (sandwich != null && fries != null && drink != null) {
                subtotal -= 1.00;
                discount = true;
            }

            // Calculate
            double tax = subtotal * 0.07;
            double total = subtotal + tax;
            
            // Print Order
            System.out.println("\nYour Order Summary:");
            if (sandwich != null) {
                System.out.println("  Sandwich: "+sandwich+" - "+formatCurrency(sandwichPrice));
            }
            if (fries != null) {
                System.out.println("  Fries: "+fries+" - "+formatCurrency(fryPrice));
            }
            if (drink != null) {
                System.out.println("  Drink: "+drink+" - " +formatCurrency(drinkPrice));
            }
            System.out.println("  Ketchup: "+ketchupPackets+" packets - "+formatCurrency(ketchupPackets * 0.25));
            if (discount) {
                System.out.println("  Discount Applied: -$1.00");
            }
            System.out.println("  Subtotal: "+formatCurrency(subtotal));
            System.out.println("  Tax: "+formatCurrency(tax));
            System.out.println("  Total: "+formatCurrency(total)+"\n");
            
            grandTotal += total;

            System.out.println("Would you like to place another order? (yes/no)");
            if (!scanner.nextLine().equalsIgnoreCase("yes")) {
                break;
            }
        }

        System.out.println("Grand Total for all orders: "+formatCurrency(grandTotal));
        scanner.close();
    }


    private static double getPositiveDouble(Scanner scanner, String prompt) {
        double value;
        while (true) {
            System.out.print(prompt);
            try {                                                   //https://www.w3schools.com/java/java_try_catch.asp & https://www.geeksforgeeks.org/numberformatexception-in-java-with-examples/ 
                value = Double.parseDouble(scanner.nextLine());
                if (value >= 0) {
                    return value;
                } 
                else {
                    System.out.println("Please enter a positive number.");
                }
            } 
            catch (NumberFormatException e) {
                System.out.println("Please enter a number.");
            }
        }
    }


    private static String formatCurrency(double amount) {
        return String.format("$%.2f", amount);
    }


}