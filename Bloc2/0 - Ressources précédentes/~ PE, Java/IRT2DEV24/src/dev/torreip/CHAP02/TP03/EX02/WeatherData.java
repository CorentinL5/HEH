package dev.torreip.CHAP02.TP03.EX02;

import java.util.ArrayList;

public class WeatherData extends Subject {

    private int temp;
    private int humidity;
    private final ArrayList<Observer> observerList;

    public WeatherData(){
        observerList = new ArrayList<>();
    }

    public void setData(int temp, int humidity) {
        this.temp = temp;
        this.humidity = humidity;
        this.ntfy();
    }

    public int getTemp() {
        return temp;
    }

    public void setTemp(int temp) {
        this.temp = temp;
    }

    public int getHumidity() {
        return humidity;
    }

    public void setHumidity(int humidity) {
        this.humidity = humidity;
    }

    @Override
    public void add(Observer observer){
        observerList.add(observer);
    }

    @Override
    public void ntfy() {
        observerList.forEach(Observer::update);
        System.out.println("\n-----------------------");
    }

}
