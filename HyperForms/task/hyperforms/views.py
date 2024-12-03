from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("""<h2>Welcome to the reading club</h2>
<p><b>The link to the introduction form is coming soon</b></p>""")
