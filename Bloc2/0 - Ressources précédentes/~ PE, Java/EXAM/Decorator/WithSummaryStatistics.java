package Decorator;

public class WithSummaryStatistics extends BaseDecorator {

    public WithSummaryStatistics(DataStatistics dataStatistics) {
        super(dataStatistics);
    }

    public void displayStatistics(){
        var sum = getData().stream().reduce(0.0, Double::sum);
        var min = getData().stream().min(Double::compareTo);
        var max = getData().stream().max(Double::compareTo);
        System.out.println("Number of recordings : " + getData().size());
        System.out.println("Sum of recordings : " + sum);
        System.out.println("Minimum value : " + min);
        System.out.println("Maximum value : " + max);
        System.out.println("---------------------------------------------------");
        this.dataStatistics.displayStatistics();
    }
}
