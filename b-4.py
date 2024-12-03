def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    total_temperature = sum(weather["temperature"] for weather in weather_information)
    average_temperature = total_temperature / len(weather_information)
    print(average_temperature)
    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_stations = [
        weather["station"] for weather in weather_information if weather["prefecture"] == "大阪府"
    ]
    print(",".join(osaka_stations))
    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_temperatures = [
        weather["temperature"] for weather in weather_information if weather["prefecture"] == "福岡県"
    ]
    average_fukuoka_temperature = sum(fukuoka_temperatures) / len(fukuoka_temperatures)
    print(average_fukuoka_temperature)


if __name__ == "__main__":
    main()
