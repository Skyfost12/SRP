class Auto {
    void moverse() {
        System.out.println("El auto se mueve sobre ruedas.");
    }
}

class Bicicleta {
    void moverse() {
        System.out.println("La bicicleta se mueve con pedales.");
    }
}

class VehiculoManager {
    void iniciarMovimiento(Object vehiculo) {
        if (vehiculo instanceof Auto) {
            ((Auto) vehiculo).moverse();
        } else if (vehiculo instanceof Bicicleta) {
            ((Bicicleta) vehiculo).moverse();
        } else {
            System.out.println("Tipo de vehículo desconocido.");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        VehiculoManager manager = new VehiculoManager();
        
        Auto auto = new Auto();
        Bicicleta bicicleta = new Bicicleta();

        manager.iniciarMovimiento(auto);      
        manager.iniciarMovimiento(bicicleta); 
    }
}