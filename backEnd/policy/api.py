from policy.models import Customer, Insurer, Policy, PolicyType
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.fields import ForeignKey, CharField


class InsurerResource(ModelResource):
    class Meta:
        queryset = Insurer.objects.all()
        include_resource_uri = False
        filtering = {
                "id": ALL,
                "name": ALL,
        }


class CustomerResource(ModelResource):
    class Meta:
        queryset = Customer.objects.all()
        include_resource_uri = False

        filtering = {
                "id": ALL,
                "name": ALL,
                "address": ALL,
        }


class PolicyResource(ModelResource):
    insurer = ForeignKey(InsurerResource, "insurer", full=True)
    customer = ForeignKey(CustomerResource, "customer", full=True)
    policy_type = CharField(attribute="policy_type__name", null=True)

    class Meta:
        queryset = Policy.objects.all().annotate()
        include_resource_uri = False

        filtering = {
                "id": ALL,
                "premium": ALL,
                "customer": ALL_WITH_RELATIONS,
                "insurer": ALL_WITH_RELATIONS,
                "policy_type": ALL_WITH_RELATIONS,
        }
    
