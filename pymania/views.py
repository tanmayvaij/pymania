from django.shortcuts import render


def home(request):

    if request.method == "POST":

        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "phonenumber": request.POST.get("phonenumber")
        }

        return render(request, "index.html", data)
    return render(request, "index.html")
