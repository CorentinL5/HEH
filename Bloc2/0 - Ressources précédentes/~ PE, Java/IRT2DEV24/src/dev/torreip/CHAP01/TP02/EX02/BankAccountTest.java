package dev.torreip.CHAP01.TP01.EX02;

public class BankAccountTest {


    public static void main(String[] args) {
        BankAccount MyBankAccount = new BankAccount();
        BankAccount MyNegativeBankAccount = new BankAccount(-12);
        BankAccount MyRichFriend = new BankAccount(9999999.9999999);

        System.out.println(MyNegativeBankAccount.getBalance());
        System.out.println(MyBankAccount.getBalance());
        MyBankAccount.deposit(10);
        MyBankAccount.deposit(-10.12);
        System.out.println(MyNegativeBankAccount.getBalance());
        System.out.println(MyBankAccount.getBalance());
        System.out.println(MyRichFriend.getBalance());


    }
}
