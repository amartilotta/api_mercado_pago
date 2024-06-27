from flask import Flask, request, render_template
import mercadopago

app = Flask(__name__)


@app.route('/')
def index():
    mp = mercadopago.SDK("ACCESS_TOKEN")
    preference_data = {
        "items": [
            {
                "title": "Mi producto",
                "quantity": 1,
                "currency_id": "ARS",
                "unit_price": 100
            }
        ]
    }
    preference = mp.create_preference(preference_data)
    print(preference['id'])
    return render_template('index.html', preference_id=preference['id'])
#............................................................................
# mp = mercadopago.SDK("ACCESS_TOKEN")


# @app.route('/pagar', methods=['POST'])
# def pagar():
#     data = request.get_json()
#     preference = {
#         "items": [{
#             "title": data['producto'],
#             "quantity": 1,
#             "currency_id": "ARS",
#             "unit_price": float(data['precio'])
#         }]
#     }
#     preferenceResult = mp.create_preference(preference)
#     return preferenceResult['response']['init_point']

# if __name__ == '__main__':
#     app.run()