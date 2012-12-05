from django.contrib import admin
from bscom.folio.models import Piece

class PortfolioPieceAdmin(admin.ModelAdmin):
    """
    Portfolio Piece admin configuration
    """
    list_display = ["title", "date"]


admin.site.register(Piece, PortfolioPieceAdmin)