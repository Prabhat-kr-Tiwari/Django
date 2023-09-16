from django.shortcuts import render, redirect

# Create your views here.

# appname/views.py
# from django.shortcuts import render, redirect
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()  # Save the user data to the database
            # You should hash the password before saving it. Django's default authentication system can help with this.
            # Redirect to a success page or login page
            return redirect('login')  # Change 'login' to your login URL
    else:
        form = UserRegistrationForm()
    
    return render(request, 'signup.html', {'form': form})

