from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Income, Expense
from .forms import CustomRegisterForm, IncomeForm, ExpenseForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomRegisterForm
from django.db.models import Sum
import calendar, csv
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
import json
from django.db.models.functions import TruncMonth
from collections import OrderedDict
from .models import Budget
from django.http import HttpResponse

@login_required
def dashboard(request):
    incomes = Income.objects.filter(user=request.user).order_by('-date')
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0
    balance = total_income - total_expense
    budget = None
    overspent = False

    if request.user.is_authenticated:
        budget = Budget.objects.filter(user=request.user).first()
        if budget and total_expense > budget.monthly_limit:
            overspent = True

    # --- Pie Chart: Category-wise Expense Data ---
    category_summary = (
        expenses.values('category')
        .annotate(total=Sum('amount'))
        .order_by('-total')
    )
    category_labels = [item['category'] for item in category_summary]
    category_totals = [float(item['total']) for item in category_summary]

    # --- Line Chart: Monthly Expense Data ---
    monthly_summary = (
        expenses.annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )
    monthly_labels = [item['month'].strftime('%B %Y') for item in monthly_summary]
    monthly_totals = [float(item['total']) for item in monthly_summary]

    context = {
        'incomes': incomes,
        'expenses': expenses,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'category_labels': json.dumps(category_labels),
        'category_data': json.dumps(category_totals),
        'monthly_labels': json.dumps(monthly_labels),
        'monthly_data': json.dumps(monthly_totals),
        'budget': budget,
        'overspent': overspent,

    }
    return render(request, 'tracker/dashboard.html', context)


def register_view(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('dashboard')
    else:
        form = IncomeForm()
    return render(request, 'tracker/add_income.html', {'form': form})

from django.contrib import messages

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})

# 🔁 EDIT INCOME
@login_required
def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'tracker/edit_income.html', {'form': form})

# ❌ DELETE INCOME
@login_required
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == 'POST':
        income.delete()
        return redirect('dashboard')
    return render(request, 'tracker/delete_income.html', {'income': income})

# 🔁 EDIT EXPENSE
@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/edit_expense.html', {'form': form})

# ❌ DELETE EXPENSE
@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('dashboard')
    return render(request, 'tracker/delete_expense.html', {'expense': expense})


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def set_budget(request):
    budget, created = Budget.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        amount = request.POST.get('monthly_limit')
        budget.monthly_limit = amount
        budget.save()
        messages.success(request, "Budget updated.")
        return redirect('dashboard')
    return render(request, 'tracker/set_budget.html', {'budget': budget})


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=expenses.csv'

    writer = csv.writer(response)
    writer.writerow(['Amount', 'Category', 'Description', 'Date'])

    expenses = Expense.objects.filter(user=request.user)
    for expense in expenses:
        writer.writerow([expense.amount, expense.category, expense.description, expense.date])

    return response