from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.conf import settings
from groq import Groq

# Initialize Groq Client
client = Groq(api_key=settings.GROQ_API_KEY)

def chat_page(request):
    return render(request, "chat.html")

class ChatBotView(APIView):
    def post(self, request):
        question = request.data.get('message', '')

        if not question:
            return Response({"error": "No message sent."}, status=status.HTTP_400_BAD_REQUEST)

        # Initialize Groq client inside the view
        api_key = settings.GROQ_API_KEY
        if not api_key:
            return Response({"error": "GROQ_API_KEY not set in environment!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        client = Groq(api_key=api_key)

        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",


                messages=[{"role": "user", "content": question}]
            )

            answer = response.choices[0].message.content  # ✅ correct


            return Response({"reply": answer}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
