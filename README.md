# CSA2001
# 🚲 Bike Price Predictor

## 📌 Overview

This project is a Bike Price Prediction System that tries to estimate the resale value of a bike using some basic details like age, kilometers driven, engine power and brand.

The main idea is to give a simple data based way to guess bike prices, since most of the time people just rely on guess or random opinions.

---
❓ Why I Made This

So basically, high end bikes are expensive and not everyone can afford them, specially students. Because of this, many people go for second hand bikes.

I also faced this problem personally when I was trying to buy a bike. It was honestly confusing to decide if the price was correct or not. Some bikes looked cheap but had issues, some looked costly but maybe worth it, so there was no clear idea.

That is why I thought of building something that can at least give an approx idea of price.

---

⚙️ How It Works

The program does few simple steps

It loads the dataset from a csv file
Then it cleans the data (removes missing values)
Then converts brand names into numbers (not the best way maybe, but works)
After that it normalizes the values between 0 and 1

Then a Linear Regression model is trained using a formula (normal equation).

Finally, it takes user input and predicts the bike price

---

🧠 Tech Used

Python
NumPy
Pandas
Matplotlib (not really used much right now, maybe later)

---

📂 Project Structure

project-folder/

bikes.csv → dataset file
code.py → main code
README.md → this file

---

🚀 Setup

1. Download Code

---

2. Install dependancies

Make sure python is installed first

pip install pandas numpy matplotlib

---

3. Add dataset

Put the bikes.csv file inside the folder

You can find datasets from kaggle (thats what I did)

---

▶️ How to Run

Just run

python code.py

Then follow the steps shown on screen and enter the values

---

📊 Example Output

Bike: Honda
Future Age: 5.0 years
Predicted Price: ₹45,000

---

📈 Model Info

The model used is Linear Regression

It is implemented manually using maths (not using sklearn)

Metrics used
MAE (Mean Absolute Error)
R² Score

---

⚠️ Limitations

This is a basic project so it has some limitations

It does not consider bike condition
No location factor
No ownership history

Also it assumes bike runs around 8000 km per year which may not be true always

---

🔧 Future Improvements

Can add more features like condition and location
Try better models
Improve dataset
Maybe add graphs later

---

📚 What I Learned

I learned how linear regression actually works in real code (before this it was confusing)

Also learned working with csv files and how datasets are used

Learned how to find datasets from kaggle

And overall how to connect theory with actual implementation

---

🤝 Contributing

This is just a learning project, but yeah improvements are always welcome

---

📄 Note

This project is made as learning project for CSA2001 course

---

Thanks for checking this out 🙂

