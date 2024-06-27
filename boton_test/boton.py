import os
from dotenv import load_dotenv

load_dotenv()  # carga las variables de entorno desde el archivo .env

access_token = os.getenv("ACCESS_TOKEN")
client_id = os.getenv("CLIENT_ID")

# print(access_token)
# print(client_id)
# SDK de Mercado Pago
import mercadopago
# Agrega credenciales
sdk = mercadopago.SDK(access_token)


# Crea un ítem en la preferencia
preference_data = {
    "items": [
        {
            "title": "Dibujo de Goku",
            "quantity": 1,
            "unit_price": 10,
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
print(preference["init_point"])

#probar tarjetas
#chequear estado solicitud


