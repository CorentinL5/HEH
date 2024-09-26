package dev.torreip.CHAP02.TP03.EX02;

public class WeatherDataTest {
    public static void main(String[] args) {
        WeatherData weatherStation = new WeatherData();

        ShowDataObserver showData = new ShowDataObserver(weatherStation);
        StatsObserver stats = new StatsObserver(weatherStation);

        weatherStation.add(showData);
        weatherStation.add(stats);

        weatherStation.setData(10,55);
        weatherStation.setData(22,11);
        weatherStation.setData(444,22);


    }
}
