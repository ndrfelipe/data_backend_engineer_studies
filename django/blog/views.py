from django.shortcuts import render

# Create your views here.
def blog(request):
    # function-based view
    return render(
        request,
        'blog/index.html'
    )

def example(request):
    # function-based view
    return render(
        request,
        'blog/example.html'
    )