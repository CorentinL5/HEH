package dev.torreip.CHAP01.TP01.EX02;

public class BankAccount {
    private double balance;

    public BankAccount() {
        balance = 0.0;
    }

    public BankAccount(double initBalance) {
        if (initBalance > 0.0) {
            balance = initBalance;
        } else {
            balance = 0.0;
        }
    }

    public void deposit(double moneyDeposited) {
        if(moneyDeposited > 0.0) {
            balance += moneyDeposited;
        } else {
          System.out.println("A Deposit Must be positive!");
        }
    }

    public double getBalance() {
        return balance;
    }
}
