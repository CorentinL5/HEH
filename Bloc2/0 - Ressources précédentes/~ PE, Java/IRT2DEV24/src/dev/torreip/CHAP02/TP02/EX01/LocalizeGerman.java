package dev.torreip.CHAP02.TP02.EX01;

public class LocalizeGerman implements LocalizeStrategy {

    private final String localizedText;
    private double exchangeRate;
    private final String currency;

    public LocalizeGerman(){
        localizedText = "Der Gesamtpreis der Rechnung : ";
        exchangeRate = 1;
        currency = "€";
    }

    public double getExchangeRate() {
        return exchangeRate;
    }

    public void setExchangeRate(double exchangeRate) {
        this.exchangeRate = exchangeRate;
    }

    @Override
    public String Display(double price) {
        return localizedText + currency + ' ' + (exchangeRate * price);
    }
}
