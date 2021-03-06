from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january" : "Eat no meat for entire month",
    "february" : "Walk for atleast 20 minutes everyday",
    "march" : "Learn Django for atleast 20 minutes everyday",
    "april" : "Learn Spark for atleast 20 minutes everyday",
    "may" : "Learn Pandas for atleast 20 minutes everyday",
    "june" : "Learn EDA on different datasets everyday",
    "july" : "Learn different machine learning algorithms",
    "august" : "Solve different machine learning algorithms everyday",
    "september" : "Learn HLD and LLD everyday for every project worked on",
    "october" : "Learn the deployment process and CICD pipeline everyday in all the cloud platform",
    "november" : "Prepare for interviews everyday revising everything",
    "december" : None
    # "december" : "Sit in an interview everyday and get a good job as Data Scientist"
}
# Create your views here.

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {"months" : months})
    

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    try:
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
        # return HttpResponseRedirect("/challenges/" + redirect_month)
    except:   
        return HttpResponseNotFound("This month number is not supported")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {"text" : challenge_text, "month_name": month})
        
    except:
        raise Http404()
    