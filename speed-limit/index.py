from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 90 + 70 + 130 + 30 + 50 +100

def plot(distribution):
    mu, sigma = np.mean(distribution), np.std(distribution)
    count, bins, ignored = plt.hist(distribution, bins=50, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
    plt.show()

def find_speed_limit(road_df: pd.DataFrame) -> float:
    return 10 * int(np.percentile(road_df['speed'], q = 95) / 10)

def find_biggest_speeder(road_df: pd.DataFrame) -> float:
    licenses = road_df['license']
    max_speed = road_df['speed'].max()
    license = road_df[road_df['speed'] == max_speed]['license'].values[0]

    return (license, max_speed)

speeds_df = pd.read_csv('https://raw.githubusercontent.com/hyperc54/data-puzzles-assets/master/visualisation/speeds_data.csv')
speeds_by_road = speeds_df.groupby('road')
speed_limits_by_road = speeds_by_road.apply(find_speed_limit)

speeds_df['limit'] = speeds_df['road'].map(speed_limits_by_road)
speeds_df['percent_of_limit'] = speeds_df['speed'] / speeds_df['limit']
speeds_df.sort_values('percent_of_limit', ascending=False, inplace=True)
print(speeds_df.head())

# speeders_by_road = speeds_by_road.apply(find_biggest_speeder)

# percent_of_limit = [(speeder / limit) for limit, speeder in zip(speed_limits_by_road, speeders_by_road)]

# max_percent_of_limit = np.max(percent_of_limit)

# print(f'{max_percent_of_limit * 100}%')

# # for road, road_df in speeds_by_road:
# #     print(road)
# #     print(road_df.head())
# #     print()
