package dev.torreip.CHAP02.TP02.EX02;

public class Validator {
    private String data;
    private ValidationStrategy dataValidation;

    public Validator(ValidationStrategy validation, String data) {
        this.dataValidation = validation;
        this.data = data;
    }

    public boolean isValid(){
        return this.dataValidation.Validate(this.data);
    }
}
