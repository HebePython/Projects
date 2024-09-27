package com.yourpackage;

public class Fuelgauge {
    private double fuelLevel;
    
    Fuelgauge() {
        this.fuelLevel = 50.0;
    }
    public double getFuelLevel() {
        return fuelLevel;
    }
    public void consumeFuel(double distanceTraveled) {
        double fuelConsumed = distanceTraveled * 0.1;
        this.fuelLevel = Math.max(0.0, this.fuelLevel - fuelConsumed);
    }

}
