package Strategy;

import java.util.List;

public class RepresentationsData {
    private DisplayStrategy strategy;
    public RepresentationsData() {
        this.strategy = new PairsSetNotationStrategy();
    }
    public void setStrategyShowData(DisplayStrategy strategy) {
        this.strategy = strategy;
    }
    public void displayData(List<Integer> list) {
        this.strategy.displayData(list);
    }
}
