package dev.torreip.CHAP02.TP03.EX02;

public class ShowDataObserver implements Observer {

    private WeatherData dataSource;

    public ShowDataObserver(WeatherData datasource){
        dataSource = datasource;
    }

    @Override
    public void update() {
        System.out.print("Temp: " + this.dataSource.getTemp() + " | " + "Humidity: " + this.dataSource.getHumidity() + "% ||| ");
    }
}
