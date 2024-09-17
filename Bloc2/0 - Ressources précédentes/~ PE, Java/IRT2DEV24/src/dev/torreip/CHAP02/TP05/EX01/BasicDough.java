package dev.torreip.CHAP02.TP05.EX01;

public class BasicDough implements Pizza {
    private final String name;
    private final double price;

    BasicDough() {
        this.name = "Basic Dough";
        this.price = 5;
    }

    @Override
    public double getCost() {
        return this.price;
    }

    public String getName() {
        return name;
    }
}
