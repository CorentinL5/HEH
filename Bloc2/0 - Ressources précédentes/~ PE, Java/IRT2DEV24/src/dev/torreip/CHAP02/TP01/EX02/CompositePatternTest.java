package dev.torreip.CHAP02.TP01.EX02;

import java.util.Scanner;

public class CompositePatternTest {

    public static void main(String[] args) {

        Restaurant MCDonnalds = new Restaurant();
        MCDonnalds.setBenefit(42.069);

        Restaurant BurgerKing = new Restaurant();
        BurgerKing.setBenefit(11.22);

        City Mons = new City();
        Mons.add(MCDonnalds);

        City Quaregnon = new City();
        Quaregnon.add(MCDonnalds);
        Quaregnon.add(BurgerKing);

        State Hainaut = new State();
        Hainaut.add(Mons);
        Hainaut.add(Quaregnon);


        System.out.print(Hainaut.benefitCalc());
    }

}
