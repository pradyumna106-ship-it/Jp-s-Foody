# Jp-s-Foody

MealMate is a full‑stack food ordering and delivery web application that connects hungry diners with nearby local restaurants. It is designed to offer a smooth, transparent ordering experience for users while helping restaurants accept and manage online orders without paying heavy commissions to third‑party platforms.

## Problem Overview

On a busy or rainy day, many people want restaurant‑quality food without stepping outside. At the same time, restaurants often face empty tables during off‑peak hours and would love to serve more customers. Traditional food delivery platforms bridge this gap, but they often:

- Charge high commissions on every order, cutting deeply into restaurant profits.  
- Offer unclear menus and limited information for customers.  
- Provide inconsistent order tracking and sometimes steep delivery charges.

These issues create friction for both diners and restaurant owners. MealMate aims to simplify this process and make it fair for everyone involved.

## What Is MealMate?

MealMate is a Python/Django‑based web application that brings diners and local eateries closer together. Users can browse restaurants, explore clear and structured menus, place online orders, and track them in real time. Restaurant owners get a dedicated dashboard to receive, manage, and update orders without relying on expensive third‑party delivery aggregators.

The focus is on:

- A clean, intuitive customer experience.  
- Empowering restaurant partners with better control over their online orders.  
- Reducing platform overheads so small eateries can stay profitable.

## Key Features

### For Diners

- **Easy Restaurant Search**  
  Browse nearby restaurants and discover local eateries quickly.

- **Clear Menus**  
  View organized menus with dish details so you know exactly what you are ordering.

- **Quick Online Ordering**  
  Add items to a cart and place orders in just a few clicks.

- **Real‑Time Order Tracking**  
  Track your order status from placement to preparation and delivery.

### For Restaurants

- **Restaurant Dashboard**  
  Secure login for restaurant owners to manage their presence on the platform.

- **Order Management**  
  View incoming orders, update statuses (e.g., received, preparing, out for delivery), and mark them as completed.

- **Fair Pricing**  
  Reduce reliance on high‑commission platforms by handling online orders directly through MealMate.

## Why Build Jp-s-Foody?

### For Diners

- Discover local food options easily.  
- Enjoy a smoother ordering flow with clear menus and tracking.  
- Reduce friction and uncertainty around delivery and order status.

### For Restaurants

- Reach more customers without sacrificing a large share of revenue.  
- Manage orders efficiently from a single dashboard.  
- Retain better control over customer relationships and branding.

### For Developers

MealMate is also a learning‑focused project that demonstrates a practical full‑stack architecture:

- **Django** for backend development, data models, business logic, and APIs.  
- **HTML, CSS, JavaScript** for building a responsive and user‑friendly front end.  
- **Real‑world problem‑solving** by designing flows that work well for both diners and restaurant owners.

This project is a great way to practice authentication, CRUD operations, form handling, templates, and integration of frontend and backend components in a realistic scenario.

## Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** (e.g., SQLite during development; can be upgraded to PostgreSQL/MySQL)  
- **Other Tools:** Git/GitHub for version control and collaboration

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/pradyumna106-ship-it/Jp-s-Foody.git
cd Jp-s-Foody
```
2. Create and activate a virtual environment (optional but recommended).
```bash
pip install -r requirements.txt
```
3. Install dependencies:
  ```bash
npm install
```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver
```

7. Open the app in your browser at:
```bash
http://127.0.0.1:8000/
```


## Roadmap / Possible Enhancements

- User authentication and profiles for diners and restaurant owners.  
- Payment gateway integration for online payments.  
- Delivery partner assignment and tracking.  
- Ratings and reviews for restaurants and dishes.  
- Mobile‑friendly UI improvements.

## Contributing

Contributions, ideas, and suggestions are welcome. Feel free to open issues or submit pull requests to improve features, fix bugs, or enhance documentation.

## License

Specify your license here (e.g., MIT License) once you decide how you want others to use this project.



