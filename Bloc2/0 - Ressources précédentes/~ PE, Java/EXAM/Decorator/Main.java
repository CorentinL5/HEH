package Decorator;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        DataStatistics dataStatistics = new BaseDataStatistics(List.of(1.0,2.0,3.0));
        DataStatistics withMeanStatistics = new WithMeanStatistics(dataStatistics);
        DataStatistics withSummaryStatistics = new WithSummaryStatistics(withMeanStatistics);
        withSummaryStatistics.displayStatistics();
    }
}
