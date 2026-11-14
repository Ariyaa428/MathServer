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

