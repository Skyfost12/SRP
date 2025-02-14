// Incorrecto
class Order {
    constructor(items, prices, taxRate) {
        this.items = items;
        this.prices = prices;
        this.taxRate = taxRate;
    }

    calculateTotal() {
        let total = 0;
        for (let price of this.prices) {
            total += price;
        }
        const discount = 5;
        const tax = (total - discount) * this.taxRate;
        return total - discount + tax;
    }

    generateInvoice() {
        const total = this.calculateTotal();
        let invoice = "Factura:\n";
        for (let i = 0; i < this.items.length; i++) {
            invoice += `${this.items[i]}: $${this.prices[i]}\n`;
        }
        invoice += `Total (incluyendo impuestos): $${total}\n`;
        return invoice;
    }

    sendConfirmationEmail(email) {
        const invoice = this.generateInvoice();
        console.log(`Enviando email a ${email} con la siguiente Factura:\n${invoice}`);
    }

    applyDiscount(discount) {
        let total = 0;
        for (let price of this.prices) {
            total += price;
        }
        total -= discount;
        return total > 0 ? total : 0;
    }
}

// Ejemplo de uso
class Order {
    constructor(items) {
        this.items = items;
    }

    getSubtotal() {
        return this.items.reduce((subtotal, [item, price]) => subtotal + price, 0);
    }
}

class TaxCalculator {
    calculateTax(subtotal, taxRate) {
        return subtotal * taxRate;
    }
}

class DiscountManager {
    applyDiscount(subtotal, discount) {
        const total = subtotal - discount;
        return total > 0 ? total : 0;
    }
}

class InvoiceGenerator {
    generateInvoice(order, subtotal, tax, total) {
        let invoice = "Factura:\n";
        for (const [item, price] of order.items) {
            invoice += `${item}: $${price}\n`;
        }
        invoice += `Subtotal: $${subtotal}\n`;
        invoice += `Impuesto: $${tax}\n`;
        invoice += `Total (incluyendo impuestos): $${total}\n`;
        return invoice;
    }
}

class EmailSender {
    sendEmail(email, content) {
        console.log(`Enviando email a ${email} con el siguiente contenido:\n${content}`);
    }
}

// Ejemplo de uso
const order = new Order([["Libro", 12.99], ["Lapiz", 0.99]]);
const taxCalculator = new TaxCalculator();
const discountManager = new DiscountManager();
const invoiceGenerator = new InvoiceGenerator();
const emailSender = new EmailSender();

const subtotal = order.getSubtotal();
const discountedTotal = discountManager.applyDiscount(subtotal, 5);
const tax = taxCalculator.calculateTax(discountedTotal, 0.1);
const finalTotal = discountedTotal + tax;

const invoice = invoiceGenerator.generateInvoice(order, subtotal, tax, finalTotal);
emailSender.sendEmail("comprador@example.com", invoice);
