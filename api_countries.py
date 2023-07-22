import requests

def nombre_paises (url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
        print('----------------------------------------------')
        print(f"Nombre Oficial: {pais['name']['official']}")
        print(f"Nombre Común: {pais['name']['common']}")
        print(f"Capital: {pais['capital'][0]}")
        cod = (f"{pais['idd']['root']}")
        cod2 = (f"{pais['idd']['suffixes'][0]}")
        print(f"Nombre Común:{cod+cod2}")
        moneda = pais.get("currencies", {})
        moneda_names = [f"{nombre.get('name', '')} → {nombre.get('symbol', '')}"for nombre in moneda.values()]
        print(f"Moneda:{(moneda_names)[0]}")

url = 'https://restcountries.com/v3.1/independent?status=true&fields=capital,name,currencies,idd'
nombre_paises(url)
