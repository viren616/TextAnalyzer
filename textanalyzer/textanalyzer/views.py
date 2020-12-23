from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    text = request.POST.get('text','default')
    punccheck = request.POST.get('removepunc' , 'off')
    fullcapp = request.POST.get('fullcap','off')
    lineremover= request.POST.get('lineremover','off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount= request.POST.get('charcount', 'off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    if punccheck == "on":
        for char in text:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        text=analyzed
    if (fullcapp == "on"):
        analyzed=""
        for char in text:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Upper Case', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        text=analyzed
    if (lineremover== "on"):
        analyzed = ""
        for char in text:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Change To Upper Case', 'analyzed_text': analyzed}
        text=analyzed
       # return render(request, 'analyze.html', params)
    if (spaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(text):
            if text[index] == " "  and text[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Change To Upper Case', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        text=analyzed
    if (charcount== "on"):
        analyzed=""
        for index, char in enumerate(text):
            if text[index] == " " or text[index]=="\n":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Change To Upper Case', 'analyzed_text': len(analyzed)}
        # return render(request, 'analyze.html', params)
    #
    # else:
    #     return HttpResponse("error")
    return render(request, 'analyze.html', params)


# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("remove punc virendd")
#
# def capfirst(request):
#     return HttpResponse("cap virendd")
#
# def newlineremover(request):
#     return HttpResponse("new line virendd")
#
# def spaceremover(request):
#     return HttpResponse("space virendd")
#
# def charcount(request):
#     return HttpResponse("charcount virendd")
