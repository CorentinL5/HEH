package Decorator;

public class WithMeanStatistics extends BaseDecorator {

    public WithMeanStatistics(DataStatistics dataStatistics) {
        super(dataStatistics);
    }

    public void displayStatistics(){
        var sum = getData().stream().reduce(0.0, Double::sum);
        System.out.println("Average : " + sum/getData().size());
        System.out.println("---------------------------------------------------");
        this.dataStatistics.displayStatistics();
    }
}
