capitalOfCountries={

    "France": "Paris",
    "Germany": "Berlin",
    "Turkey": "Ankara",
    "UK": "Londan",
    "Cute Country": None,
    "Best Country":None
}
def removedNone(anything):  #You can name anything you want as a parameter
    removedNone={} 
    for key,value in capitalOfCountries.items():
        if value is not None:
            removedNone[key]=value   
    return removedNone

print(removedNone(capitalOfCountries))


