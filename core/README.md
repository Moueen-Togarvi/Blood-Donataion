# Dr Blood Donar - Bahawalnagar Donor Directory

A specialized Django-based web application designed as a **Blood Donor Directory** for the city of **Bahawalnagar, Punjab, Pakistan**. This platform connects people in urgent need of blood with local available donors.

## 🌟 Key Features

- **Mobile-First Design**: Optimized for a native app-like experience on mobile devices.
- **Bahawalnagar Focused**: Specifically localized for Bahawalnagar with pre-filled locations.
- **Quick Search Pills**: Interactive blood group filters for instant results.
- **Verified Donors**: Prominent badges for verified and available donors.
- **One-Click Contact**: "Call Now" and "Copy Number" buttons for fast communication.
- **Minimalist Interface**: English-only, clean, and extremely simple navigation.
- **Donor Profiles**: Detailed listings including distance from DHQ Hospital and secondary phone numbers.

## 🚀 Tech Stack

- **Backend**: Python / Django
- **Frontend**: Vanilla CSS (Modern, Responsive Design)
- **Database**: SQLite (Default)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/moueen-togarvi/Blood-Donataion.git
cd Blood-Donataion/DrBloodDonar-master
```

### 2. Set Up Virtual Environment
```bash
# Install virtualenv if you haven't
pip install virtualenv

# Create environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
```

### 5. Run the Application
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

## 📸 Project Focus

The project has been pivoted from a general "Blood Request" board to a dedicated **Donor Directory**. The UI/UX is designed for maximum accessibility, prioritizing speed and clarity for users in medical emergencies.

---
*Developed with focus on community service for Bahawalnagar.*
