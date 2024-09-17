package dev.torreip.CHAP02.TP02.EX01;

public class LocalizeEnglishUK implements LocalizeStrategy {

    private final String localizedText;
    private double exchangeRate;
    private final String currency;

    public LocalizeEnglishUK(){
        localizedText = "The total invoice price is :¨";
        exchangeRate = 1.17;
        currency = "£";
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
