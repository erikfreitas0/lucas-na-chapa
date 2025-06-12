cardapio = {
    1: {"nome": "Xis Salada", "preco": 28.00},
    2: {"nome": "Xis Burger", "preco": 28.00},
    3: {"nome": "Xis Mignon", "preco": 37.00},
    4: {"nome": "Xis Kamikase", "preco": 42.00},
    5: {"nome": "Xis Bacon", "preco": 35.00},
    6: {"nome": "Xis do Dani", "preco": 41.00},
    7: {"nome": "Xis Camarão", "preco": 44.00},
    8: {"nome": "Xis Calabresa", "preco": 31.00},
    9: {"nome": "Xis Frango", "preco": 31.00},
    10: {"nome": "Xis Costela", "preco": 36.00},
    11: {"nome": "Xis Coração", "preco": 31.00},
    12: {"nome": "Xis Alcatra", "preco": 36.00},
    13: {"nome": "Super Costela", "preco": 41.00},
    14: {"nome": "Xis da Casa", "preco": 43.00},
    15: {"nome": "Misto Quente", "preco": 24.00},
    16: {"nome": "Queijo Quente", "preco": 24.00},
    17: {"nome": "Xis Fiora", "preco": 42.00},
    18: {"nome": "Xis Dog", "preco": 28.00},
    19: {"nome": "Xis Picanha", "preco": 42.00},
    20: {"nome": "Xis Lucão", "preco": 36.00},
    21: {"nome": "Xis Americano", "preco": 40.00},
    22: {"nome": "Xis Alcatra Especial", "preco": 56.00},
    23: {"nome": "Xis Especial da Casa", "preco": 69.00},
    24: {"nome": "Xis Chico Salad", "preco": 35.00},
    25: {"nome": "Xis Mignon Especial", "preco": 56.00},
    26: {"nome": "Xis Frango Especial", "preco": 56.00},
    27: {"nome": "Xis Vegetariano", "preco": 29.00}
}

def mostrar_cardapio():
    print("--- CARDÁPIO ---")
    for codigo, item in cardapio.items():
        print(f"{codigo} - {item['nome']} - R${item['preco']}")
        
        
