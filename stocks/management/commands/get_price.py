# -*- coding: UTF-8 -*-
from django.core.management.base import BaseCommand

from stocks.models import Stock, StockPair
from stocks.utils import update_stocks_prices


class Command(BaseCommand):
    help = u'更新股票价格，默认只更新收藏的股票'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help=u'更新全部股票'
        )

    def handle(self, *args, **options):
        stocks = Stock.objects.all()
        print 'Updating'
        if options.get('all'):
            stocks = Stock.objects.all()
            pairs = StockPair.objects.all()
            print 'All Stocks'
        else:
            stocks = stocks.filter(star=True)
            pairs = StockPair.objects.filter(star=True)
            print 'Used Stocks'

        i = 0
        count = stocks.count()
        while i < count:
            group = stocks[i:i+50]
            update_stocks_prices(group)
            i += 50

        if options.get('verbosity'):
            print 'Done updating {} stocks. '.format(count)
        for pair in pairs:
            pair.update_if_needed()
        if options.get('verbosity'):
            print 'Updated Pairs'
