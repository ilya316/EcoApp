from django.core.management.base import BaseCommand
from Wastes.models import WasteSite, WasteTypes
import os, sys, json


class Command(BaseCommand):
    help = 'fill the db'
    
    def handle(self, *args, **kwargs):
        script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        
        # Types
        # with open(script_directory + '\\Wastes\\management\\commands\\types.json', 'r', encoding='utf8') as data:
        #     for item in json.loads(data.read()):
        #         new_type = WasteTypes(**item)
        #         new_type.save()
        # Containers
        with open(script_directory + '\\Wastes\\management\\commands\\container_sites.json', 'r', encoding='utf8') as data:
            for item in json.loads(data.read()):
                _lattitude, _longitude = str(item['Coordinates']).split(',')
                try:
                    new_site = WasteSite(
                        name = item['YardName'],
                        address = item['YardAddress'][0]['Address'],
                        yard_type = item['YardType'],
                        lattitude = _lattitude,
                        longitude = _longitude
                    )
                    new_site.save()
                except:
                    pass
        # # Large containers
        # with open(script_directory + '\\Wastes\\management\\commands\\large_containers.json', 'r', encoding='utf8') as data:
        #     for item in json.loads(data.read()):
        #         try:
        #             _lattitude, _longitude = item['geoData']['coordinates']
        #             new_site = WasteSite(
        #                 name = item['Name'],
        #                 address = item['Address'][0]['Address'],
        #                 yard_type = item['Name'],
        #                 lattitude = _lattitude,
        #                 longitude = _longitude
        #             )
        #             new_site.save()
        #         except:
        #             pass
        # # Lamps
        # with open(script_directory + '\\Wastes\\management\\commands\\lamps.json', 'r', 'utf8') as data:
        #     for item in json.loads(data.read()):
        #         try:
        #             _lattitude, _longitude = item['geoData']['coordinates']
        #             new_site = WasteSite(
        #                 name = item['Name'],
        #                 address = item['Address'],
        #                 yard_type = item['Name'],
        #                 lattitude = _lattitude,
        #                 longitude = _longitude
        #             )
        #             new_site.save()
        #         except:
        #             pass
        # -------------------