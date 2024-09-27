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
        speedometer.increaseSpeed(increaseSpeed);
        odometer.updateDistance(distanceTraveled);
  
    }

    public void displayDashboard() {
        System.out.println("DASHBOARD WORKS");
        
    }
}