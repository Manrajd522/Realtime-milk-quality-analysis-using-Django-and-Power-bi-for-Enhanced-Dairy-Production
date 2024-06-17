from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from django.core.exceptions import ObjectDoesNotExist
from .forms import UserForm, RecordForm
from .models import Record,User
from datetime import date
from django.db.models import Sum,Avg
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import authenticate, login, logout


def user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user_form.save()
            messages.info(request, "You are registered successfully")
            user_form = UserForm()  # Clear the form after successful submission
        
    else:
        user_form = UserForm()
    
    # Retrieve all users
    all_users = User.objects.all()
    
    return render(request, 'userform.html', {'user_form': user_form, 'all_users': all_users})


  


def total(request):
    submit = None
    total_quantity = 0
    average_fat = 0
    total_amount = 0
    Name = None
    
    if request.method == "POST":
        user = request.POST.get('User')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')

        if user:
            try:
                Name = User.objects.get(User_id=user)
            except User.DoesNotExist:
                Name = None  # Handle case where user does not exist
                
           
            submit = Record.objects.filter(user_id=user, Date__range=(fromdate, todate))
            aggregates = submit.aggregate(
                total_quantity=Sum('Quantity', default=0),
                average_fat=Avg('Fat', default=0),
                total_amount=Sum('Amount', default=0)
            )
            total_quantity = aggregates['total_quantity'] or 0
            average_fat = aggregates['average_fat'] or 0
            total_amount = aggregates['total_amount'] or 0
    
    return render(request, 'total.html', {
        'Name': Name,
        'submit': submit,
        'total_amount': total_amount,
        'total_quantity': total_quantity,
        'average_fat': average_fat,
        
    })


def record(request):
    context = {'data': Record.objects.filter(Date=date.today())}

    if request.method == "POST":
        user_id = request.POST.get('user_id')
        date_str = request.POST.get('date')
        quantity = request.POST.get('quantity')
        fat = request.POST.get('fat')
        snf = request.POST.get('snf')
        amount = request.POST.get('amount')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            context['error'] = 'User does not exist.'
            return render(request, 'record.html', context)

        if user and date_str and quantity and fat and snf and amount:
            record = Record.objects.create(
                user_id=user,
                Date=parse_date(date_str),
                Quantity=quantity,
                Fat=fat,
                SNF=snf,
                Amount=amount
            )
            record.save()
            return redirect('record')

    return render(request, 'record.html', context)

# def dashboard(request):
#     # Number of users
#     num_users = User.objects.count()
    
#     # Number of records
#     num_records = Record.objects.count()
    
#     # Today's total quantity in liters
#     today_total_quantity = Record.objects.filter(Date=datetime.now().date()).aggregate(sum_quantity=Sum('Quantity'))['sum_quantity'] or 0
    
#     # Today's total amount
#     today_sum_amount = Record.objects.filter(Date=datetime.now().date()).aggregate(sum_amount=Sum('Amount'))['sum_amount'] or 0
    
#     context = {
#         'num_users': num_users,
#         'num_records': num_records,
#         'today_total_quantity': today_total_quantity,
#         'today_sum_amount': today_sum_amount,
#     }
    
#     return render(request, 'dashboard.html', context)

def dashboard(request):
    # Number of users
    num_users = User.objects.count()
    
    # Number of records
    num_records = Record.objects.count()
    
    # Today's total quantity in liters
    today_total_quantity = Record.objects.filter(Date=datetime.now().date()).aggregate(sum_quantity=Sum('Quantity'))['sum_quantity'] or 0
    
    # Today's total amount
    today_sum_amount = Record.objects.filter(Date=datetime.now().date()).aggregate(sum_amount=Sum('Amount'))['sum_amount'] or 0
    
    # Monthly collection data
    monthly_collection_data = []
    for month in range(1, 13):
        monthly_amount = Record.objects.filter(Date__month=month).aggregate(sum_amount=Sum('Amount'))['sum_amount'] or 0
        monthly_collection_data.append(monthly_amount)
    
    context = {
        'num_users': num_users,
        'num_records': num_records,
        'today_total_quantity': today_total_quantity,
        'today_sum_amount': today_sum_amount,
        'monthly_collection_data': monthly_collection_data,
    }
    
    return render(request, 'dashboard.html', context)
def get_monthly_collection_data(request):
    # Get monthly collection data for the current year
    today = datetime.now()
    year = today.year
    monthly_collection_data = []

    for month in range(1, 13):
        month_records = Record.objects.filter(Date__year=year, Date__month=month)
        total_amount = month_records.aggregate(total_amount=Sum('Amount'))['total_amount'] or 0
        monthly_collection_data.append(total_amount)

    return JsonResponse(monthly_collection_data, safe=False)

def visuals(request):
    return render(request,'visuals.html')

def update_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == "POST":
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect(reverse('record'))
    else:
        form = RecordForm(instance=record)
    return render(request, 'update_record.html', {'form': form})

def delete_record(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if request.method == "POST":
        record.delete()
        return redirect(reverse('record'))
    return render(request, 'delete_record.html', {'record': record})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user) 
            return redirect('/record/') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')
