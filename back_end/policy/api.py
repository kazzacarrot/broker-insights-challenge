from policy.models import Customer, Insurer, Policy, PolicyType
from tastypie.resources import ModelResource
from tastypie.fields import ForeignKey, CharField
# from django.db.models import CharField, F


class InsurerResource(ModelResource):
    class Meta:
        queryset = Insurer.objects.all()
        include_resource_uri = False


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        include_resource_uri = False

class PolicyResource(ModelResource):
    Insurer = ForeignKey(InsurerResource, "insurer", full=True)
    customer = ForeignKey(CustomerResource, "customer", full=True)
    policy_type = CharField(attribute="policy_type__name", null=True)

    class Meta:
        queryset = Policy.objects.all().annotate()
        include_resource_uri = False

    
