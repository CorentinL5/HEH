package Decorator;

import java.util.List;

public abstract class BaseDecorator implements DataStatistics {
    DataStatistics dataStatistics;
    public BaseDecorator(DataStatistics dataStatistics) {
        this.dataStatistics = dataStatistics;
    }

    public List<Double> getData() {
        return dataStatistics.getData();
    }
}
