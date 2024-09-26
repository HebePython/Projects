package com.yourpackage;

public class Odometer {
    private double kmTraveled;
    
    Odometer(double disTraveled) {
        this.kmTraveled = disTraveled;
    }
    public double getKmTraveled() {
        return kmTraveled;
    }
    public void setKmTraveled(double kmTraveled) {
        this.kmTraveled = kmTraveled;
    }
}
