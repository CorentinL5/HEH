package dev.torreip.CHAP02.TP01.EX02;

import java.util.ArrayList;

public class State implements Composite {

    private final ArrayList<Composite> cityList;
    private double totalSales;

    public State(){
        cityList = new ArrayList<>();
    };

    public double getTotalSales() {
        return this.totalSales;
    }
    public void add(Composite city) {
        this.cityList.add(city);
    }

    @Override
    public double benefitCalc() {
        this.totalSales = 0.0;

        cityList.forEach((city) -> totalSales += city.benefitCalc());
        return this.totalSales;
    }
}
