package dev.torreip.CHAP02.TP03.EX01;

public class OctalObserver implements Observer {
    @Override
    public void update(int data) {
        System.out.println("Value in Octal: " + Integer.toOctalString(data));
    }
}
