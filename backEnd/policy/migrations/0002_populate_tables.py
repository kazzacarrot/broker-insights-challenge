# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-05-27 15:04
from __future__ import unicode_literals

from django.db import migrations

insert_statements = """

INSERT INTO policy_customer ("id", "name", "address") VALUES 
  (1, "ABC Joinery", "12 Ascott Street, Dundee"),
  (2, "XYZ Plumbing", "24 Fleet Street, Glasgow"), 
  (3, "Fast Taxis", "324b Bank Street, Aberdeen");

INSERT INTO policy_policytype ("id", "name") VALUES
  (1, "Public Liability"),
  (2, "Motor Fleet");

INSERT INTO policy_insurer ("id", "name") VALUES
  (1, "Aviva"),
  (2, "Allianz"),
  (3, "QBE");

INSERT INTO policy_policy ("customer_id", "premium", "insurer_id", "policy_type_id") VALUES
  (1, 123.87,   1, 1),
  (2, 2321.45,  2, 1), 
  (3, 59897.00, 1, 2),
  (3, 6845.00,  3, 1);
"""

delete_statements = """
DELETE FROM policy_customer;
DELETE FROM policy_type;
DELETE FROM policy_insurer;
DELETE FROM policy_policy;

"""

class Migration(migrations.Migration):

    dependencies = [
        ('policy', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(insert_statements, reverse_sql=delete_statements)

    ]
