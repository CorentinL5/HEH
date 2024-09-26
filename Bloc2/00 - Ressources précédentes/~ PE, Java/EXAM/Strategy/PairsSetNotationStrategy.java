package Strategy;

import java.util.List;

public class PairsSetNotationStrategy implements DisplayStrategy {

    @Override
    public void displayData(List<Integer> data) {
        StringBuilder toPrint = new StringBuilder("{");
        for(int i = 0; i < data.size()-1; i++) {
            toPrint.append("(").append(i+1).append(",").append(data.get(i)).append("),");
        }
        toPrint.append('(').append(data.size()).append(",").append(data.get(data.size()-1)).append(")}");
        System.out.println(toPrint);
    }
}
