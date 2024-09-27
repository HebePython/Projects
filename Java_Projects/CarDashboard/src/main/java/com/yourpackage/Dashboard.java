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

    public void updateDashboard(double speed, double distanceTraveled) { //updates dashboard with info when called.
        speedometer.increaseSpeed(speed);
        odometer.updateDistance(distanceTraveled);
        fuelgauge.consumeFuel(distanceTraveled);
 
    }

    public void displayDashboard() {
        System.out.println("Speed: " + speedometer.getcurrentSpeed() +" km/h    Distance: " + odometer.getdistanceTraveled() + " km    Fuel: " + fuelgauge.getFuelLevel() + " liters");

        
    }
}