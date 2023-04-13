import numpy as np
import pandas as pd
from geopy import distance
from tqdm import tqdm

tqdm.pandas()


def longest_distance(row: pd.Series, df: pd.DataFrame) -> tuple[str, float]:
    from_city, lat, lng = row[:3]

    other_cities = df[df['city'] != from_city]

    distances = other_cities.apply(lambda row: distance.distance((lat, lng), (row['lat'], row['lng'])).km, axis=1)
    max_index = np.argmax(distances)

    furthest_city = other_cities.iloc[max_index][0]
    furthest_distance = distances.iloc[max_index]

    return furthest_city, furthest_distance


def shortest_distance(row: pd.Series, df: pd.DataFrame) -> tuple[str, float]:
    from_city, lat, lng = row[:3]

    other_cities = df[df['city'] != from_city]

    distances = other_cities.apply(lambda row: distance.distance((lat, lng), (row['lat'], row['lng'])).km, axis=1)
    # print("========")
    # print("shortest_distances: \n", distances.sort_values().head())
    min_index = np.argmin(distances)

    closest_city = other_cities.iloc[min_index][0]
    closest_distance = distances.iloc[min_index]

    # print(f"shortest_trip: {from_city}-{closest_city}({closest_distance} km)")
    # print("========")
    return closest_city, closest_distance


def format_trip(from_city, to_city, distance):
    return f'{from_city}-{to_city}({distance} km)'


capitals_df = pd.read_csv('https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/features/travel/worldcapitals_light.csv')
capitals_df = capitals_df[capitals_df['city'] != 'Al Quds']  # Jerusalem and Al Quds are the same city


def print_longest():
    longest_distances = capitals_df.progress_apply(lambda row: longest_distance(row, capitals_df), axis=1)
    capitals_df['furthest_city'] = [r[0] for r in longest_distances]
    capitals_df['furthest_distance'] = [r[1] for r in longest_distances]
    longest_trip = capitals_df.iloc[np.argmax(capitals_df['furthest_distance'])]
    print(f'The longest trip is {format_trip(longest_trip["city"], longest_trip["furthest_city"], longest_trip["furthest_distance"])}')


def print_shortest():
    shortest_distances = capitals_df.progress_apply(lambda row: shortest_distance(row, capitals_df), axis=1)
    capitals_df['closest_city'] = [r[0] for r in shortest_distances]
    capitals_df['closest_distance'] = [r[1] for r in shortest_distances]
    capitals_df.sort_values(by='closest_distance', inplace=True)
    print(f'capitals_df: \n', capitals_df.head())
    shortest_trip = capitals_df.iloc[0]
    print(f'The shortest trip is {format_trip(shortest_trip["city"], shortest_trip["closest_city"], shortest_trip["closest_distance"])}')


print_longest()
print_shortest()
