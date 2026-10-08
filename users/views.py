from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserModel
from django.forms.models import model_to_dict


class UserListCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        user = UserModel(name=data['name'], age=data['age'], status=data['status'], weght=data['weght'])
        user.save()
        response_data = model_to_dict(user)
        return Response()
class UserRetrieveUpdateDestroyView(APIView):
    pass