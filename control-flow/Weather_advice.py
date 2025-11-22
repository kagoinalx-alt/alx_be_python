weather = input("What's the weather like today? (sunny/rainy/cold)").title()

if weather == "Sunny":
    print("Recommended: Wear a t-shirt and sunglasses.")
elif weather == "Rainy":
    print("Recommended: Don't forget your umbrella and a raincoat.")
elif weather == "Cold":
    print("Recommended: Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
