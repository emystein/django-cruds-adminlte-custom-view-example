# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Department(models.Model):
    name = models.CharField(unique=True, max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class KnowledgeBase(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    knowledge_base = models.ForeignKey(KnowledgeBase, on_delete=models.CASCADE)
    text = models.TextField(unique=True)
    answer = models.TextField()

    def __str__(self):
        return self.text
