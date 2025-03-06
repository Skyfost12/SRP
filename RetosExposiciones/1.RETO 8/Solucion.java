import java.util.Scanner;
            /* Diseño Pagos */

//Interfaz de servicio de pago
interface PaymentService {
    void processPayment(double amount);
}

/* METODOS DE PAGOS */

//Pago con tarjeta de crédito
class CreditCardPaymentService implements PaymentService {
    public void processPayment(double amount) {
        System.out.println("Processing credit card payment of: " + amount);
    }
}

//Pago con PayPal
class PayPalPaymentService implements PaymentService {
    public void processPayment(double amount) {
        System.out.println("Processing PayPal payment of: " + amount);
    }
}

//Pago con Google Pay
class GooglePayPaymentService implements PaymentService {
    public void processPayment(double amount) {
        System.out.println("Processing Google Pay payment of: " + amount);
    }
}


                /* Diseño Pedidos */
//Gestion de pedidos
class OrderService {
    private PaymentService paymentService;

    //Dependencia hacia el servicio de pago
    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService; // Dependencia inyectada por constructor
    }

    //Procesa el pedido
    public void processOrder(double amount) {
        paymentService.processPayment(amount);
        System.out.println("Order processed successfully!");
    }
}

//Prueba
public class Solucion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //Menu para simular sistema de pago
        System.out.println("Seleccione el método de pago:");
        System.out.println("1. Tarjeta de Crédito");
        System.out.println("2. PayPal");
        System.out.println("3. Google Pay");
        System.out.print("Opción: ");
        int opcion = scanner.nextInt();

        //Valor a pagar
        System.out.print("Ingrese el monto a pagar: ");
        double amount = scanner.nextDouble();

        PaymentService paymentService = null;

        
        switch (opcion) {
            case 1:
                paymentService = new CreditCardPaymentService();
                break;
            case 2:
                paymentService = new PayPalPaymentService();
                break;
            case 3:
                paymentService = new GooglePayPaymentService();
                break;
            default:
                System.out.println("Opción inválida");
                break;
        }

        
        //Procesa el pago
        OrderService orderService = new OrderService(paymentService);
        orderService.processOrder(amount);
        
        scanner.close();
    }
}