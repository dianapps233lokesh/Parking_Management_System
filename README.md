# 🚗 Parking Management System

A command-line Parking Management System built with Python. It handles vehicle entry/exit, generates tickets, calculates parking fees, and tracks revenue using a REPL (Read–Eval–Print Loop) interface.

---

## 📦 Features

- ✅ Allot parking to `TwoWheeler` or `FourWheeler`
- 🎫 Unique ticket generation
- ⏱️ Entry/exit time tracking
- 💰 Parking fee calculation
- 📋 View currently parked vehicles
- 🅿️ View available parking space
- 📈 View total revenue
- 🌀 Continuous REPL-based user interaction

---

## 📁 Project Structure

```
parking-system/
│
├── main.py
└── src/
    ├── components/
    │   ├── parking.py
    │   └── vehicle.py
    └── pipeline/
    |    └── parking_pipeline.py
    |
    |___utils/
        |
        |____id_generate.py 
```

---

## ▶️ How to Run

### Prerequisites:
- Python 3.7+

### Run the app:
```bash
python3 main.py
```

---

## 🧪 Sample Menu

```
Menu:
1. Allot Parking
2. Checkout
3. View Parked Vehicles
4. View Available Space
5. View Total Revenue
6. Exit
```

Follow the prompts to interact with the system.

---

## 🧠 Example Usage

1. Select `1` to allot parking.
2. Choose vehicle type (`1` = two-wheeler, `2` = four-wheeler).
3. Enter owner name and vehicle number.
4. Get a ticket ID.
5. Select `2` to checkout using ticket ID.
6. View fees, revenue, and parked vehicles.

---

## 🛠 Technologies Used

- Python 3
- Modules: `time`, `random`, `string`

---


## 👨‍💻 Author

Created by Lokesh Kumar Saini

---

## 📄 License

MIT License
