import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("bikes.csv")
data = data.dropna()

brand_list = list(data["brand"].unique())
data["brand_id"] = data["brand"].apply(lambda b: brand_list.index(b))

features = data[["age", "kms_driven", "power", "brand_id"]].values
target_prices = data["price"].values

feature_min = features.min(axis=0)
feature_max = features.max(axis=0)
features = (features - feature_min) / (feature_max - feature_min)

features = np.hstack([np.ones((features.shape[0], 1)), features])

split_index = int(0.8 * len(features))
train_X, test_X = features[:split_index], features[split_index:]
train_y, test_y = target_prices[:split_index], target_prices[split_index:]

model_weights = np.linalg.pinv(train_X.T @ train_X) @ train_X.T @ train_y

predicted_prices = test_X @ model_weights

mae_error = np.mean(np.abs(test_y - predicted_prices))
residual_sum = np.sum((test_y - predicted_prices) ** 2)
total_sum = np.sum((test_y - np.mean(test_y)) ** 2)
r2_score = 1 - (residual_sum / total_sum)


def show_metrics():
    print("\n" + "="*40)
    print("MODEL PERFORMANCE")
    print("="*40)
    print(f"Mean Absolute Error : ₹{mae_error:,.0f}")
    print(f"R² Score            : {r2_score:.2f}")
    print("="*40)


def run_price_predictor():
    while True:
        print("\n" + "="*50)
        print("BIKE PRICE PREDICTOR")
        print("="*50)

        print("\nAvailable Brands:")
        print("-"*30)
        for index, brand_name in enumerate(brand_list):
            print(f"{index:2d}. {brand_name}")
        print("-"*30)

        while True:
            try:
                chosen_index = int(input("\nSelect brand number: "))
                if 0 <= chosen_index < len(brand_list):
                    selected_brand = brand_list[chosen_index]
                    break
                else:
                    print("Invalid choice.")
            except:
                print("Enter a valid number.")

        bike_age = float(input("Enter current age (years): "))
        kms_used = float(input("Enter kms driven: "))
        engine_cc = float(input("Enter engine power (cc): "))

        years_ahead = float(input("Predict after how many years? (0 = now): "))
        future_age = bike_age + years_ahead

        kms_used += years_ahead * 8000

        brand_id = brand_list.index(selected_brand)
        input_data = np.array([[future_age, kms_used, engine_cc, brand_id]])

        input_data = (input_data - feature_min) / (feature_max - feature_min)
        input_data = np.hstack([np.ones((1, 1)), input_data])

        predicted_price = input_data @ model_weights

        print("\n" + "-"*40)
        print(f"Bike: {selected_brand}")
        print(f"Future Age: {future_age:.1f} years")
        print(f"Predicted Price: ₹{predicted_price[0]:,.0f}")
        print("-"*40)

        show = input("\nDo you want to see model performance? (y/n): ").lower()
        if show == 'y':
            show_metrics()

        user_choice = input("\nDo you want to predict another bike? (y/n): ").lower()
        if user_choice != 'y':
            print("Exiting...")
            break


run_price_predictor()