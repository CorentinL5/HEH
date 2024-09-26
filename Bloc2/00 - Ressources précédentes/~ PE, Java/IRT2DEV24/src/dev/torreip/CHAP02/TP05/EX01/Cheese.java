package dev.torreip.CHAP02.TP05.EX01;

public class Cheese extends ToppingsDecorator {

    Cheese(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 1.5 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Cheese";
    }
}
