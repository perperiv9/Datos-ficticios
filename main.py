from faker import Faker
import random

# Creamos o obxecto que xerará os datos ficticios.
falser = Faker("es_ES")

# No dicionario gardaranse os usuarios.
users = {}

#Xerar os usuarios ficticios cos métodos que ofrece faker
for codigo in range(1, 16):
    users[codigo] = {
        "nome": falser.name(),
        "direccion": falser.address(),
        "correo": falser.email(),
        "telefono": falser.phone_number()
    }

# Aquí recórrense os novos usuarios e imprímense os seus datos
for codigo, datos in users.items():
    print(f"\nCódigo: {codigo}")
    print(f"Nome: {datos['nome']}")
    print(f"Dirección: {datos['direccion']}")
    print(f"Correo electrónico: {datos['correo']}")
    print(f"Teléfono: {datos['telefono']}")

# Selección aleatoria do código afortunado utilizando random
codigoAfortunado = random.choice(list(users.keys()))

# Obter o nome do usuario seleccionado
nomeAfortunado = users[codigoAfortunado]["nome"]

# Mensaxe final co usuario gañador
print(f"\nO usuario chamado {nomeAfortunado} foi o afortunado!")
