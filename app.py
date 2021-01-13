from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.library import Library
from exchange_api.api import ExchangeApi

CREATE_CART_ENDPOINT = "https://market.feedbooks.com/carts.json"

if __name__ == "__main__":
    engine = create_engine('postgresql+psycopg2://user:test@localhost:5434/dpla_exchange_cart_api')
    Session = sessionmaker(bind=engine)
    session = Session()
    lib = session.query(Library).one()
    for cart in lib.carts:
        print(cart.name)

    exchange = ExchangeApi(lib.lib_id, lib.credential, CREATE_CART_ENDPOINT)
    exchange.create_cart("test cart api-4-api")

