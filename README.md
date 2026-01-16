# ♻️ Sortify

### Adaptive Household Waste Sorting & Routing Assistant

Sortify is a waste management project developed by members of **Epoch – AIML Club**.
The goal of Sortify is to simplify waste segregation, reduce contamination, and promote sustainable habits by guiding users to dispose of waste correctly using smart, localized rules.

---

## 🌍 Problem Statement

Waste segregation is one of the simplest yet most misunderstood daily activities, especially in India.
Due to unclear and inconsistent disposal rules, households often mix waste incorrectly, leading to:

* High contamination rates
* Overflowing landfills
* Wasted recyclable resources
* Environmental pollution and health risks

Despite awareness initiatives, there remains a large gap between *knowing* correct practices and *following* them consistently.

---

## 💡 Our Solution

**Sortify** acts as a personal waste assistant that helps users identify the correct disposal method for everyday waste items.

Users can:

* Enter a waste item name (text-based input)
* Receive instant guidance on:

  * Waste category (wet, dry, recyclable, e-waste, hazardous, etc.)
  * Proper disposal instructions
* Earn points for correct segregation (gamification-ready)

The project starts as a **Python-based Command Line Interface (CLI)** and is designed to scale into an AI-powered mobile or web application.

---

## 🎯 Key Features (MVP)

* Text-based waste classification
* Rule-based disposal guidance
* Simple CLI interaction
* Modular logic for easy expansion
* Lightweight and beginner-friendly architecture

---

## 🚀 Future Enhancements

* AI-based image recognition for waste items
* Multi-language support
* Routing to nearest recycling or donation centers
* Municipal pickup schedule integration
* Gamification (points, streaks, leaderboards)
* Rewards, coupons, and eco-incentives
* Data insights for municipalities and NGOs

---

## 🧑‍🤝‍🧑 Target Users

* Households & students
* Municipal corporations
* NGOs & recyclers
* Businesses generating recyclable waste

---

## 🛠️ Tech Stack (Current Phase)

* **Language:** Python
* **Interface:** Command Line Interface (CLI)
* **Data Storage:** JSON-based rule system

*(Advanced technologies will be added incrementally in later phases.)*

---

## 📁 Project Structure (Current)

```
sortify/
│
├── main.py          # CLI entry point
├── classifier.py    # Waste classification logic
├── rules.py         # Disposal rules & guidance
├── data.json        # Waste categories and instructions
├── user.py          # User points and progress (optional)
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/sortify.git
   ```

2. Navigate to the project folder

   ```bash
   cd sortify
   ```

3. Run the CLI

   ```bash
   python main.py
   ```

---

## 📌 Development Approach

* Start with a simple, rule-based CLI MVP
* Keep logic modular and UI-independent
* Gradually extend to APIs, mobile apps, and AI features
* Focus on real-world usability and scalability

---

## 🌱 Impact

* Reduces household confusion in waste segregation
* Improves recycling efficiency
* Encourages eco-friendly daily habits
* Supports cleaner and more sustainable communities

---

## 👥 Team

Developed by members of **Epoch – AIML Club**

* Aryaman Saraf
* Suryansh Bakshi

---

## 📜 License

This project is currently under development and intended for educational, research, and social-impact purposes.

---

**Turning everyday waste into responsible habits.
Let’s build a cleaner, smarter future—together. 🌍**
