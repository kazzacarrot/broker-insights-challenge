from __future__ import unicode_literals

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)


class Insurer(models.Model):
    """
    Improvement beyond the scope of this task,
    add a table to link the Insurers to policy types.
    """
    name = models.CharField(max_length=50)


class PolicyType(models.Model):
    name = models.CharField(max_length=50)


class Policy(models.Model):
    """
    Policies have a customer, a premium, a policy_type and an insurer.
    Assumptions:
    1. When a customer leaves their policies don't matter to the broker anymore.
      IE, if fast taxis moves to a different broker, then Achme can delete all their policies.
    2. If a certain policy type is no longer supported, Achme would want to convert the policies to another type.
      IE, if the broker decides to stop supporting "Motor Fleet" insurance, then Achme would contact the companies that use motor fleet insurance to 
    3. If an insurer leaves the company may want to keep their clients. 
      IE, if QBE leaves, then Achme wouldn't want to delete the policy beteen fast taxis and QBE, they'd want to convert it to Aviva or what have you.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    premium = models.DecimalField(max_digits=7, decimal_places=2)
    policy_type = models.ForeignKey(PolicyType, on_delete=models.CASCADE)
    insurer = models.ForeignKey(Insurer, on_delete=models.PROTECT)


