from flask import Flask, request, jsonify 
from models import Product, create_engine, Base, sessionmaker


app = Flask(__name__)

engine = create_engine("sqlite:///duka.db", echo=True)
Base.metadata.create_all(bind=engine)

session = sessionmaker(bind=engine)
session = session()

@app.route('/')
def hello():
    hello =  jsonify({"name":"Queen"}),200
    return hello

@app.route('/products', methods=["POST","GET"])
def product():
    if request.method=="POST":
      name = request.json["name"]
      selling_price = request.json["selling_price"]
      buying_price = request.json["buying_price"]
      new_product = Product(name, selling_price, buying_price)

      session.add(new_product)
      session.commit()

      return jsonify("stored successfuly"),201

    else:
        products = session.query(Product).all()
        print (products)
        result = []
        for p in products:
            row={}
            row["name"]=p.name
            row["id"]=p.id
            row["selling_price"]=p.selling_price
            row["buying_price"]=p.buying_price
            result.append(row)
        return jsonify(result)




if __name__=='__main__':
    app.run()