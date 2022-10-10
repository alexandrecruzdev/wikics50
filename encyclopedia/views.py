from email import message
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def similarpages(request,title):
    entries = util.list_entries()
    similares = []
    for entry in entries:
        str = entry.upper()
        if str.find(f"{title.upper()}") >= 0:
            similares.append(entry)
        else:
            print("String doesn't exist")

    if len(similares) <= 0:
         return render(request,'encyclopedia/entrynotfound.html',{
        'message': 'Page not found!'
        })
    
    return render(request,'encyclopedia/similarpages.html',{
        "entries":similares
    })

def editpage(request,title):
    content = util.get_entry(title)

    if request.method == 'POST':
        content = request.POST["content"]
        util.save_entry(title,content)
        return HttpResponseRedirect(reverse('get_encyclopedia',args=[title]))

    return render(request,'encyclopedia/editpage.html',{
      'title':title,
      'content':content
    })

def newpage(request):
  

    if request.method == 'POST':
            title = request.POST["title"]
            content = request.POST["content"]
            entries = util.list_entries()
            title_exist = False
           # if  title in entries:
            #    title_exist = True
            #    return HttpResponseRedirect(reverse('index'))

            #if not title_exist:
            #   util.save_entry(title,content)
            #    return HttpResponseRedirect(reverse('get_encyclopedia',args=[title]))
            for entry in entries:
                title = title.upper()
                entry = entry.upper()
                if title == entry:
                    title_exist = True
            
            if title_exist:
                return render(request,'encyclopedia/errorpage.html', {
                    'message':'This title has already been registered!'
                })
            else:
                title = title.capitalize()
                util.save_entry(title,content)
                return HttpResponseRedirect(reverse('get_encyclopedia',args=[title]))
            

    return render(request,'encyclopedia/newpage.html',{

    })
def randompage(request):

    entries = util.list_entries()
    title_random = random.choice(entries)
    entry = util.get_entry(title_random)


    return render(request,'encyclopedia/randompage.html',{
        'title': title_random,
        'entry':entry
    })

def get_encyclopedia(request,title):

    if request.method == 'GET':
        entry = util.get_entry(title)
        if util.get_entry(title):
            return render(request,'encyclopedia/getencyclopedia.html',{
            'title': title,
            'entry': entry,
            })
        return HttpResponseRedirect(reverse('similarpages', args=[title]))

       
    
    if request.method == 'POST':
        title = request.POST["q"]
        entry = util.get_entry(title)
        if util.get_entry(title):
            return render(request,'encyclopedia/getencyclopedia.html',{
            'title': title,
            'entry': entry,
            })
        
        return HttpResponseRedirect(reverse('similarpages', args=[title]))

    
  
    
    