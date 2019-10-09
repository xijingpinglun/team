import json

from django.http import HttpResponse
from django.conf import settings


def render_json(data, code=0,msg=""):
    result = {
        'code': code,
        "message":msg,
        'data': data
    }

    if settings.DEBUG:
        json_data = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        json_data = json.dumps(result, ensure_ascii=False, separators=[',', ':'])

    return HttpResponse(json_data)