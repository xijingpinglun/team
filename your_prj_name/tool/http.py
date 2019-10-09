import json

from django.http import HttpResponse,JsonResponse
from django.conf import settings


def render_json(data, code=0,message=''):
    result = {
        'code': code,
        'message':message,
        'data': data
    }

    # if settings.DEBUG:
    #     json_data = json.dumps(result, ensure_ascii=False, indent=4, sort_keys=True)
    # else:
    #     json_data = json.dumps(result, ensure_ascii=False, separators=[',', ':'])

    return JsonResponse(result,json_dumps_params={"ensure_ascii":False})