//Clase Factura
class Factura {
    constructor(public numero: string, public total: number) {}
}

//Clase que de administrar la factura
class FacturaFactory {
    crearFactura(numero: string, total: number): Factura {
      return new Factura(numero, total);
    }
}

//Clase Pedido: El pedido recive la facturaFactory a travez de dependencias
class Pedido {
    constructor(private facturaFactory: FacturaFactory) {}
  
    generarFactura(): Factura {
      return this.facturaFactory.crearFactura("F001", 20000);
    }
}

//Prueba
const facturaFactory = new FacturaFactory();
const pedido = new Pedido(facturaFactory);
const factura = pedido.generarFactura();

console.log(`Factura generada: Número ${factura.numero}, Total: ${factura.total}`); // Factura generada: Número F001, Total: 20000