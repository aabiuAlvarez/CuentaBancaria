class CuentaBancaria:
    def __init__(self, titular):
        self.__titular = titular  
        self.__saldo = 0  

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"\nSe han depositado ${cantidad:.2f} MXN. Saldo actual: ${self.__saldo:.2f} MXN")
        else:
            print("\nError: La cantidad a depositar debe ser mayor que 0.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if self.__saldo >= cantidad:
                self.__saldo -= cantidad
                print(f"\nSe han retirado ${cantidad:.2f} MXN. Saldo actual: ${self.__saldo:.2f} MXN")
            else:
                print("\nError: No hay suficiente saldo para retirar esa cantidad.")
        else:
            print("\nError: La cantidad a retirar debe ser mayor que 0.")

    def mostrar_saldo(self):
        print(f"\n{self.__titular}, tu saldo actual es: ${self.__saldo:.2f} MXN")

   
    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    
    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("Error: El saldo no puede ser negativo.")



def mostrar_menu():
    print("\n--- Menú de la Cuenta Bancaria ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Ver saldo")
    print("4. Salir")



def main():
    
    titular = input("Ingresa el nombre del titular de la cuenta: ")
    cuenta = CuentaBancaria(titular)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            cantidad = float(input("Ingresa la cantidad a depositar en MXN: "))
            cuenta.depositar(cantidad)
        elif opcion == '2':
            cantidad = float(input("Ingresa la cantidad a retirar en MXN: "))
            cuenta.retirar(cantidad)
        elif opcion == '3':
            cuenta.mostrar_saldo()
        elif opcion == '4':
            print(f"\nGracias por usar la cuenta bancaria, {cuenta.get_titular()}. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 4.")



if __name__ == "__main__":
    main()