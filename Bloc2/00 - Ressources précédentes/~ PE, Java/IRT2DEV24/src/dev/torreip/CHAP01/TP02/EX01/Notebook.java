package dev.torreip.CHAP01.TP01.EX01;

public class Notebook {

    //Attribute
    private String courseName;

    //Constructor
    public Notebook() {
        this.courseName = "IRT2 - JAVA";
    }

    public Notebook(String courseName) {
        this.courseName = courseName;
    }

    //Method
    //public, private, protected
    //types int String

    /*
    B)
    public void displayMessage(courseName) {
        System.out.println("Welcome to the notebook for " + courseName + " course!");
    }

     */

    public void displayMessage() {
        //Instructions
        System.out.println("Welcome to the notebook for " + courseNameGet() + " course!");
    }

    public void courseNameSet(String courseName){
        this.courseName = courseName;
    }

    public String courseNameGet(){
        return this.courseName;
    }

}
