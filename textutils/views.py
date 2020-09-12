from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Gurpreet', 'place':'Mars'}
    return render(request, 'index.html', params)

def about(request):
    return HttpResponse("Hello I am About page")
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    purpose = ''

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        purpose = purpose + 'Remove Punactuations,'
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':purpose,'analyzed_text':analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        purpose = purpose + 'Fullcaps,'
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': purpose,'analyzed_text':analyzed}
        djtext = analyzed
    if (newlineremover == "on"):
        analyzed = ""
        purpose = purpose + 'Remove Newline,'
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed


    if (spaceremover == "on"):
        analyzed = ""
        purpose = purpose + 'Remove Space,'
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed


    if (charcount == "on"):
        purpose = purpose + 'Count Characters,'
        cc = 0
        analyzed = ""
        for char in djtext:
            if(char != ' '):
                cc = cc + 1

        analyzed = djtext + str(cc)
        params = {'purpose': purpose, 'analyzed_text': analyzed}

        djtext = analyzed



    return render(request, 'analyze.html', params)
