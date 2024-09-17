package dev.torreip.CHAP02.TP01.EX03;

import dev.torreip.CHAP02.TP01.EX02.City;
import dev.torreip.CHAP02.TP01.EX02.Restaurant;
import dev.torreip.CHAP02.TP01.EX02.State;

public class CompositePatternTest {

    public static void main(String[] args) {

        String courseName;

        Folder Anime = new Folder("Anime\n");
        Folder Show = new Folder("Show\n");

        File Frieren = new File("Frieren\n");
        File MrRobot = new File("Mr.Robot");

        Anime.add(Frieren);
        Show.add(Anime);
        Show.add(MrRobot);


        System.out.print(Show.returnName());
    }

}
