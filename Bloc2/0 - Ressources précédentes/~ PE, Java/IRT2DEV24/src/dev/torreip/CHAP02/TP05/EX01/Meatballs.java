package dev.torreip.CHAP02.TP05.EX01;

public class Meatballs extends ToppingsDecorator {

    Meatballs(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 2.5 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Meatballs";
    }
}
