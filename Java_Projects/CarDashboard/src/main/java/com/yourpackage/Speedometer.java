package com.yourpackage;

public class Speedometer {
    private double currentSpeed;

    Speedometer() {
        this.currentSpeed = 0;
    }
    public double getcurrentSpeed() {
        return currentSpeed;
    }
    public void increaseSpeed(int amount) {
        this.currentSpeed += amount;
    }
    public void descreaseSpeed(int amount) {
        this.currentSpeed -= Math.max(0, this.currentSpeed - amount);
    }

    
}
