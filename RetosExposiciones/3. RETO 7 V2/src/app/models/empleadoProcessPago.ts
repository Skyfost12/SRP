import { Empleado } from "./empleado";

export class empleadoProcessPago extends Empleado {
  constructor(id: number, nombre: string, salario: number) {
    super(id, nombre, salario);
  }

  procesarPago(): string {
    const salarioNeto = this.salario - this.calcularImpuestos();
    return `Pago procesado: ${this.nombre} ha recibido $${salarioNeto} después de impuestos.`;
  }

}