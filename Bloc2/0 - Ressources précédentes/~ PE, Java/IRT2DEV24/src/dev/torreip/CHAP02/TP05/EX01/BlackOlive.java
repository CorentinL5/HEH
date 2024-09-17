package dev.torreip.CHAP02.TP05.EX01;

public class BlackOlive extends ToppingsDecorator {

    BlackOlive(Pizza pizza) {
        super(pizza);
    }

    @Override
    public double getCost() {
        return 1.2 + selectedPizza.getCost();
    }

    @Override
    public String getName() {
        return selectedPizza.getName() + " Black Olive";
    }
}
