package dev.torreip.CHAP02.TP01.EX02;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class City implements Composite {

    private final ArrayList<Composite> restList = new ArrayList<>();
    private double totalSales;

    public double getTotalSales() {
        return this.totalSales;
    }

    public void add(Composite restaurant) {
        this.restList.add(restaurant);
    }

    @Override
    public double benefitCalc() {
        this.totalSales = 0.0;

        Composite restaurant;
        for(Iterator<Composite> var1 = this.restList.iterator(); var1.hasNext(); this.totalSales += restaurant.benefitCalc()) {
            restaurant = (Composite) var1.next();
        }

        return this.totalSales;
    }
}
