# Ex.03 Design a Website for Server Side Processing
## Date: 14/11/2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
    <head>
        <title>calculater</title>
    </head>
    <body>
        <h1>Ariya(26009918)</h1>
        <h2>Churn Rate Count</h2>

        <form method="POST">
          {% csrf_token %}
            
            <label>Customers Count:</label>
            <input type="number"  name="length" value="{{ Customer_Lost }}">
            <br><br><br><br>
            
            <label> Customers initial Count:</label>
            <input type="number" name="breadth" value="{{ Initial_customer }}" >
            <br><br><br><br>
            
            <input type="submit" value="count" >
            <br><br><br><br>
            
            <label>Churn Rate Total:</label>
            <input type="number"value="{{ area }}">
        </form>
    </body>
</html>

views.py
from django.shortcuts import render

def Churn_Rate_area(request):
    Customer_Lost = float(request.POST.get('length', '0'))
    Initial_customer = float(request.POST.get('breadth', '0'))

    area = (Customer_Lost/Initial_customer) *100 if request.method == 'POST' else 0
    print("Customer _Lost =", Customer_Lost)
    print("Initial_customer =", Initial_customer)
    print("area of rectangle =", area)

    return render(
        request,
        'myapp/ariya.html',
        {'Customer_Lost': Customer_Lost, 'Initial_customer':  Initial_customer, 'area': area}
    )

urls.py


from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.Churn_Rate_area, name=' Churn_Rate_area'),
]

```


## OUTPUT - SERVER SIDE:

![alt text](<Screenshot (11).png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot (10)-1.png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
