
from django.shortcuts import render
from django.http import JsonResponse
from PIL import Image, ExifTags
from django.conf import settings


def main(request):
    context = {'mapbox_access_token': settings.MAP_BOX_ACCESS_TOKEN}
    return render(request, 'main.html', context=context)


def upload_document(request):
    if request.method == "POST":
        my_img = request.FILES.get('file')

    with Image.open(my_img) as image:
        exif = {ExifTags.TAGS[k]: v for k,
                v in image._getexif().items() if k in ExifTags.TAGS}
        north = exif['GPSInfo'][2]
        east = exif['GPSInfo'][4]
        latitude = float(north[0] + north[1] / 60 + north[2] / 3600)
        longitude = float(east[0] + east[1] / 60 + east[2] / 3600)
        return JsonResponse({'latitude': latitude, 'longitude': longitude})
