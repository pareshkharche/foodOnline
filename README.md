# 🍽️ FoodOnline – Online Food Ordering Platform

A full-stack Django-based web application for online food ordering, enabling customers to browse restaurants, view menus, place orders, and track deliveries — all in one platform.

---

## 🚀 Features

- User registration and authentication (customers and vendors)
- Restaurant/vendor onboarding and profile management
- Menu and food item management by vendors
- Customers can browse menus and add items to cart
- Order placement and real-time order tracking
- GIS-ready (with GDAL) for location-based services
- Admin dashboard for superusers and vendors
- Fully responsive user interface

---

## 🛠️ Tech Stack

- **Backend**: Python, Django, DRF
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Others**:
  - GDAL (for location/geospatial support)
  - Django ORM
  - Django admin panel
  - Environment variable management with `.env`
  - Bootstrap-based styling

---

## 📁 Project Structure (Partial)

```
foodOnline/
├── accounts/             # Handles user registration and authentication
├── customers/            # Logic for customer-side features
├── marketplace/          # Logic for vendors/restaurants
├── menu/                 # Food menu and item management
├── orders/               # Order lifecycle management
├── static/               # CSS, JavaScript, fonts, images
├── foodOnline_main/      # Project configuration, settings, URLs
├── manage.py             # Django's main CLI entry
└── .env-sample           # Sample file for environment variables
```

---

## 💡 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pareshkharche/foodOnline.git
cd foodOnline
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If `requirements.txt` is not present, you can generate it using:
> ```bash
> pip freeze > requirements.txt
> ```

### 4. Install GDAL (Required for Geo-related Features)

Use the provided `.whl` file or run:

```bash
pip install gdal-3.10.2-cp312-cp312-win_amd64.whl
```

Or install directly using pip (if not OS-specific):

```bash
pip install GDAL
```

### 5. Set Up PostgreSQL Database

1. Create a PostgreSQL database and user.
2. Copy `.env-sample` to `.env` and update values:

```env
DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Then visit: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Testing the App

- Log in as a vendor or customer
- Browse restaurant menus
- Add items to cart and place orders
- Track orders (GIS support optional)
- Access admin at `/admin` (login with superuser credentials)

---

