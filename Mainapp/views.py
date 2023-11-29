from django.shortcuts import render

def homepage(Request):
    return render(Request,"index.html")

def aboutpage(Request):
    return render(Request,"about.html")

def servicepage(Request):
    return render(Request,"service.html")

def projectpage(Request):
    return render(Request,"project.html")

def blogpage(Request):
    return render(Request,"blog.html")

def teampage(Request):
    return render(Request,"team.html")


def testimonialpage(Request):
    return render(Request,"testimonial.html")


def contactpage(Request):
    return render(Request,"contact.html")
