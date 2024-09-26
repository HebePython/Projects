package com.yourpackage;

public class CarDashboard {
    private Fuelgauge fuel = new Fuelgauge(0);         //litres
    private Odometer kmTraveled = new Odometer(0);    // distance traveled in km
    private Speedometer currentSpeed = new Speedometer(0);      // km/h
    
    CarDashboard() { //remove?

    }

    public static void main(String[] args) {
        
        CarDashboard temp = new CarDashboard();

        System.out.println(temp.currentSpeed.getKmh());
        

    }
}