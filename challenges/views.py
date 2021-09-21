from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

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
    "december" : "Sit in an interview everyday and get a good job as Data Scientist"
}
# Create your views here.

def monthly_challenge_by_number(request, month):
    forward_month = monthly_challenges.keys()
    
    return HttpResponse(month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
    