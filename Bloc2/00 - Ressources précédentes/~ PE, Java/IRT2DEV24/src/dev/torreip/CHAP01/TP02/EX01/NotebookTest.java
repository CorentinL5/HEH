package dev.torreip.CHAP01.TP01.EX01;

import java.util.Scanner;

public class NotebookTest {

    public static void main(String[] args) {

        String courseName;

        /*
            Two Step Process
            Notebook MyNotebook;
            MyNotebook = new Notebook();

         */

        Notebook MyNotebook = new Notebook("OwO");

        // Use The Method of MyNotebook
        Scanner courseScanner = new Scanner(System.in);

        // Initial Name
        MyNotebook.displayMessage();

        // Rename The Course Name
        System.out.print("Please define the course name for the notebook. ");
        courseName = courseScanner.nextLine();
        MyNotebook.courseNameSet(courseName);

        // Display The New Course Name
        MyNotebook.displayMessage();
    }
}
