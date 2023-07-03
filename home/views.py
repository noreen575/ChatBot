from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"


# Create your views here.
def chat(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def chatAPI(request):
    try:
        if request.method == "POST":
            prompt = request.POST["prompt"]
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return JsonResponse(response)
        else:
            return HttpResponse("Bad request")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}")
