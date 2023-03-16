class CuentaJoven(Cuenta):
    
    bonificacion = 0.10

    def __init__(self, titular=None, balance=0):
        super().__init__(titular, balance)
        self.tipo = "Joven"
        if usuario is None:
            raise ValueError('La cuenta debe estar asociada a un usuario')

    def __str__(self):
        return f"\n Tipo: {self.tipo}\n Bonificación: {self.bonificacion*100}%"

    def retirar(self):
        return self.titular.mayor_edad() and self.titular.edad < 25
    if not usuario.mayor_edad():
            raise ValueError('El titular de una cuenta joven debe ser mayor de edad')
    if usuario.edad >= 25:
            raise ValueError('El titular de una cuenta joven debe tener menos de 25 años')

    def depositar(self, cantidad):
        super().depositar(cantidad + cantidad*self.bonificacion)
        
        cuenta = CuentaJoven(usuario, balance)
        self.cuentas.append(cuenta)
        return cuenta