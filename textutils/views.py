from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")


def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse(sites)


def analyze(request):
    # Get text
    djtext = request.POST.get('text', 'defaults')
    print(djtext)
    removepunc = request.POST.get('removepunc', 'off')
    FULLCAPTIAL = request.POST.get('UPPERCASE', 'off')
    newlineremove = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    punctions = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punctions:
                analyzed = analyzed + char

            params = {"purpose": "Remove Punctuations", "analyzed_text": analyzed}
            djtext = analyzed
        # anyalze the  text
        # return render(request, 'analyze.html', params)
    if FULLCAPTIAL == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {"purpose": "Full Capitaled letter", "analyzed_text": analyzed}

            djtext = analyzed
    # return render(request, 'analyze.html', params)
    if newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":

                analyzed = analyzed + char
            else:
                print("NO")
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
    # return render(request, 'analyze.html', params)
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
    if removepunc != "on" and FULLCAPTIAL != "on" and newlineremove != "on" and extraspaceremover != "on" :
        return HttpResponse("Pleas e the select ON any button")
    return render(request, 'analyze.html', params)
