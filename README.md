# AccuKnox User Management Tests

This repository contains end-to-end test automation for the **User Management module** of [OrangeHRM](https://opensource-demo.orangehrmlive.com/), using **Playwright with Python**.

## ✅ Features Covered

- Navigate to Admin Module
- Add a New User
- Search the Newly Created User
- Edit User Details
- Validate Updates
- Delete the User

---

## 📦 Project Structure

```
AccuKnox-user-management-tests/
├── pages/
│   ├── login_page.py       # Login logic abstraction
│   └── admin_page.py       # Admin page CRUD operations
│
├── tests/
│   ├── test_add_user.py    # Adds a user
│   └── test_crud_flow.py   # Full CRUD flow
│
├── README.md               # This file
└── requirements.txt        # Dependencies
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/AccuKnox-user-management-tests.git
cd AccuKnox-user-management-tests
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4. Run tests
```bash
pytest tests/
```

---

## 🧪 Test Credentials
**Username**: Admin  
**Password**: admin123  
➡️ [Login URL](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login)

---

## 🐛 Issues/Bugs Encountered
> No major issues encountered during automation. The Employee Name field requires exact match and suggestion click.

---

## 🧾 Test Case Document
Excel File Name: `AccuKnox_User_Management_TestCases.xlsx`
