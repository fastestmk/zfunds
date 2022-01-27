from django.shortcuts import render
from .utils import send_async_email, sendSlackMessage
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from threading import Thread
from django.conf import settings



class NotificationAPIView(APIView):
	permissions_classes = (IsAuthenticated,)
	
	@staticmethod
	def post(request):
		context = {}
		email = request.user.email
		if not email:
			context["success"] = False
			context["message"] = "Email doesn't exist"

			return Response(context)
		else:	
			subject = "Payment from zfunds"
			message = "You have received 500 rupees"
			print(type(settings), "typeofsetingngs")
			sender = settings.EMAIL_HOST_USER
			receivers = [email]
			try:
				send_async_email(subject, message, sender, receivers, fail_silently=True)
				sendSlackMessage(message)
				context["success"] = True
				context["message"] = "Message sent to mail and slack"
				return Response(context)
			except Exception as e:
				print(str(e))
				context["success"] = False
				context["message"] = "Some error occured"
				return Response(context)	