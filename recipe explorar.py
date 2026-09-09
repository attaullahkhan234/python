pasta = ("pasta arrabiata", "Italian", 20, "medium")
biryani = ("chicken biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty:", pasta[-1])

all_recipes = [pasta, biryani]
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe Time:", all_recipes[1][2], "mins")
print("Pasta details (sliced):", pasta[1:3])

print("\npasta recipe details:")
for detail in pasta:
    print(" -", detail)


pasta_ingrediants = {"pasta", "tomato sauce", "garlic", "chili flakes", "olive oil"}
biryani_ingrediants = {"chicken", "rice", "spices", "yogurt", "onion"}
print("\nPasta ingrediants:", pasta_ingrediants)
print("Biryani ingrediants:", biryani_ingrediants)
print("Total pasta ingrediants:", len(pasta_ingrediants))


pasta_ingrediants.add("basil")
pasta_ingrediants.discard("garlic")
print("\nUpdated pasta ingrediants:", pasta_ingrediants)


all_ingrediants = pasta_ingrediants.union(biryani_ingrediants)
common_ingrediants = pasta_ingrediants.intersection(biryani_ingrediants)
only_pasta_ingrediants = pasta_ingrediants.difference(biryani_ingrediants)
unique_to_both = pasta_ingrediants.symmetric_difference(biryani_ingrediants)

print("\nAll ingrediants:", all_ingrediants)
print("Common ingrediants:", common_ingrediants)
print("Ingrediants only in pasta:", only_pasta_ingrediants)
print("Ingrediants unique to both recipes:", unique_to_both)
