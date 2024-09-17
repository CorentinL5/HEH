package dev.torreip.CHAP02.TP02.EX02;

public class ValidatorTest {
    public static void main(String[] args) {
        Validator dataValidator;
        String data;

        data = "23";
        dataValidator = new Validator(new IntValidation(), data);
        System.out.println("Valid Integer ? " + dataValidator.isValid());
        dataValidator = new Validator(new MailValidation(), data);
        System.out.println("Valid Mail ? "+dataValidator.isValid());

        System.out.println("------------------");

        data = "uwu@kawai.moe";
        dataValidator = new Validator(new IntValidation(), data);
        System.out.println("Valid Integer ? " + dataValidator.isValid());
        dataValidator = new Validator(new MailValidation(), data);
        System.out.println("Valid Mail ? "+dataValidator.isValid());
    }
}
