from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Stock
from .forms import StockForm, PortfolioForm
from .api import get_stock_price
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def home(request):
    return render(request, 'base.html')

@login_required
def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio/portfolio_list.html', {'portfolios': portfolios})

@login_required
def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    stocks = portfolio.stock_set.all()
    return render(request, 'portfolio/portfolio_detail.html', {'portfolio': portfolio, 'stocks': stocks})

from django.http import JsonResponse

@login_required
def add_stock(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock_price = get_stock_price(stock.symbol)
            if stock_price is not None:
                stock.current_price = stock_price
                stock.portfolio = portfolio
                stock.save()
                return redirect('portfolio_detail', pk=portfolio.pk)
            else:
                # Add error message to form and return as JSON response
                form.add_error(None, "Unable to retrieve stock price. Please try again later.")
                errors = form.errors.as_json()
                return JsonResponse({'errors': errors}, status=400)
        else:
            # Return form errors as JSON response
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = StockForm()
    return render(request, 'portfolio/add_stock.html', {'form': form})


@login_required
def add_portfolio(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.save()
            return redirect('portfolio_list')
    else:
        form = PortfolioForm()
    return render(request, 'portfolio/add_portfolio.html', {'form': form})
