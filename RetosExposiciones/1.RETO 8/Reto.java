// Reto Alto Acoplamiento
/* 
//Clase que representa el servicio de pago con tarjeta de crédito
class CreditCardPaymentService {
    public void processPayment(double amount) {
        System.out.println("Processing credit card payment of: " + amount);
    }
}

// Clase que representa el servicio de gestión de pedidos
class OrderService {
    private CreditCardPaymentService paymentService; // ALTO ACOPLAMIENTO

    public OrderService() {
        this.paymentService = new CreditCardPaymentService(); // Dependencia directa
    }

    public void processOrder(double amount) {
        // Procesa el pago usando el servicio de pago con tarjeta de crédito
        paymentService.processPayment(amount);
        System.out.println("Order processed successfully!");
    }
}*/