package Decorator;

import java.util.List;

public class BaseDataStatistics implements DataStatistics {
    private List<Double> data;

    public BaseDataStatistics(List<Double> data) {
        this.data = data;
    }

    @Override
    public void displayStatistics() {
        System.out.println("Data List :");
        for(int i = 0; i < data.size(); i++) {
            System.out.println(data.get(i));
        }
        System.out.println("---------------------------------------------------");
    }

    @Override
    public List<Double> getData() {
        return this.data;
    }
}
