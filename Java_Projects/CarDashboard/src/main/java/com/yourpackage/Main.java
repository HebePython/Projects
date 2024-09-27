package com.yourpackage;

public class Main {
    public static void main(String[] args) {
        Dashboard dashboard = new Dashboard();
        
        dashboard.updateDashboard(60, 5.0); //incr speed 60 and travel 5km.

        System.out.println("MAIN WORKS");
    }
}
