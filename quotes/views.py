from django.urls import reverse_lazy
from django.views import generic
from quotes.models import Quote,Individual
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from quotes.serializers import QuoteSerializer

# api views
@api_view(["GET"])
def endpoints(request):
    data = {
        "/api/quotes",
        "/api/individual",
        "/api/quotes/<int:pk>",
    }
    return Response(data)   


class ListQuoteAPI(generics.ListCreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class DetailQuoteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# frontend views
class QuoteCreate(generic.CreateView):
    model = Quote
    template_name = "quotes/form.html"
    fields = '__all__'
    success_url = reverse_lazy("quotes")

class IndividualCreate(generic.CreateView):
    model = Individual
    template_name = "quotes/form.html"
    fields = '__all__'
    success_url = reverse_lazy("createquote")


class QuoteList(generic.ListView):
    model=Quote
    template_name = "quotes/all_quotes.html"
    context_object_name = "quotes"
    paginate_by = 5
    
    queryset = Quote.objects.all().order_by("-pk")