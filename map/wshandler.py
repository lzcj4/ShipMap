from map.models import ShipDefenceArea


# from map.websocket import JSONObject


def add_or_update_area(json_obj):
    items = ShipDefenceArea.objects.filter(name=json_obj.id)
    if len(items) > 0:
        item = items[0]
        item.longitude = json_obj.lnglat[0]
        item.latitude = json_obj.lnglat[1]
        item.radius = json_obj.radius
        item.save()
    else:
        ShipDefenceArea.objects.create(name=json_obj.id, longitude=json_obj.lnglat[0],
                                       latitude=json_obj.lnglat[1], radius=json_obj.radius)
