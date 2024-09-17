package dev.torreip.CHAP02.TP02.EX01;

public class Invoice {

    private double price;
    private LocalizeStrategy displayLang;

    public Invoice(double price){
        this.price = price;
        this.displayLang = new LocalizeFrench();
    }

    public double getPrice(){
        return this.price;
    }

    public void setPrice(double price){
        this.price = price;
    }

    public void setDisplayLang(LocalizeStrategy local){
        this.displayLang = local;
    }

    public String showInvoice(){
        return this.displayLang.Display(price);
    }


}
