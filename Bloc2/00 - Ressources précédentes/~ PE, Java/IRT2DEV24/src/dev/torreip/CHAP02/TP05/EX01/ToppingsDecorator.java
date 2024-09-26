package dev.torreip.CHAP02.TP05.EX01;

public abstract class ToppingsDecorator implements Pizza {

    protected Pizza selectedPizza;
    ToppingsDecorator(Pizza pizza) {
        this.selectedPizza = pizza;
    };
}
