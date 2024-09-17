package dev.torreip.CHAP02.TP05.EX01;

public class ThinDough implements Pizza {
    private final String name;
    private final double price;

    ThinDough() {
        this.name = "Thin Dough";
        this.price = 3;
    }

    @Override
    public double getCost() {
        return this.price;
    }

    public String getName() {
        return name;
    }
}
