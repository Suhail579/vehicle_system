# Vehicle Booking System

A Django REST Framework project for managing vehicles and customer bookings. Users can view available vehicles and book vehicles for selected dates. The system prevents double bookings for overlapping dates.


Installation required :


- pip install django
- pip install djangorestframework


## 2. Migration Commands

Run the following commands:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

## 3. How to Run the Project

Start the Django development server:

```Command 
python manage.py runserver
```

Open the project in your browser:


- http://127.0.0.1:8000/


## 4. How to Test APIs

Use **Postman** to test the REST APIs.

Steps:

1. Open Postman.
2. Select the HTTP method (GET or POST).
3. Enter the API URL.
4. For POST requests, select Body.
5. Select raw and JSON.
6. Enter the JSON data.
7. Click Send.
8. Check the response and status code.

## 5. API Endpoint List

| Method | Endpoint | Description |
|---|---|---|
| GET | /vehicle/ | Get all vehicles |
| GET | /booking/ | Get all bookings |
| POST | /booking/ | Create a new booking |

**Note:** Replace these endpoint paths if your project's `urls.py` uses different paths.

## 6. Sample JSON for Booking

Use the following JSON in Postman to create a booking.

**Method:** POST

**URL:** `http://127.0.0.1:8000/booking/`

**Body (raw → JSON):**

```json
{
    "customer_name": "Ali",
    "customer_phone": "8877878868",
    "Start_date": "2026-11-07",
    "End_date": "2026-11-08",
    "Total_amount": "1000.00",
    "vehicle": 1
}
```

## 7. Booking Validation

The booking system includes the following validations:

- Start date cannot be in the past.
- End date must be after the start date.
- A vehicle cannot be booked for overlapping dates.
- An already booked vehicle cannot be booked again for the same dates.
- After booking, vehicle availability is updated.

## 8. Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Postman
