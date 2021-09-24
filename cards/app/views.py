from django.shortcuts import render, redirect

cards = [
    {
        "id": 1,
        "name": "Mercedes A Class",
        "image": "https://i.auto-bild.de/mdb/extra_large/62/aklasse-bb5.png",
        "description": "This is a Mercedess A-Class from autobild.de website.",
        "color": "silver",
    },
    {
        "id": 2,
        "name": "Audi A1",
        "image": "https://i.auto-bild.de/mdb/extra_large/65/a1-e91.png",
        "description": "This is an Audi A1 from autobild.de website.",
        "color": "brown",
    },
    {
        "id": 3,
        "name": "BMW 2er Gran Tourer",
        "image": "https://i.auto-bild.de/mdb/extra_large/99/2ergrantourer-a02.png",
        "description": "This is a beautiful BMW from autobild.de website.",
        "color": "blue",
    },
    {
        "id": 4,
        "name": "Chevrolet Camaro",
        "image": "https://i.auto-bild.de/mdb/extra_large/53/fourthgeneration-439.jpg",
        "description": "This is a Chevrolet Camaro 4th Generation.",
        "color": "red",
    },
]


def index(request):
    return render(request, "index.html", context={"cards": cards})


def command(request, id, cmd):
    for card in cards:
        if id == card["id"]:
            if cmd == "delete":
                cards.remove(card)
            if cmd == "color":
                colors = ["red", "blue", "green", "silver", "brown"]
                card["color"] = colors[(colors.index(card["color"]) + 1) % len(colors)]
    return redirect("/")
