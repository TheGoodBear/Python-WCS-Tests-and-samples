# coding: utf-8

# imports modules
import requests


def Main():
    """
        Main function
    """

    MinProductsInCategory = 10
    MaxProductsInCategory = 20
    Categories = []
    Products = []

    print("\nDémo d'API Open Food Facts")
    print("--------------------------")
    
    print(f"\nRécupération des catégories contenant entre {MinProductsInCategory} et {MaxProductsInCategory} produits.")

    print("\nInterrogation de l'API...")
    Response = requests.get("https://fr.openfoodfacts.org/categories.json")
    Results = Response.json()

    print(f"\n{Results['count']} catégories ont été récupérées.")
    input("Appuyer sur Entrée pour démarrer le filtrage...")

    for Item in Results["tags"]:
        if MinProductsInCategory <= Item["products"] <= MaxProductsInCategory:
            Categories.append((Item["name"], Item["url"], Item["products"]))
            print(f"Récupération de la catégorie {Item['name']} contenant {Item['products']} produits")

    print(f"\nAprès filtrage, {len(Categories)} catégories ont été récupérées.")
    print(f"\nRécupération des produits de chaque catégorie.")
    input("Appuyer sur Entrée pour démarrer la récupération...")

    CategoryNumber = 0
    MaxCategories = 30
    for Category in Categories:
        print(f"\nRécupération des {Category[2]} produits de la catégorie {Category[0]}")
        ProductsInCategory = []
        PageNumber = 0
        NextPage = True
        
        while NextPage:
            PageNumber += 1
            Response = requests.get(f"{Category[1]}.json/{PageNumber}")
            Results = Response.json()
            # if len(Results["products"]) == 0:
            #     NextPage = False
            NextPage = False if len(Results["products"]) == 0 else True
            for Item in Results["products"]:

                try:
                    if (Item["product_name_fr"].strip() != ""
                        and len(Item["brands"]) > 0
                        and Item["nutriscore_grade"].strip() != ""):
                        ProductsInCategory.append((Item["product_name_fr"], Item["brands"], Item["nutriscore_grade"].upper()))
                        print(f"Récupération du produit {Item['product_name_fr']} de marque {Item['brands'][0]} ayant le nutriscore {Item['nutriscore_grade'].upper()}")
                except:
                    pass

        if len(ProductsInCategory) > 0:
            CategoryNumber += 1
            Products.append({Category[0] : ProductsInCategory})
        else:
            print(f"Suppression de la catégorie {Category[0]}")
            Categories.remove(Category)

        if CategoryNumber == MaxCategories:
            break

    print("\nTraitement terminé.\n")


# Program entry point
if __name__ == "__main__":
    Main()