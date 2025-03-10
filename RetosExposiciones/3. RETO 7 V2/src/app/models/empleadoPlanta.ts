import { empleadoProcessPago } from "./empleadoProcessPago";

export class EmpleadoPlanta extends empleadoProcessPago {
  constructor(id: number, nombre: string, salario: number) {
    super(id, nombre, salario);
  }

  override procesarPago(): string {
    const salarioNeto = this.salario - this.calcularImpuestos();
    return `Pago procesado: ${this.nombre} ha recibido $${salarioNeto} después de impuestos.`;
  }

  override calcularImpuestos(): number {
    return this.salario * 0.15;
  }
}
