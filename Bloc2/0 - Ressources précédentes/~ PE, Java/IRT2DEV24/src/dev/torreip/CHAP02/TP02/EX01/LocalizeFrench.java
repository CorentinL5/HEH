package dev.torreip.CHAP02.TP02.EX01;

public class LocalizeFrench implements LocalizeStrategy {

    private final String localizedText;
    private double exchangeRate;
    private final String currency;

    public LocalizeFrench(){
        localizedText = "Le prix total de la facture est : ";
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
        return localizedText + (exchangeRate * price) + ' ' + currency;
    }
}
