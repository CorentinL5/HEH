package dev.torreip.CHAP02.TP03.EX01;

import java.util.Scanner;

public class ValueScannerTest {
    public static void main(String[] args) {
        ValueScanner updater = new ValueScanner();
        BinaryObserver binaryConvertor = new BinaryObserver();
        HexObserver hexConverter = new HexObserver();
        OctalObserver octalObserver = new OctalObserver();

        updater.add(binaryConvertor);
        updater.add(hexConverter);
        updater.add(octalObserver);

        Scanner scanner = new Scanner(System.in);

        while(true){
            System.out.print("Please Input an Integer: ");
            int value = scanner.nextInt();
            System.out.println("-----------------------");
            updater.setInput(value);
        }
    }
}
