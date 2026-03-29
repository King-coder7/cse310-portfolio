from django.shortcuts import render

# 1. Home Page View
def home(request):
    return render(request, 'portfolio_app/home.html')

# 2. Projects Gallery View (Dynamic Content)
def projects(request):
    # This list acts as our data source to dynamically generate the page
    my_projects = [
        {'title': 'Python Web Scraper', 'description': 'Automated data extraction.'},
        {'title': 'Django Portfolio', 'description': 'My CSE 310 Module 5 project.'},
    ]
    # We pass this data to the template
    return render(request, 'portfolio_app/projects.html', {'projects': my_projects})

# 3. Contact Form View (Interactivity / User Input)
def contact(request):
    context = {}
    # This block handles the user input when they click "Submit"
    if request.method == 'POST':
        user_name = request.POST.get('name')
        # Creates a dynamic message to send back to the page
        context['message'] = f"Thanks for reaching out, {user_name}!"
    
    return render(request, 'portfolio_app/contact.html', context)