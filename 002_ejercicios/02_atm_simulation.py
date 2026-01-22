import asyncio


# Exceociones personalizadas. 

class ATMError(Exception):
    """Clase base para errores del cajero."""
    pass


class AuthError(ATMError):
    """Error de contraseña o identidad."""
    pass


class InsufficientFundsError(ATMError):
    """Error de fondos insuficientes."""
    pass


# Clases de Dominio.
class User:
    def __init__(self, user_id: str, pin: str, balance: float, is_activate: bool = True):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.is_activate = is_activate


class ATM:
    def __init__(self, cash_available: float):
        self.cash_available = cash_available # Dinero Fisico en el cajero

    async def validate_identity(self, user: User)
        print("[1] Validando identidad y estado del usuario")
        await asyncio.sleep(1)  # Simula tiempo de espera
        if not user.is_activate:
            raise AuthError("Usuario inactivo.")
        print("[1] Identidad validada.")
        
    async def authenticate(self, user: User, input_pin:str):
        print("[2] Validando contraseña")
        await asyncio.sleep(2)
        if user.pin != input_pin:
            raise AuthError("PIN incorrecto.")
        
    async def check_balance(self, user: User, amount:float):
        print(f"[3, 5] Validando saldo en cuenta para el monto de {amount}")
        await asyncio.sleep(2)
        if amount > user.balance:
            raise InsufficientFundsError("Fondos insuficientes en la cuenta.")
        print("Saldo disponible en la cuenta")
        
    async def validate_atm_cash(self, amount: float):
        print("[4] Validando disponibilidad de efectivo.")
        await asyncio.sleep(2)
        if amount > self.cash_available:
            raise ATMError("Cajero sin efectivo suficiente para atender la solicitud.")
        print("Efectivo disponible.")
        
    async def withdraw_process(self, user: User, amount: float, pin: str):
        try:
            #Flujo de ejecuión asincrono. 
            await self.validate_identity(user)
            await self.authenticate(user, pin)
            await self.check_balance(user, amount)
            await self.validate_atm_cash(amount)
            
            # Aprobación final. 
            print("\n------ Procesando trx ----")
            await asyncio.sleep(2)
            user.balance -= amount
            self.cash_available -= amount
            print(f"Retiro exitoso de {amount}. Nuevo saldo: {user.balance}")
            
        except ATMError as e:
            print(f"Error en la transacción: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Ejecución del programa: 
async def main()
    cajero = ATM(cash_available=5000.0)
    usuario_prueba = User(user_id="U001", pin="1234", balance=3000.0, is_activate=True)

    monto_a_retirar = 200.0
    await cajero.withdraw_process(usuario_prueba, monto_a_retirar, pin="1234")

if __name__ == "__main__":
    asyncio.run(main())