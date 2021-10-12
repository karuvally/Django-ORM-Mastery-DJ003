from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q

# Part 2
#################################################################
"""
def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list_(request):
    posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list(request):
    posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

    print(posts)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

# OR query
def student_list(request):
    posts = Student.objects.filter(firstname__startswith="raq") | Student.objects.filter(surname__startswith="austin")
    print(posts.query)
    return render(
        request,
        "output.html",
        {
            "posts": posts,
            "sql_query": posts.query
        }
    )

# OR query with QObjects
def student_list(request):
    # Select students whose firstname starts with "raq" and lastname does not start with "austin"
    posts = Student.objects.filter(Q(firstname__startswith="raq") | ~Q(surname__startswith="austin"))
    print(posts.query)
    return render(
        request,
        "output.html",
        {
            "posts": posts,
            "sql_query": posts.query
        }
    )
"""

# AND query
def student_list(request):
    posts = Student.objects.filter(Q(firstname__startswith="raq") & Q(surname__startswith="avery"))
    print(posts, connection.queries)
    return render(
        request,
        "output.html",
        {
            "posts": posts,
            "sql_query": posts.query
        }
    )    
