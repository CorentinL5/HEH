package dev.torreip.CHAP02.TP02.EX01;

public class InvoiceTest {
    public static void main(String[] args){
        Invoice myInvoice = new Invoice(50.50);
        System.out.println("Default (French)");
        System.out.println("----------------");
        System.out.println(myInvoice.showInvoice());
        System.out.println("\nGerman");
        System.out.println("----------------");
        myInvoice.setDisplayLang(new LocalizeGerman());
        System.out.println(myInvoice.showInvoice());
        System.out.println("\nEnglish (UK)");
        System.out.println("----------------");
        myInvoice.setDisplayLang(new LocalizeEnglishUK());
        System.out.println(myInvoice.showInvoice());
    }
}
