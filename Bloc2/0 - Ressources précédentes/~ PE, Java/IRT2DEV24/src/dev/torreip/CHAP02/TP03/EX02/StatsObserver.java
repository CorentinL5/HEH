package dev.torreip.CHAP02.TP03.EX02;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class StatsObserver implements Observer {

    private ArrayList<Integer> previousTemps = new ArrayList<>();
    private WeatherData dataSource;

    public StatsObserver(WeatherData dataSource){
        this.dataSource = dataSource;
    }

    @Override
    public void update() {
        previousTemps.add(dataSource.getTemp());
        double sum = 0.0;
        for(int i = 0; i < previousTemps.size(); i++)
        {
            sum = sum + previousTemps.get(i);
        }
        sum = sum/previousTemps.size();
        System.out.print("The Min/Average/Max are: " + Collections.min(previousTemps) + "/" + sum  + "/" + Collections.max(previousTemps));
    }
}
