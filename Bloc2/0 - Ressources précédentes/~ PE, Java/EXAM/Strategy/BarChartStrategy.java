package Strategy;

import java.util.List;

public class BarChartStrategy implements DisplayStrategy{
    @Override
    public void displayData(List<Integer> data) {
        for(int i = 0; i < data.size(); i++) {
            String toPrint = String.valueOf(i+1);
            toPrint = toPrint + ": " + "*".repeat(data.get(i));
            System.out.println(toPrint);
        }
    }
}
