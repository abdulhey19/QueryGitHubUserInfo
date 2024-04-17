from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
import requests

# Create your views here.
github_url="https://api.github.com/users/"

def sorgu(request):
    if request.method == 'POST':
        github_name=request.POST.get("githubname") 
        response_user=requests.get(github_url+github_name)
        profile=response_user.json()
        if "message" in profile:
            return redirect("sorgu")
        else:
            response_repos=requests.get(github_url+github_name+"/repos")
            repos=response_repos.json()
            if not "name" in profile:
                return redirect("sorgu")
            return render(request, "sorgu.html",{'profile':profile, 'repos':repos})
    else:
        return render(request, 'sorgu.html')
        


    
