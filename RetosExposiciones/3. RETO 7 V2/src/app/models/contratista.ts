import { Empleado } from "./empleado";

export class Contratista extends Empleado {
  facturaEnviada: boolean = false;

  constructor(id: number, nombre: string, salario: number) {
    super(id, nombre, salario);
  }

  enviarFactura(): string {

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
