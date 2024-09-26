package dev.torreip.CHAP02.TP05.EX01;

public class Mushroom extends ToppingsDecorator {

    Mushroom(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 3 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Mushroom";
    }
}
