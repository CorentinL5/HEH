package dev.torreip.CHAP02.TP01.EX03;

import java.util.ArrayList;

public class Folder implements Composite {

    private String name;
    private String allFiles;

    public Folder(String name) {
        this.name = name;
    }

    private final ArrayList<Composite> fileList = new ArrayList<>();

    public void setFileName(String name){
        this.name = name;
    }

    public String getFileName(){
        return this.name;
    }

    public void add(Composite file){
        fileList.add(file);
    }


    @Override
    public String returnName() {
        allFiles = this.getFileName();

        fileList.forEach((file) -> allFiles += file.returnName());
        return allFiles;
    }
}
