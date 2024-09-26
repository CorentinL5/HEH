package dev.torreip.CHAP02.TP05.EX01;

public class PizzaTest {
    public static void main(String[] args) {
        Pizza myPizza = new BasicDough();
        System.out.println(myPizza.getName());
        System.out.println(myPizza.getCost());
        myPizza = new Meatballs(myPizza);
        myPizza = new Cheese(myPizza);
        myPizza = new Onions(myPizza);
        myPizza = new Meatballs(myPizza);
        myPizza = new Cheese(myPizza);
        myPizza = new Tuna(myPizza);
        myPizza = new Mushroom(myPizza);
        myPizza = new BlackOlive(myPizza);
        myPizza = new Ham(myPizza);
        System.out.println(myPizza.getName());
        System.out.println(myPizza.getCost());
    }
}
