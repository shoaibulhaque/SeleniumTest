from django.shortcuts import render
from .models import Person  # Assuming you're using the Person model

def homepage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        birth_date = request.POST.get("birth_date")

        # Basic validation (enhance as needed)
        if not all([name, email]):
            # Handle missing required fields
            return render(request, "home.html", {"success": False, "error": "Please fill in all required fields."})

        # Create Person instance
        person = Person.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            address=address,
            birth_date=birth_date
        )

        return render(request, "home.html", {"success": True})
    else:
        return render(request, "home.html")
