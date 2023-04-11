import pandas as pd

country_names = ['Guinea', 'Iran', 'Trinidad and Tobago', 'Honduras', 'Lebanon',
                 'Ethiopia', 'Niger', 'Afghanistan', 'India', 'American Samoa',
                 'Cuba', 'Gabon', 'Nicaragua', 'Channel Islands', 'Martinique']

populations = pd.read_csv(
    'https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/misc/earth/population_by_country.csv',
)

surface_areas = pd.read_csv(
    'https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/misc/earth/surface_by_country.csv',
)

def mine():
    countries = populations.merge(surface_areas, on='Country (or dependency)', how='inner')
    countries = countries[countries['Country (or dependency)'].isin(country_names)]
    countries['Density'] = countries['Population (2020)'] / countries['Land Area (Km²)']
    countries['first_letter'] = countries['Country (or dependency)'].apply(lambda c: c[0])
    countries.sort_values(by='Density', ascending=False, inplace=True)

    print("".join(countries['first_letter']))


    # countries = [c for c in country_pop if c['name'] in country_names]
    # print(countries)

def theirs():
    # First merge the dataset together on the 'Country' field
    countries_merged = populations.merge(surface_areas, on='Country (or dependency)')
    # Filter the dataframe to the countries of interest
    countries_merged = countries_merged[countries_merged['Country (or dependency)'].isin(country_names)]

    # Compute the missing field Density
    countries_merged['Density'] = countries_merged['Population (2020)'] / countries_merged['Land Area (Km²)']

    # Sort the dataframe according to the Density field (descending)
    countries_merged = countries_merged.sort_values('Density', ascending=False)

    # Get the first letter of each country and concatenate them
    countries_merged['first_letter'] = countries_merged['Country (or dependency)'].apply(lambda x:x[0])

    # Get the first letter of each country and concatenate them
    message = ''.join(list(countries_merged['first_letter']))
    print(message)


mine()
theirs()
