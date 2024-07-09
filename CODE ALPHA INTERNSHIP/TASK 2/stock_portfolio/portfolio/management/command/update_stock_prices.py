from django.core.management.base import BaseCommand
from portfolio.models import Stock
from portfolio.api import get_stock_price

class Command(BaseCommand):
    help = 'Update stock prices'

    def handle(self, *args, **kwargs):
        stocks = Stock.objects.all()
        for stock in stocks:
            stock.current_price = get_stock_price(stock.symbol)
            stock.save()
        self.stdout.write(self.style.SUCCESS('Successfully updated stock prices'))
