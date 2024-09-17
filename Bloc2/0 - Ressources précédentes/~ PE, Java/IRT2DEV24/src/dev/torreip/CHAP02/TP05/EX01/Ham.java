package dev.torreip.CHAP02.TP05.EX01;

public class Ham extends ToppingsDecorator {

    Ham(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 2.75 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Ham";
    }
}
