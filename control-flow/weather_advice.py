def main():
    # Prompt the User for Weather Input
    weather = input("What's the weather like today? (Sunny/Rainy/Cold): ").strip().lower()

    if weather == 'sunny':
        print("Wear a t-shirt and sunglasses.")
    elif weather == 'rainy':
        print("Don't forget your umbrella and raincoat.")
    elif weather == 'cold':
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry I don't have a recomendations for this weather.")

if __name__ == "__main__":
    main()

