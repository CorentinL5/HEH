package Strategy;

import java.util.List;

public class Main {
    public static void main(String[] args){
        RepresentationsData representationsData = new RepresentationsData();
        representationsData.displayData(List.of(1,4,6,8));

        representationsData.setStrategyShowData(new BarChartStrategy());
        representationsData.displayData(List.of(1,4,6,8));
    }
}