package com.yourpackage;

import com.yourpackage.config.Config;

public class Fuelgauge {
    private double fuelLevel;
    
    Fuelgauge() {
        this.fuelLevel = Config.MAX_FUEL_CAPACITY;
    }
    public double getFuelLevel() {
        return fuelLevel;
    }
    public void consumeFuel(double distanceTraveled) {
        double fuelConsumed = distanceTraveled * 0.1;
 //       this.fuelLevel = Math.max(0.0, this.fuelLevel - fuelConsumed);
        if (fuelLevel - fuelConsumed > 0) {
            fuelLevel -= fuelConsumed;
        } else {
            fuelLevel = 0.0;
            System.out.println("Fuel tank is empty");
        }

        if (fuelLevel <= Config.LOW_FUEL_WARNING) {
            System.out.println("Warning: Low Fuel");
        }

    }

}
