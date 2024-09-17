package dev.torreip.CHAP02.TP02.EX02;

import dev.torreip.CHAP02.TP02.EX02.ValidationStrategy;

public class MailValidation implements ValidationStrategy {

    @Override
    public boolean Validate(String data) {
        return data.indexOf("@") != -1 ;
    }
}
