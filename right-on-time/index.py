import numpy as np
import matplotlib.pyplot as plt


GAME_TIME = 18 * 60  # 6pm in number of minutes from midnight
N_FRIENDS = 4
STD_DEV_ARRIVAL_TIME_MIN = 10


# ... and that's all!
# right_appointment_time = ?


def plot(distribution):
    mu, sigma = np.mean(distribution), np.std(distribution)
    count, bins, ignored = plt.hist(distribution, bins=50, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu)**2 / (2 * sigma**2)), linewidth=2, color='r')
    plt.show()


def format_time(minutes):
    hours = int(minutes // 60)
    minutes = int(minutes % 60)
    return f'{hours}:{minutes}pm'


def simulate_one_game_offset(n_friends, std_dev_arrival_time_min):
    return np.max([
        np.random.normal(0, std_dev_arrival_time_min)
        for _ in range(n_friends)
    ])


offsets = [simulate_one_game_offset(N_FRIENDS, STD_DEV_ARRIVAL_TIME_MIN) for _ in range(100000)]
offset_99p = np.percentile(offsets, 99)
answer = GAME_TIME - np.ceil(offset_99p)

print(f'99% of my friends will arrive at the game by {format_time(answer)}')

# mu = GAME_TIME
# sigma = STD_DEV_ARRIVAL_TIME_MIN


# lasts = np.array(lasts)
# lasts = np.sort(lasts)

# last_arrival_99p = np.percentile(lasts, 99)
# print(f'last friend will arrive at {format_time(answer)}')

# # print(f'99% of my friends will arrive at the game by {answer}')
# # hours = int(answer // 60)
# # minutes = int(answer % 60)

# # print(f'at {hours}:{minutes}pm')
