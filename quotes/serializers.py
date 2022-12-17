from rest_framework import serializers
from quotes.models import Individual,Quote

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ["id","name"]


class QuoteSerializer(serializers.ModelSerializer):
    individual = IndividualSerializer()
    class Meta:
        model = Quote
        fields = ["id","quote","individual"]