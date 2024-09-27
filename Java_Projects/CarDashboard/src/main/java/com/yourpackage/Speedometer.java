package com.yourpackage;

public class Speedometer {
    private double currentSpeed;

    Speedometer() {
        this.currentSpeed = 0.0;
    }
    public double getcurrentSpeed() {
        return currentSpeed;
    }
    public void increaseSpeed(double amount) {
        this.currentSpeed += amount;
    }
    public void descreaseSpeed(double amount) {
        this.currentSpeed -= Math.max(0.0, this.currentSpeed - amount);
    }

    
}
