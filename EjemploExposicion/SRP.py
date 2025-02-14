# Incorrecto
class Order:
    def __init__(self, Items, TaxRate):
        self.Items = Items 
        self.TaxRate = TaxRate
    
    def CalculateTotal(self):
        Total = sum(Price for Item, Price in self.Items)
        Discount = 5  
        Tax = (Total - Discount) * self.TaxRate
        return Total - Discount + Tax
    
    def GenerateInvoice(self):
        Total = self.CalculateTotal()
        Invoice = "Factura:\n"
        for Item, Price in self.Items:
            Invoice += f"{Item}: ${Price}\n"
        Invoice += f"Total (incluyendo impuestos): ${Total}\n"
        return Invoice
    
    def SendConfirmationEmail(self, Email):
        Invoice = self.GenerateInvoice()
        print(f"Enviando email a {Email} con la siguiente Factura:\n{Invoice}")
    
    def ApplyDiscount(self, Discount):
        Total = sum(Price for Item, Price in self.Items) - Discount
        return Total if Total > 0 else 0 


OrderInstance = Order([("Libro", 12.99), ("Lapicero", 0.99)], 0.1)
print(OrderInstance.CalculateTotal())
print(OrderInstance.GenerateInvoice())
OrderInstance.SendConfirmationEmail("customer@example.com")


# Correcto
class Order:
    def __init__(self, Items):
        self.Items = Items
    
    def GetSubtotal(self):
        return sum(Price for _, Price in self.Items)

class TaxCalculator:
    def CalculateTax(self, Subtotal, TaxRate):
        return Subtotal * TaxRate

class DiscountManager:
    def ApplyDiscount(self, Subtotal, Discount):
        Total = Subtotal - Discount
        return Total if Total > 0 else 0

class InvoiceGenerator:
    def GenerateInvoice(self, Order, Subtotal, Tax, Total):
        Invoice = "Factura:\n"
        for Item, Price in Order.Items:
            Invoice += f"{Item}: ${Price}\n"
        Invoice += f"Subtotal: ${Subtotal}\n"
        Invoice += f"Impuesto: ${Tax}\n"
        Invoice += f"Total (incluyendo impuestos): ${Total}\n"
        return Invoice

class EmailSender:
    def SendEmail(self, Email, Content):
        print(f"Enviando email a {Email} con el siguiente contenido:\n{Content}")


OrderInstance = Order([("Libro", 12.99), ("Lapiz", 0.99)])
TaxCalculatorInstance = TaxCalculator()
DiscountManagerInstance = DiscountManager()
InvoiceGeneratorInstance = InvoiceGenerator()
EmailSenderInstance = EmailSender()

Subtotal = OrderInstance.GetSubtotal()
DiscountedTotal = DiscountManagerInstance.ApplyDiscount(Subtotal, 5)
Tax = TaxCalculatorInstance.CalculateTax(DiscountedTotal, 0.1)
FinalTotal = DiscountedTotal + Tax

Factura = InvoiceGeneratorInstance.GenerateInvoice(OrderInstance, Subtotal, Tax, FinalTotal)
EmailSenderInstance.SendEmail("comprador@example.com", Factura)
