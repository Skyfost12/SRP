public class PayPal
{
    public string Correo { get; set; }
    public string Contraseña { get; set; }
    public double Monto { get; set; }

    public PayPal(string correo, string contraseña, double monto)
    {
        Correo = correo;
        Contraseña = contraseña;
        Monto = monto;
    }
}

public class TarjetaCredito
{
    public string NumeroTarjeta { get; set; }
    public string NombreTitular { get; set; }
    public string FechaExpiracion { get; set; }
    public double Monto { get; set; }

    public TarjetaCredito(string numero, string titular, string expiracion, double monto)
    {
        NumeroTarjeta = numero;
        NombreTitular = titular;
        FechaExpiracion = expiracion;
        Monto = monto;
    }
}

public class TransferenciaBancaria
{
    public string NumeroCuenta { get; set; }
    public string Banco { get; set; }
    public double Monto { get; set; }

    public TransferenciaBancaria(string cuenta, string banco, double monto)
    {
        NumeroCuenta = cuenta;
        Banco = banco;
        Monto = monto;
    }
}

public class ProcesadorPagos
{
    public void ProcesarPago(object metodoPago)
    {
        if (metodoPago is TarjetaCredito tarjeta)
        {
            Console.WriteLine($"Procesando pago con Tarjeta de Crédito. Monto: {tarjeta.Monto}");
            Console.WriteLine($"Tarjeta: {tarjeta.NumeroTarjeta} - Titular: {tarjeta.NombreTitular}");
        }
        else if (metodoPago is PayPal paypal)
        {
            Console.WriteLine($"Procesando pago con PayPal. Monto: {paypal.Monto}");
            Console.WriteLine($"Correo asociado: {paypal.Correo}");
        }
        else if (metodoPago is TransferenciaBancaria transferencia)
        {
            Console.WriteLine($"Procesando pago con Transferencia Bancaria. Monto: {transferencia.Monto}");
            Console.WriteLine($"Cuenta: {transferencia.NumeroCuenta} - Banco: {transferencia.Banco}");
        }
        else
        {
            throw new ArgumentException("Método de pago no soportado");
        }
    }
}

class Program
{
    static void Main()
    {
        ProcesadorPagos procesador = new ProcesadorPagos();
        TarjetaCredito tarjeta = new TarjetaCredito("1234-5678-9876-5432", "Juan Pérez", "12/27", 100.50);
        PayPal paypal = new PayPal("juan.perez@example.com", "secreto123", 75.30);
        TransferenciaBancaria transferencia = new TransferenciaBancaria("0987654321", "Banco XYZ", 200.00);

        procesador.ProcesarPago(tarjeta);
        procesador.ProcesarPago(paypal);
        procesador.ProcesarPago(transferencia);
    }
}

// Si tu solución cumple con OCP, Bitcoin debería funcionar sin modificar el código ya existente.
public class Bitcoin : IMetodoPago
{
    public string Wallet { get; set; }
    public double Monto { get; set; }

    public Bitcoin(string wallet, double monto)
    {
        Wallet = wallet;
        Monto = monto;
    }

    public void Procesar()
    {
        Console.WriteLine($"Procesando pago con Bitcoin. Monto: {Monto}");
        Console.WriteLine($"Wallet: {Wallet}");
    }
}