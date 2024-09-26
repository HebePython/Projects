package com.yourpackage;

public class Dashboard {
    private Speedometer speedometer;
    private Fuelgauge fuelgauge;       
    private Odometer odometer;    
    
    Dashboard() { // constructor 
        speedometer = new Speedometer();
        fuelgauge = new Fuelgauge();
        odometer = new Odometer();
    }

    public void updateDashboard(double increaseSpeed, double distanceTraveled) {
        System.out.printf("\nCurrent Speed: %d\nDistance traveled: %.02f", speedometer.getcurrentSpeed(), distanceTraveled.getdistanceTraveled());
    }

}