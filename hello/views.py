from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.http import HttpResponse
from django.views.generic import ListView
from hello.forms import LogMessageForm
from hello.models import LogMessage

from rest_framework import generics
from hello.models import StockData
from hello.serializers import StockDataSerializer

# This is the StockData API
class StockDataListCreate(generics.ListCreateAPIView):
    """API endpoint for listing and adding stock data."""
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

class StockDataDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving, updating, or deleting a specific stock record."""
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

# The standard Website

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage
    template_name = "hello/home.html"  # Explicitly specify the template

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        "hello/hello_there.html",
        {
            "name": name,
            "date": now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        message = form.save(commit=False)
        message.log_date = now()
        message.save()
        return redirect("home")
    return render(request, "hello/log_message.html", {"form": form})
