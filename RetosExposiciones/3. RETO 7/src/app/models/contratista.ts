import { Empleado } from "./empleado";

export class Contratista extends Empleado {
  facturaEnviada: boolean = false;

  constructor(id: number, nombre: string, salario: number) {
    super(id, nombre, salario);
  }

  enviarFactura(): void {
    this.facturaEnviada = true;
  }

  procesarPago(): string {
    //Utilizar la factura para "Asignar" la factura y ya el area correspondiente se encargará de procesarla
    if (!this.facturaEnviada) {
      this.enviarFactura();
      return `Factura enviada por el contratista ${this.nombre} con un salario de ${this.salario}.`;
    }
    return `La factura ya fue enviada por el contratista ${this.nombre}.`;
  }

  override calcularImpuestos(): number {
    return this.salario * 0.05;
  }
}
