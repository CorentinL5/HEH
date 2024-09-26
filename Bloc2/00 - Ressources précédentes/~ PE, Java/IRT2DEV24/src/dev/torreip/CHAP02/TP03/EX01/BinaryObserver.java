package dev.torreip.CHAP02.TP03.EX01;

public class BinaryObserver implements Observer {
    @Override
    public void update(int data) {
        System.out.println("Value in Binary: " + Integer.toBinaryString(data));
    }
}
