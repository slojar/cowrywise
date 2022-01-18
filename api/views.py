from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Answer


class AnswerView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            # Create new UUID instance
            Answer.objects.create()
            # Get all UUID instance (with latest at the top)
            all_items = Answer.objects.all().order_by('-id')

            answer = {str(item.key): str(item.value).replace("-", "") for item in all_items}

            return Response(answer)
        except Exception as ex:
            return Response({"error": "An error has occurred", "message": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


