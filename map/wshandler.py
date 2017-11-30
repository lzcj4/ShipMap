import json

from map.models import ShipDefenceArea


def get_all_areas():
    items = ShipDefenceArea.objects.all()
    result = []
    for item in items:
        item_props = {"id": item.name, "longitude": item.longitude, "latitude": item.latitude, "radius": item.radius}
        result.append(item_props)
    return json.dumps(result)


def add_or_update_area(json_obj):
    items = ShipDefenceArea.objects.filter(name=json_obj.id)
    if len(items) > 0:
        for item in items:
            item.longitude = json_obj.lnglat[0]
            item.latitude = json_obj.lnglat[1]
            item.radius = json_obj.radius
            item.save()
    else:
        ShipDefenceArea.objects.create(name=json_obj.id, longitude=json_obj.lnglat[0],
                                       latitude=json_obj.lnglat[1], radius=json_obj.radius)
