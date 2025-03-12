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

    //Procesa el pedido
    public void processOrder(double amount, String payment_method) {
        paymentService = PaymentFactory.create_payment_method(payment_method);
        if(paymentService != null){
            System.err.println("Orden Procesada");
        }else{
            System.err.println("Error");
        }
    }
}

class PaymentFactory{   
    public static PaymentService create_payment_method(String payment_method){
        if(payment_method == "TarjetaCredito"){
            return new CreditCardPaymentService();
        }else{
            if (payment_method == "Paypal") {
                return new PayPalPaymentService();
            }else{
                if (payment_method == "GooglePlay") {
                    return new GooglePayPaymentService();
                }else{
                    return null;
                }
            }
        }
    }

}


//Prueba
public class SolucionFactory {
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

        String paymentService = "";

        
        switch (opcion) {
            case 1:
                paymentService = "TarjetaCredito";
                break;
            case 2:
                paymentService = "Paypal";
                break;
            case 3:
                paymentService = "GooglePlay";
                break;
            default:
                System.out.println("Opción inválida");
                break;
        }

        
        //Procesa el pago
        OrderService orderService = new OrderService();
        orderService.processOrder(amount,paymentService);
        
        scanner.close();
    }
}