package dev.torreip.CHAP02.TP01.EX03;

public class File implements Composite {

    private String name;

    public File(String name) {
        this.name = name;
    }

    public void setFileName(String name){
        this.name = name;
    }
    @Override
    public String returnName() {
        return this.name;
    }
}
