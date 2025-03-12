import { Empleado } from "./empleado";

export abstract class empleadoProcessPago extends Empleado {
  constructor(id: number, nombre: string, salario: number) {
    super(id, nombre, salario);
  }

   abstract procesarPago(): string 

}