from django.shortcuts import render, HttpResponse, redirect



def index(request):
    return render(request, "index.html")

def compressor_view(request):
    return render(request, "compressor.html")


# def login_view(request):
#     # Add your login logic here if needed
#    return render(request, 'login.html')

def contact_view(request):
    return render(request, 'contact.html')

def part1_view(request):
    return render(request, "part1.html")

def part2_view(request):
    return render(request, "part2.html")

def part3_view(request):
    return render(request, "part3.html")

def part4_view(request):
    return render(request, "part4.html")

def part5_view(request):
    return render(request, "part5.html")

def chiller_view(request):
    return render(request, "chiller.html")

def hydraulicpump_view(request):
    return render(request, "hydraulicpump.html")

def notification_view(request):
    return render(request, "notification.html")


def part6_view(request):
    return render(request, "part6.html")

def part7_view(request):
    return render(request, "part7.html")

def part8_view(request):
    return render(request, "part8.html")

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the 'index' page after successful login
            print(f"User '{username}' has logged in.")  # Print the message to the console
            return redirect('index')
        else:
            # Handle invalid login
            print(f"Login attempt failed for user '{username}'.")  # Print the message to the console
            return render(request, 'login.html', {'error_message': 'Invalid username or password', 'username': f'{username}'})
    else:
        return render(request, 'login.html')