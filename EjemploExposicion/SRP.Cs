// Incorrecto
using System;
using System.Collections.Generic;

class Order
{
    private List<string> items;
    private List<double> prices;
    private double taxRate;

    public Order(List<string> items, List<double> prices, double taxRate)
    {
        this.items = items;
        this.prices = prices;
        this.taxRate = taxRate;
    }

    public double CalculateTotal()
    {
        double total = 0;
        foreach (var price in prices)
        {
            total += price;
        }
        double discount = 5;
        double tax = (total - discount) * taxRate;
        return total - discount + tax;
    }

    public string GenerateInvoice()
    {
        double total = CalculateTotal();
        var invoice = new System.Text.StringBuilder("Factura:\n");
        for (int i = 0; i < items.Count; i++)
        {
            invoice.AppendLine($"{items[i]}: ${prices[i]}");
        }
        invoice.AppendLine($"Total (incluyendo impuestos): ${total}");
        return invoice.ToString();
    }

    public void SendConfirmationEmail(string email)
    {
        string invoice = GenerateInvoice();
        Console.WriteLine($"Enviando email a {email} con la siguiente Factura:\n{invoice}");
    }

    public double ApplyDiscount(double discount)
    {
        double total = 0;
        foreach (var price in prices)
        {
            total += price;
        }
        total -= discount;
        return total > 0 ? total : 0;
    }

    public static void Main(string[] args)
    {
        var items = new List<string> { "Libro", "Lapicero" };
        var prices = new List<double> { 12.99, 0.99 };
        var order = new Order(items, prices, 0.1);
        Console.WriteLine(order.CalculateTotal());
        Console.WriteLine(order.GenerateInvoice());
        order.SendConfirmationEmail("customer@example.com");
    }
}


// Correcto
using System;
using System.Collections.Generic;

class Order
{
    public List<Tuple<string, double>> Items { get; set; }

    public Order(List<Tuple<string, double>> items)
    {
        Items = items;
    }

    public double GetSubtotal()
    {
        double subtotal = 0;
        foreach (var item in Items)
        {
            subtotal += item.Item2;
        }
        return subtotal;
    }
}

class TaxCalculator
{
    public double CalculateTax(double subtotal, double taxRate)
    {
        return subtotal * taxRate;
    }
}

class DiscountManager
{
    public double ApplyDiscount(double subtotal, double discount)
    {
        double total = subtotal - discount;
        return total > 0 ? total : 0;
    }
}

class InvoiceGenerator
{
    public string GenerateInvoice(Order order, double subtotal, double tax, double total)
    {
        var invoice = "Factura:\n";
        foreach (var item in order.Items)
        {
            invoice += $"{item.Item1}: ${item.Item2}\n";
        }
        invoice += $"Subtotal: ${subtotal}\n";
        invoice += $"Impuesto: ${tax}\n";
        invoice += $"Total (incluyendo impuestos): ${total}\n";
        return invoice;
    }
}

class EmailSender
{
    public void SendEmail(string email, string content)
    {
        Console.WriteLine($"Enviando email a {email} con el siguiente contenido:\n{content}");
    }
}

class Program
{
    static void Main(string[] args)
    {
        var order = new Order(new List<Tuple<string, double>> { 
            new Tuple<string, double>("Libro", 12.99), 
            new Tuple<string, double>("Lapiz", 0.99) 
        });

        var taxCalculator = new TaxCalculator();
        var discountManager = new DiscountManager();
        var invoiceGenerator = new InvoiceGenerator();
        var emailSender = new EmailSender();

        double subtotal = order.GetSubtotal();
        double discountedTotal = discountManager.ApplyDiscount(subtotal, 5);
        double tax = taxCalculator.CalculateTax(discountedTotal, 0.1);
        double finalTotal = discountedTotal + tax;

        string invoice = invoiceGenerator.GenerateInvoice(order, subtotal, tax, finalTotal);
        emailSender.SendEmail("comprador@example.com", invoice);
    }
}
