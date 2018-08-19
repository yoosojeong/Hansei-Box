from django.shortcuts import render

class Choose(APIView):

    def post(self, request, format=None):

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):

        return render(request, "choose.html", {})