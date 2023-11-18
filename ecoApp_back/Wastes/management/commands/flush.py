from django.core.management.base import BaseCommand
from Wastes.models import WasteSite, WasteTypes
import os, sys, json


class Command(BaseCommand):
    help = 'flush one table the db'

    def add_arguments(self, parser):
        parser.add_argument("table_name", nargs="?", type=str, default="site")

    def handle(self, *args, **kwargs):
        table_name =  kwargs["table_name"]

        


        