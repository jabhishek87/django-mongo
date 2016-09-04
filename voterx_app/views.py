import json
from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse
from django.core.urlresolvers import RegexURLPattern, RegexURLResolver
from voterx_app.patch import JsonResponse
from voterx_app.models import models
from voterx_app import exceptions

def index(request):
    return JsonResponse({"msg":"JsonResponse"})


class BaseView(View):

    def __init__(self):
        self.base_excluded_fields_type = ['DateTimeField']
        self._allowed_fields =self.get_model_fields()

    def query_set_dict(self, query_set):
        return [entry.as_dict() for entry in query_set]

    def get_model_fields(self):
        all_fields = self.model._meta.fields
        return [
            field.name
            for field in all_fields
            if field.get_internal_type() not in self.base_excluded_fields_type
        ]

    def get(self, request):
        query_set = self.model.objects.all()
        # json_data = serializers.serialize('json', query_set)
        return JsonResponse(self.query_set_dict(query_set), safe=False)
        #return HttpResponse(json_data, content_type='application/json')

    def post(self, request):
        if request.body:
            #import ipdb; ipdb.set_trace()
            try:
                data = json.loads(request.body)
                new_rec = self.model()
                for field, val in data.iteritems():
                    setattr(new_rec, field, val)

                new_rec.save()
            except ValueError:
                raise ValueError('Json Cannot Be Decoded')

        return JsonResponse(new_rec.as_dict(), safe=False)

    def put(self, request):
        raise exceptions.MethodNotImplementedError()

    def patch(self, request):
        raise exceptions.MethodNotImplementedError()


class NameView(BaseView):
    model = models.Name


class DemographicsView(BaseView):
    model = models.Demographics


class ResidenceView(BaseView):
    model = models.Residence


class PhoneNumberView(BaseView):
    model = models.PhoneNumber


class EmailView(BaseView):
    model = models.Email


class CommercialView(BaseView):
    model = models.Commercial


class PartyView(BaseView):
    model = models.Party


class DistrictView(BaseView):
    model = models.District


class Commercial2View(BaseView):
    model = models.Commercial2


class CommercialfecView(BaseView):
    model = models.Commercialfec


class CommercialinterestsView(BaseView):
    model = models.Commercialinterests


class CommercialhomepurchasingView(BaseView):
    model = models.Commercialhomepurchasing


class VotehistoryView(BaseView):
    model = models.Votehistory


class CsDrtvVoterView(BaseView):
    model = models.CsDrtvVoter


class R7L2VoterView(BaseView):
    model = models.R7L2Voter


class AggregatedVoterView(BaseView):
    model = models.AggregatedVoter



