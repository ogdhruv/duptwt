from django.urls import path
from quotes.views import QuoteCreate,IndividualCreate,QuoteList,ListQuoteAPI,DetailQuoteAPI,endpoints

urlpatterns = [
    path("",QuoteList.as_view(),name="quotes"),
    path("createquote/",QuoteCreate.as_view(),name="createquote"),
    path("createindividual/",IndividualCreate.as_view(),name="createindividual"),
    
    path("api/",view=endpoints,name="api"),
    path("api/quotes",view=ListQuoteAPI.as_view(),name="listapi"),
    path("api/quotes/<int:pk>",view=DetailQuoteAPI.as_view(),name="detailedapi")

]