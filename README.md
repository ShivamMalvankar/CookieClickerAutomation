---

# 🍪 Cookie Clicker Bot (Selenium Automation)

Automate the popular **Cookie Clicker** web game using Python and Selenium.
This bot continuously clicks the cookie and intelligently purchases upgrades to maximize cookie production.

---

## 🚀 Features

* ⚡ Auto-clicks the main cookie at high speed
* 🧠 Automatically buys the best available upgrades
* 📈 Optimizes cookie production over time
* 🔄 Runs continuously with timed upgrade checks
* 🖥️ Works directly in your browser using Selenium

---

## 🛠️ Tech Stack

* **Python 3**
* **Selenium WebDriver**
* **ChromeDriver**

---

## 📂 Project Structure

```
CookieClickerBot/
│
├── main.py              # Main automation script
├── requirements.txt     # Required dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/cookie-clicker-bot.git
cd cookie-clicker-bot
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Download ChromeDriver**

* Download from: [https://chromedriver.chromium.org/](https://chromedriver.chromium.org/)
* Make sure version matches your Chrome browser
* Add it to your system PATH or project folder

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

The bot will:

1. Open Cookie Clicker in your browser
2. Start clicking automatically
3. Periodically buy upgrades

---

## 🧠 How It Works

* Uses Selenium to locate elements on the webpage
* Continuously clicks the cookie using a loop
* Every few seconds:

  * Reads available upgrades
  * Checks affordability
  * Purchases the best option

---

## 📌 Example Logic

```python
while True:
    cookie.click()

    if time_to_check_upgrades:
        buy_best_upgrade()
```

---

## ⚠️ Disclaimer

* This project is for **educational purposes only**
* Excessive automation may affect game experience
* Use responsibly

---

## 🔮 Future Improvements

* Add GUI dashboard
* Multi-threaded clicking
* Smarter upgrade strategy (ROI-based)
* Support for other idle games

---

## 🤝 Contributing

Pull requests are welcome!
Feel free to fork this repo and improve the bot.

---

## 📧 Contact

Created by **Shivam Malvankar**
If you like this project, give it a ⭐ on GitHub!

---
