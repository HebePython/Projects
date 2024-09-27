package com.yourpackage;

public class Main {
    public static void main(String[] args) {
        Dashboard dashboard = new Dashboard();
        System.out.println("MAIN WORKS");

        dashboard.displayDashboard();

        dashboard.updateDashboard(60.0, 5.0); //incr speed 60 and travel 5km.
        dashboard.displayDashboard();
        
        dashboard.updateDashboard(-20.0, 2.0);
        dashboard.displayDashboard();
    }
}
