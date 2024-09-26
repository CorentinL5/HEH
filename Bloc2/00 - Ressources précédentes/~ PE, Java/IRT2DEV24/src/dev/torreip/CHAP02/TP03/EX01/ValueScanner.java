package dev.torreip.CHAP02.TP03.EX01;

import java.util.ArrayList;

public class ValueScanner extends Subject {

    private int input;
    private final ArrayList<Observer> observerList;

    public ValueScanner(){
        observerList = new ArrayList<>();
    }

    public void setInput(int input) {
        this.input = input;
        this.ntfy();
    }

    @Override
    public void add(Observer observer){
        observerList.add(observer);
    }

    @Override
    public void ntfy() {
        observerList.forEach(observer -> {observer.update(input);});
    }
}
