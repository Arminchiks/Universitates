from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from itertools import count
import json
import requests



api_url=("https://restcountries.com/v3.1/all")


try:
    response=requests.get(api_url)


    if response.status_code==200:
        countries_data=response.json()


        print("Visu  valstu nosaukumi")
        for country in countries_data:
            country_name= country.get("name",{}).get("common","Nezināms nosaukums")
            print(country_name)


        total_countries=len(countries_data)
        print(f"\nKopējais valstu skaits: {total_countries}")

        total_population=sum(country.get("population", 0) for country in countries_data)
        average_population=total_population / total_countries if total_countries else 0
        print(f"\n Vidējais iedzīvotāju skaits valstīs: {average_population:,.0f}") 

        largest_pop_country= max(countries_data, key=lambda x: x.get("population", 0))
        largest_pop_name= largest_pop_country.get("name", {}).get("common", "No name")
        largest_pop=largest_pop_country.get("population", 0)
        print(f"\nValsts ar vislielāko iedzīvotāju skaitu: {largest_pop_name} ({largest_pop:,.0f} iedzīvotāji)")

        total_area=sum(country.get("area", 0) for country in countries_data)
        print(f"\nVisu valstu kopējā platība: {total_area:,.0f} kvadrātkilometri")

        latvia_info=next((country for country in countries_data if country.get("name", {}).get("common")=="Latvia"), None)

        if latvia_info:

            subregion=latvia_info.get("subregion", "Nav pieejams")
            print(f"\nLatvijas apakšreģions {subregion}")

            borders=latvia_info.get("borders", "Nav pieejai robežvalstu kodi")
            print(f"Latvijas robežvalstu kodi: {borders}")
        else:
            print("Latvijas nav atrasta valstu sarakstā")
    else:
        print(f"Pieprasījuma kļuda. Statusa kods: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Notiksui kļūda pieprasījumā: {e}")


