class FacturaBad {
  constructor(numero: string, total: number) {}
}

class PedidoBad {
  crearFactura(): FacturaBad {
    return new FacturaBad("F001", 20000);
  }
}