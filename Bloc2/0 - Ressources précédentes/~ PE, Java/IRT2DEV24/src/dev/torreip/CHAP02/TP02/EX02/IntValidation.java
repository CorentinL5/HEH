package dev.torreip.CHAP02.TP02.EX02;

public class IntValidation implements ValidationStrategy {

    @Override
    public boolean Validate(String data) {
        try {
            Integer.parseInt(data);
            return true;
        } catch (Exception e) {
            return false;
        }
        }
    }
