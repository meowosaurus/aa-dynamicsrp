"""App Views"""

# Django
from django.contrib.auth.decorators import login_required, permission_required
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Subquery, OuterRef
from django.db.models import F
from django.db.models.functions import Coalesce

from .models import *

def test():
    all_settings = Setting.objects.all()

    test_matrix = []
    #for setting in all_settings:
        




@login_required
@permission_required("dynamicsrp.basic_access")
def payouts(request: WSGIRequest) -> HttpResponse:
    """
    Index view
    :param request:
    :return:
    """

    #context = {"text": "Hello, World!"}

    ship_rows = Ship.objects.all().order_by("name")
    columns = Reimbursement.objects.all().order_by("index")
    matrix = []
    column_width = 100 / (columns.count() + 1)

    setting_display_all_ships = Setting.objects.get(name="display_all_ships")

    for row in ship_rows:
        if Payout.objects.filter(ship=row).count() > 0 or setting_display_all_ships.value == "True":
            row_data = [row]
            for column in columns:
                cell = Payout.objects.filter(ship=row, reimbursement=column).first()
                row_data.append(cell)
            matrix.append(row_data)

    test()

    context = {'header_rows': ship_rows, 
                'matrix': matrix,
                'columns': columns,
                'column_width': column_width}

    return render(request, "dynamicsrp/payouts.html", context)
