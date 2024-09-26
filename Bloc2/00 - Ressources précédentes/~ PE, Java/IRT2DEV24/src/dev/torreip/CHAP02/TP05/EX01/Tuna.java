package dev.torreip.CHAP02.TP05.EX01;

public class Tuna extends ToppingsDecorator {

    Tuna(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 5 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Tuna";
    }
}
