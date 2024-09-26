package com.yourpackage;

public class Odometer {
    private double distanceTraveled;
    
    Odometer() {
        this.distanceTraveled = 0;
    }
    public double getdistanceTraveled() {
        return distanceTraveled;
    }
    public void updateDistance(double amount) {
        this.distanceTraveled += amount;
    }
}
