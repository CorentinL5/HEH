package dev.torreip.CHAP02.TP01.EX02;

public class Restaurant implements Composite {

    private double benefit;

    public void setBenefit(double value) {
        benefit = value;
    }

    public double getBenefit() {
        return this.benefit;
    }

    @Override
    public double benefitCalc() {
        return this.benefit;
    }
}
