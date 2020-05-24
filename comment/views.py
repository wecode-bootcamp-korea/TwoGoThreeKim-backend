import json
from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment

class CommentView(View):
    def post(Self, request):
        comment_info = json.loads(request.body)

        try:
            Comment.objects.create(
                    user_id = comment_info['user_id'],
                    user_comment = comment_info['user_comment'],
            )
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)

    def get(self, request):
        comment_data = list(Comment.objects.values())

        try:
            return JsonResponse({'data':comment_data},status=200)
        except Comment.DoesNotExist:
            return JsonResponse({'message':'COMMENT_DOES_NOT_EXIST'}, status=400)
