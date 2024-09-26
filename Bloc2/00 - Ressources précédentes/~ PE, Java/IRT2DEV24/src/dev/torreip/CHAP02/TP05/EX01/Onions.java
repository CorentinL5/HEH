package dev.torreip.CHAP02.TP05.EX01;

public class Onions extends ToppingsDecorator {

    Onions(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 0.8 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Onions";
    }
}
