from ipware import get_client_ip
import json, requests

from api.serializers import VisitorsAddressModelSerializer
from .models import VisitorsAddressModel


def ip_address(request):
    ip, is_routable = get_client_ip(request)
    # ip = "94.158.58.245"
    if ip is not None:
        data = json.loads(requests.get('http://ip-api.com/json/' + ip).text)
        # Add the user ID to the data dictionary
        if request.user.is_authenticated:
            data['user'] = request.user.id
        else:
            data['user'] = "1"

        # Pass the dictionary directly to the serializer
        serializer = VisitorsAddressModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print("Serializer saved successfully!")
        else:
            print('*' * 80, "Serializer is not valid", serializer.errors, serializer)
        return data
    else:
        return 'Unknown'
