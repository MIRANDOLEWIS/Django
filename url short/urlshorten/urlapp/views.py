from django.http import HttpResponse
from django.shortcuts import redirect, render
import uuid
from urlapp.models import LinkInfo
# Create your views here.
def urlform(request):
    return render(request,"urlapp/urlhome.html",{})

def create(request):
    if request.method == "POST":
        mainlink = request.POST["link"]
        uid = str(uuid.uuid4())[:5]

        new_link = LinkInfo(
            mainlink = mainlink,
            linkid = uid,
        )

        new_link.save()

        return HttpResponse(uid)


def go(request,pk):
    url_details = LinkInfo.objects.get(linkid=pk)

    return redirect('https://'+url_details.mainlink)        
