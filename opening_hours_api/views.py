import json

from rest_framework.response import Response
from rest_framework.views import APIView

from opening_hours_api.utils import convert_opening_hours


class OpeningHoursAPIView(APIView):

    def post(self, request):
        opening_hours = request.data
        human_readable_dict = convert_opening_hours(opening_hours)
        return Response(json.dumps(human_readable_dict))
