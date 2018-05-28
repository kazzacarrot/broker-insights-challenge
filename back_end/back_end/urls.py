from django.conf.urls import url, include
from policy.api import PolicyResource, CustomerResource, InsurerResource

policy_resource = PolicyResource()
customer_resource = CustomerResource()
insurer_resource = InsurerResource()

app_name = "policy"

urlpatterns = [
    # The normal jazz here...
    url(r'^api/', include(policy_resource.urls)),
    url(r'^api/', include(customer_resource.urls)),
    url(r'^api/', include(insurer_resource.urls)),
]
