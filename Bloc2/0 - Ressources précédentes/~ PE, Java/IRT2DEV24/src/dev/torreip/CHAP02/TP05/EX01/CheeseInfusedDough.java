package dev.torreip.CHAP02.TP05.EX01;

public class CheeseInfusedDough implements Pizza {
    private final String name;
    private final double price;

    CheeseInfusedDough() {
        this.name = "Cheese Infused Dough";
        this.price = 10;
    }

    @Override
    public double getCost() {
        return this.price;
    }

    public String getName() {
        return name;
    }
}
